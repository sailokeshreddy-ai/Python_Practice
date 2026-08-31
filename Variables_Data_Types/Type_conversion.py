#type_conversion
a = "5"
b = 6.5

print(type(a)) # <class 'str'>
print(type(b)) # <class 'float'>
# print(a + b) # TypeError: can only concatenate str (not "float") to str

c = int(a) + b
print(c) # 11.5

d = 4.5
d = str(d)
print(type(d)) # <class 'str'>
print(d) # "4.5"
