"""import re
num = input()
if re.match("([1-9][0-9][A-Za-z][A-Za-z][A-Za-z][0-9][0-9][0-9][0-9]$)", num):
    print("valid")
else:
    print("not valid")
    """
    
#shortcut

import re
num = input()
if re.match("([1-9][0-9][A-Za-z]{3}[0-9]{4}$)", num):
    print("valid")
else:
    print("not valid")