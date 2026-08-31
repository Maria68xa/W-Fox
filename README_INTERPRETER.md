# W-Fox Python Interpreter 🦊

## مرحباً بك في مترجم لغة W-Fox!

هذا المشروع يحتوي على مترجم كامل لغة البرمجة **W-Fox** مكتوب بلغة **Python**.

---

## 📂 هيكل المشروع

```
W-Fox/
├── src/
│   ├── lexer.py          # تحليل لفظي (Tokenization)
│   ├── parser.py         # تحليل بناء الجملة (Parsing)
│   └── interpreter.py    # التنفيذ (Interpretation)
├── examples/
│   ├── example1_simple.wfox       # مثال بسيط
│   ├── example2_arithmetic.wfox   # عمليات حسابية
│   └── example3_complex.wfox      # تعبيرات معقدة
├── tests/
│   ├── test_lexer.py     # اختبارات الـ Lexer
│   └── test_interpreter.py # اختبارات المترجم
└── README_INTERPRETER.md
```

---

## 🔧 كيفية التشغيل

### المتطلبات:
- Python 3.7+

### تشغيل المترجم:

```bash
# من مجلد src
cd src
python interpreter.py
```

### تشغيل برنامج W-Fox مخصص:

```python
from interpreter import run_program

code = """
Put 'price'= 60, print ['price'];
Put 'result' = 10 & 5, print ['result'];
"""

run_program(code)
```

---

## 📖 شرح كل ملف

### 1. **lexer.py** - التحليل اللفظي

**الوظيفة:** تقسيم البرنامج إلى أجزاء صغيرة (Tokens)

**المثال:**
```
الكود: Put 'price'= 60, print ['price'];

الـ Tokens:
- PUT (كلمة محجوزة)
- IDENTIFIER: 'price'
- EQUALS: =
- NUMBER: 60
- COMMA: ,
- PRINT (كلمة محجوزة)
- LBRACKET: [
- IDENTIFIER: 'price'
- RBRACKET: ]
- SEMICOLON: ;
```

### 2. **parser.py** - تحليل بناء الجملة

**الوظيفة:** تحويل الـ Tokens إلى أوامر مفهومة

**المثال:**
```
الـ Tokens → Statements

AssignmentStatement(
    variable='price',
    value=60
)

PrintStatement(
    variable='price'
)
```

### 3. **interpreter.py** - التنفيذ

**الوظيفة:** تنفيذ الأوامر وإظهار النتائج

**المثال:**
```
تخزين المتغيرات:
variables = {
    'price': 60
}

طباعة النتيجة:
✓ تم حفظ price = 60
📤 النتيجة: 60
```

---

## 📝 أمثلة

### مثال 1: متغير بسيط

```wfox
Put 'x'= 42, print ['x'];
```

**الإخراج:**
```
✓ تم حفظ x = 42
📤 النتيجة: 42
```

### مثال 2: عملية حسابية

```wfox
Put 'sum' = 10 & 5, print ['sum'];
```

**الإخراج:**
```
✓ تم حفظ sum = 15
📤 النتيجة: 15
```

### مثال 3: تعبير معقد

```wfox
Put 'result' = 10 & 5 ^ 2 - 20 \ 4, print ['result'];
```

**الحساب:**
```
10 & 5 ^ 2 - 20 \ 4
= 10 + (5 * 2) - (20 / 4)
= 10 + 10 - 5
= 15
```

**الإخراج:**
```
✓ تم حفظ result = 15
📤 النتيجة: 15
```

---

## 🧪 الاختبارات

### تشغيل اختبارات الـ Lexer:

```bash
cd tests
python test_lexer.py
```

### تشغيل اختبارات المترجم:

```bash
cd tests
python test_interpreter.py
```

---

## 🎯 العمليات المدعومة

| العملية | الرمز | المثال | النتيجة |
|--------|------|--------|--------|
| جمع | `&` | `10 & 5` | 15 |
| طرح | `-` | `10 - 5` | 5 |
| ضرب | `^` | `10 ^ 5` | 50 |
| قسمة | `\` | `10 \ 5` | 2 |

---

## 🔄 مراحل التنفيذ

```
الكود البرمجي
    ↓
Lexer (تحليل لفظي)
    ↓
Tokens (رموز)
    ↓
Parser (تحليل نحوي)
    ↓
Statements (أوامر)
    ↓
Interpreter (تنفيذ)
    ↓
النتيجة
```

---

## 🚀 الخطوات التالية

- [ ] إضافة حلقات التكرار (Loops)
- [ ] إضافة الشروط (If/Else)
- [ ] إضافة الدوال (Functions)
- [ ] إضافة المزيد من العمليات المنطقية
- [ ] تحسين معالجة الأخطاء (Error Handling)
- [ ] إنشاء واجهة بيانات (GUI)

---

## 📞 للمزيد من المساعدة

إذا كان لديك أسئلة أو اقتراحات، يرجى فتح مشكلة (Issue) على GitHub.

---

**صُنع بـ ❤️ لـ W-Fox Programming Language**
