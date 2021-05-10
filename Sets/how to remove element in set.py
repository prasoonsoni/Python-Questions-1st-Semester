s = {"apple", "orange", "mango","kiwi","cherry"}
s.remove("kiwi")# if item is not there in set it will give error
s.discard("apple")# it will not give any error if item is not present in set
s.pop()# to remove random element
s.clear()# to remove all the elements from the set
del(s)# to remove entire set
print(s)