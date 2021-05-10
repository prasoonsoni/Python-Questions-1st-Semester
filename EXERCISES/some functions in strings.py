a = "PRASOON"
b = a.lower()
print(b)

a = "prasoon"
b = a.upper()
print(b)

a = "prasoon"
b = a.title()
print(b)

a ="apple"
b = a.find("p")
print(b)

a = "prasoon"
b = a.isalpha()
print(b)

a = "prasoon"
b = a.startswith("pr")
print(b)

a = "prasoon"
b = a.endswith("oon")
print(b)

a = "          prasoon            "
b = a.strip() ## to remove space from end and beginning
print(b)
print(a)

a = "            prasoon                "
b = a.rstrip()###to remove white space from end
print(b)

a = "             prasoon            "
b = a.lstrip()## to remove whitee space from beggining
print(b)

 
a = "computer"
print(a[0])
print(a[1])


"""slicing-->"""
a = "computer"
print(a[0:3]) ##to extract sub string from a string#

"""extended slicing"""

a = "computer"
print(a[0:8:2]) ### [i:j:k] k-1 items are skipped

# to reverse a string

a = "prasoon"
print(a[::-1])


































