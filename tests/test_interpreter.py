# اختبارات المترجم

import sys
sys.path.insert(0, '../src')

from interpreter import run_program

def test_simple_variable():
    """اختبار متغير بسيط"""
    code = "Put 'x'= 42, print ['x'];"
    print("\n--- اختبار: متغير بسيط ---")
    run_program(code)

def test_addition():
    """اختبار الجمع"""
    code = "Put 'sum' = 10 & 5, print ['sum'];"
    print("\n--- اختبار: الجمع ---")
    run_program(code)

def test_complex_expression():
    """اختبار تعبير معقد"""
    code = "Put 'result' = 10 & 5 ^ 2 - 20 \ 4, print ['result'];"
    print("\n--- اختبار: تعبير معقد ---")
    run_program(code)

def test_multiple_variables():
    """اختبار متغيرات متعددة"""
    code = """
    Put 'x'= 10, print ['x'];
    Put 'y'= 20, print ['y'];
    Put 'z' = 30, print ['z'];
    """
    print("\n--- اختبار: متغيرات متعددة ---")
    run_program(code)

if __name__ == "__main__":
    print("\n🧪 اختبارات المترجم\n")
    test_simple_variable()
    test_addition()
    test_complex_expression()
    test_multiple_variables()
    print("\n✨ جميع الاختبارات انتهت!\n")
