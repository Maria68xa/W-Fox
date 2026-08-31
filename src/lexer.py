# W-Fox Lexer (Tokenizer)
# هذا الملف يقسم الأوامر إلى أجزاء صغيرة (Tokens)

import re
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class TokenType(Enum):
    # الكلمات المحجوزة
    PUT = "PUT"
    PRINT = "PRINT"
    
    # العمليات
    PLUS = "PLUS"        # & (جمع)
    MINUS = "MINUS"      # - (طرح)
    MULTIPLY = "MULTIPLY" # ^ (ضرب)
    DIVIDE = "DIVIDE"    # \ (قسمة)
    
    # الرموز
    EQUALS = "EQUALS"    # =
    COMMA = "COMMA"      # ,
    SEMICOLON = "SEMICOLON" # ;
    LPAREN = "LPAREN"    # (
    RPAREN = "RPAREN"    # )
    LBRACKET = "LBRACKET" # [
    RBRACKET = "RBRACKET" # ]
    
    # الأنواع
    IDENTIFIER = "IDENTIFIER"  # 'variable_name'
    NUMBER = "NUMBER"          # 123, 45.67
    STRING = "STRING"          # "hello"
    
    # النهاية
    EOF = "EOF"

@dataclass
class Token:
    type: TokenType
    value: any
    line: int
    column: int

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def error(self, msg: str):
        raise Exception(f"Lexer Error at line {self.line}, column {self.column}: {msg}")
    
    def current_char(self) -> Optional[str]:
        if self.pos >= len(self.text):
            return None
        return self.text[self.pos]
    
    def peek_char(self, offset=1) -> Optional[str]:
        pos = self.pos + offset
        if pos >= len(self.text):
            return None
        return self.text[pos]
    
    def advance(self):
        if self.pos < len(self.text):
            if self.text[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\n\r':
            self.advance()
    
    def read_identifier(self) -> str:
        """قراءة المتغيرات المحاطة بعلامات اقتباس"""
        quote = self.current_char()
        self.advance()  # تخطي علامة الاقتباس الأولى
        
        result = ""
        while self.current_char() and self.current_char() != quote:
            result += self.current_char()
            self.advance()
        
        if not self.current_char():
            self.error(f"Expected closing quote")
        
        self.advance()  # تخطي علامة الاقتباس الثانية
        return result
    
    def read_string(self) -> str:
        """قراءة النصوص المحاطة بعلامات اقتباس مزدوجة"""
        self.advance()  # تخطي علامة الاقتباس الأولى
        result = ""
        
        while self.current_char() and self.current_char() != '"':
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    result += '\n'
                elif self.current_char() == 't':
                    result += '\t'
                else:
                    result += self.current_char()
                self.advance()
            else:
                result += self.current_char()
                self.advance()
        
        if not self.current_char():
            self.error("Expected closing double quote")
        
        self.advance()  # تخطي علامة الاقتباس الثانية
        return result
    
    def read_number(self) -> float:
        """قراءة الأرقام"""
        result = ""
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            result += self.current_char()
            self.advance()
        
        if '.' in result:
            return float(result)
        return float(result)
    
    def tokenize(self) -> List[Token]:
        """تقسيم النص إلى tokens"""
        while self.pos < len(self.text):
            self.skip_whitespace()
            
            if self.current_char() is None:
                break
            
            line = self.line
            col = self.column
            char = self.current_char()
            
            # الكلمات المحجوزة والمعرّفات
            if char.isalpha():
                word = ""
                while self.current_char() and self.current_char().isalnum():
                    word += self.current_char()
                    self.advance()
                
                if word.upper() == "PUT":
                    self.tokens.append(Token(TokenType.PUT, word, line, col))
                elif word.upper() == "PRINT":
                    self.tokens.append(Token(TokenType.PRINT, word, line, col))
                else:
                    self.error(f"Unknown keyword: {word}")
            
            # المعرّفات والنصوص
            elif char in "'`":
                identifier = self.read_identifier()
                self.tokens.append(Token(TokenType.IDENTIFIER, identifier, line, col))
            
            elif char == '"':
                string = self.read_string()
                self.tokens.append(Token(TokenType.STRING, string, line, col))
            
            # الأرقام
            elif char.isdigit():
                number = self.read_number()
                self.tokens.append(Token(TokenType.NUMBER, number, line, col))
            
            # العمليات الحسابية
            elif char == '&':
                self.tokens.append(Token(TokenType.PLUS, char, line, col))
                self.advance()
            
            elif char == '-':
                self.tokens.append(Token(TokenType.MINUS, char, line, col))
                self.advance()
            
            elif char == '^':
                self.tokens.append(Token(TokenType.MULTIPLY, char, line, col))
                self.advance()
            
            elif char == '\\':
                self.tokens.append(Token(TokenType.DIVIDE, char, line, col))
                self.advance()
            
            # الرموز
            elif char == '=':
                self.tokens.append(Token(TokenType.EQUALS, char, line, col))
                self.advance()
            
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, char, line, col))
                self.advance()
            
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, char, line, col))
                self.advance()
            
            elif char == '(':
                self.tokens.append(Token(TokenType.LPAREN, char, line, col))
                self.advance()
            
            elif char == ')':
                self.tokens.append(Token(TokenType.RPAREN, char, line, col))
                self.advance()
            
            elif char == '[':
                self.tokens.append(Token(TokenType.LBRACKET, char, line, col))
                self.advance()
            
            elif char == ']':
                self.tokens.append(Token(TokenType.RBRACKET, char, line, col))
                self.advance()
            
            else:
                self.error(f"Unknown character: {char}")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
