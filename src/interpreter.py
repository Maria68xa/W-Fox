# W-Fox Interpreter
# هذا الملف ينفذ الأوامر

from typing import Dict, Any
from parser import (
    Parser, AssignmentStatement, PrintStatement, Expression
)
from lexer import Lexer, TokenType

class Interpreter:
    def __init__(self):
        self.variables: Dict[str, Any] = {}  # ذاكرة المتغيرات
    
    def evaluate_expression(self, expr: Any) -> Any:
        """تقييم التعبير الحسابي"""
        
        # إذا كان رقماً مباشراً
        if isinstance(expr, (int, float)):
            return expr
        
        # إذا كان نصاً
        if isinstance(expr, str) and not isinstance(expr, tuple):
            return expr
        
        # إذا كان متغيراً
        if isinstance(expr, tuple) and expr[0] == "VAR":
            var_name = expr[1]
            if var_name not in self.variables:
                raise Exception(f"Variable '{var_name}' is not defined")
            return self.variables[var_name]
        
        # إذا كان تعبيراً معقداً
        if isinstance(expr, Expression):
            left = self.evaluate_expression(expr.left)
            right = self.evaluate_expression(expr.right)
            
            if expr.operator == '&':  # جمع
                return left + right
            elif expr.operator == '-':  # طرح
                return left - right
            elif expr.operator == '^':  # ضرب
                return left * right
            elif expr.operator == '\\':  # قسمة
                if right == 0:
                    raise Exception("Division by zero")
                return left / right
            else:
                raise Exception(f"Unknown operator: {expr.operator}")
        
        raise Exception(f"Cannot evaluate expression: {expr}")
    
    def execute_assignment(self, stmt: AssignmentStatement):
        """تنفيذ أمر الإسناد"""
        value = self.evaluate_expression(stmt.value)
        self.variables[stmt.variable] = value
        print(f"✓ تم حفظ {stmt.variable} = {value}")
    
    def execute_print(self, stmt: PrintStatement):
        """تنفيذ أمر الطباعة"""
        if stmt.variable not in self.variables:
            raise Exception(f"Variable '{stmt.variable}' is not defined")
        
        value = self.variables[stmt.variable]
        print(f"📤 النتيجة: {value}")
    
    def run(self, statements):
        """تنفيذ البرنامج"""
        for stmt in statements:
            if isinstance(stmt, AssignmentStatement):
                self.execute_assignment(stmt)
            elif isinstance(stmt, PrintStatement):
                self.execute_print(stmt)
            else:
                raise Exception(f"Unknown statement type: {type(stmt)}")

def run_program(code: str):
    """تشغيل برنامج W-Fox"""
    print("\n" + "="*50)
    print("🦊 W-Fox Interpreter")
    print("="*50 + "\n")
    
    try:
        # المرحلة 1: Lexical Analysis (تحليل لفظي)
        print("📝 المرحلة 1: تحليل لفظي (Tokenization)...")
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        print(f"✓ تم العثور على {len(tokens)-1} tokens")
        for token in tokens[:-1]:
            print(f"  - {token.type.value}: {token.value}")
        
        # المرحلة 2: Syntax Analysis (تحليل بناء الجملة)
        print("\n🔍 المرحلة 2: تحليل بناء الجملة (Parsing)...")
        parser = Parser(tokens)
        statements = parser.parse()
        print(f"✓ تم تحليل {len(statements)} أوامر")
        
        # المرحلة 3: Interpretation (التنفيذ)
        print("\n⚙️ المرحلة 3: التنفيذ (Interpretation)...\n")
        interpreter = Interpreter()
        interpreter.run(statements)
        
        print("\n" + "="*50)
        print("✨ انتهى التنفيذ بنجاح!")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ خطأ: {e}\n")

if __name__ == "__main__":
    # مثال: برنامج بسيط
    code = """
    Put 'price'= 60, print ['price'];
    Put 'result' = 10 & 5, print ['result'];
    Put 'total' = 100 - 30 ^ 2, print ['total'];
    """
    
    run_program(code)
