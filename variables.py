# ceci est un commentaire

# foo
# bar 
# bazz
from re import A


nombre = 123
print(nombre)
print(type(nombre))

nombre = 3.14
print(nombre)

nombre = "123"
print(nombre)

text = "du texte"
print(text)

is_day = True
print(is_day)

has_sugar = False
print(has_sugar)
print(type(has_sugar))

has_accepted_ula = None
print(has_accepted_ula)
print(type(has_accepted_ula))

html_code = '<h1>titre de mon blog</h1>'
print(html_code)
nickname = "John \"Dead\" Doe"
print(nickname)
print(type(nickname))

multiline_text = "foo\n baz\n bar "
print(multiline_text)

multiline_text = """foo
'baz'
bar"""
print(multiline_text)

nombre6 = 3.14
print(type(nombre6))



nombre = '5'
print(type(nombre))
nombre = int(nombre)
print(type(nombre))

nombre = '5'
print(type(nombre))
nombre = float(nombre)
print(type(nombre))

nombre = 3.14
print(nombre)
print(type(nombre))
nombre = int(nombre)
print(nombre)

nombre = str(nombre)
print(type(nombre))

my_var = 0
my_var = bool(my_var)
print(my_var)

my_var = 0
my_var = bool(my_var)
print(my_var)
my_var = [132 , 'abc', False]
my_var = bool(my_var)
print(my_var)

my_var = 0
my_var = bool(my_var)
print(my_var)
my_var = [132 , 'abc', False]
my_var = bool(my_var)
print(my_var)

# swap

a = 42
b = 123

#  a == 123 et b == 42

# a = b
# b = a/3 + 1
# print(b)

# classique
# c = a
# a = b
# b = c

# destructured assignement

# a, b = b, a


a = a + b
b = a - b
a = a - b

print(a)

# arrondi

import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(Decimal("0.5").quantize(Decimal("1"))) 
print(Decimal("1.5").quantize(Decimal("1"))) 
