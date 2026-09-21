# اختبارات الـ Lexer

import sys
sys.path.insert(0, '../src')

from lexer import Lexer, TokenType

def test_simple_assignment():
    """اختبار تحليل أمر إسناد بسيط"""
    code = "Put 'x'= 10"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    assert tokens[0].type == TokenType.PUT
    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[1].value == "x"
    assert tokens[2].type == TokenType.EQUALS
    assert tokens[3].type == TokenType.NUMBER
    assert tokens[3].value == 10.0
    
    print("✓ اختبار الإسناد البسيط نجح")

def test_arithmetic_operators():
    """اختبار تحليل العمليات الحسابية"""
    code = "10 & 5 - 3 ^ 2 \ 4"
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[1].type == TokenType.PLUS
    assert tokens[3].type == TokenType.MINUS
    assert tokens[5].type == TokenType.MULTIPLY
    assert tokens[7].type == TokenType.DIVIDE
    
    print("✓ اختبار العمليات الحسابية نجح")

def test_string_parsing():
    """اختبار تحليل النصوص"""
    code = 'Put \'msg\' = "Hello", print [\'msg\']'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    string_tokens = [t for t in tokens if t.type == TokenType.STRING]
    assert len(string_tokens) > 0
    assert string_tokens[0].value == "Hello"
    
    print("✓ اختبار النصوص نجح")

if __name__ == "__main__":
    print("\n🧪 اختبارات الـ Lexer\n")
    test_simple_assignment()
    test_arithmetic_operators()
    test_string_parsing()
    print("\n✨ جميع الاختبارات نجحت!\n")
