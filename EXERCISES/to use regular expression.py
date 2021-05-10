""" . match any char
^ match start of string
$ match end of sring
* 0 or more occourances
+ 1 or more occourances
? 0 or 1
[]
^ - negation """

"""import re
re.match()
re.search()"""

import re
x = input()
if re.match("a.b$", x):
    print("matched")
else:
    print("not match")
    
"""import re
x = "The python Programming"
if re.match("The.+Programming", x):
    print("matched")
else:
    print("not matched")"""
    
"""import re
x = "TheProgramming"
if re.match("The.*Programming", x):
    print("matched")
else:
    print("not matched")"""
"""    
import re
x = "The Programming"
if re.match("[A-Z]", x):
    print("matched")
else:
    print("not match")"""
    
import re
x = "the programming"
if re.match("[a-z]", x):
    print("matched")
else:
    print("not match")
    
import re
x = "29"
if re.match("[0-9]", x):
    print("matched")
else:
    print("not match")
    
import re
x = "$"
if re.match("[^A-Za-z0-9]", x):
    print("matched")
else:
    print("not match")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

