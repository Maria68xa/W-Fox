# W-Fox Parser
# هذا الملف يحول الـ Tokens إلى أوامر قابلة للتنفيذ

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from lexer import Token, TokenType, Lexer

@dataclass
class AssignmentStatement:
    """تمثيل أمر إسناد: Put 'x' = 10"""
    variable: str
    value: Any

@dataclass
class PrintStatement:
    """تمثيل أمر طباعة: print ['x']"""
    variable: str

@dataclass
class Expression:
    """تمثيل تعبير حسابي"""
    left: Any
    operator: Optional[str]
    right: Optional[Any]

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.statements = []
    
    def error(self, msg: str):
        token = self.current_token()
        raise Exception(f"Parser Error at line {token.line}, column {token.column}: {msg}")
    
    def current_token(self) -> Token:
        if self.pos >= len(self.tokens):
            return self.tokens[-1]  # EOF
        return self.tokens[self.pos]
    
    def peek_token(self, offset=1) -> Token:
        pos = self.pos + offset
        if pos >= len(self.tokens):
            return self.tokens[-1]
        return self.tokens[pos]
    
    def advance(self):
        self.pos += 1
    
    def expect(self, token_type: TokenType) -> Token:
        token = self.current_token()
        if token.type != token_type:
            self.error(f"Expected {token_type}, got {token.type}")
        self.advance()
        return token
    
    def parse_expression(self) -> Any:
        """تحليل التعبيرات الحسابية مثل: 10 & 5 ^ 2"""
        return self.parse_additive()
    
    def parse_additive(self):
        left = self.parse_multiplicative()
        
        while self.current_token().type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token().value
            self.advance()
            right = self.parse_multiplicative()
            left = Expression(left, op, right)
        
        return left
    
    def parse_multiplicative(self):
        left = self.parse_primary()
        
        while self.current_token().type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op = self.current_token().value
            self.advance()
            right = self.parse_primary()
            left = Expression(left, op, right)
        
        return left
    
    def parse_primary(self) -> Any:
        token = self.current_token()
        
        if token.type == TokenType.NUMBER:
            self.advance()
            return token.value
        
        elif token.type == TokenType.STRING:
            self.advance()
            return token.value
        
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return ("VAR", token.value)  # تمييز المتغيرات
        
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return expr
        
        else:
            self.error(f"Unexpected token: {token.type}")
    
    def parse_statement(self):
        """تحليل أمر واحد"""
        token = self.current_token()
        
        if token.type == TokenType.PUT:
            return self.parse_assignment()
        else:
            self.error(f"Unexpected token: {token.type}")
    
    def parse_assignment(self) -> AssignmentStatement:
        """تحليل أمر الإسناد: Put 'x' = value"""
        self.expect(TokenType.PUT)
        
        var_token = self.expect(TokenType.IDENTIFIER)
        variable = var_token.value
        
        self.expect(TokenType.EQUALS)
        
        value = self.parse_expression()
        
        return AssignmentStatement(variable, value)
    
    def parse_print_command(self) -> PrintStatement:
        """تحليل أمر الطباعة: print ['x']"""
        self.expect(TokenType.PRINT)
        self.expect(TokenType.LBRACKET)
        
        var_token = self.expect(TokenType.IDENTIFIER)
        variable = var_token.value
        
        self.expect(TokenType.RBRACKET)
        
        return PrintStatement(variable)
    
    def parse(self) -> List[Any]:
        """تحليل البرنامج كاملاً"""
        statements = []
        
        while self.current_token().type != TokenType.EOF:
            if self.current_token().type == TokenType.PUT:
                statements.append(self.parse_assignment())
            elif self.current_token().type == TokenType.PRINT:
                statements.append(self.parse_print_command())
            elif self.current_token().type == TokenType.COMMA:
                self.advance()  # تخطي الفاصلة
            elif self.current_token().type == TokenType.SEMICOLON:
                self.advance()  # تخطي النقطة والفاصلة
            else:
                self.error(f"Unexpected token: {self.current_token().type}")
        
        return statements
