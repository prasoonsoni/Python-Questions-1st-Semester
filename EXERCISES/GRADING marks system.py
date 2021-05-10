"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""

marks = float(input("Enter Your Marks : "))
if marks>100:
    print("enter your marks correctly!!")
else:
    if marks<25:
        print("F")
    else:
            if 25<marks<45:
                print("E")
            else:
                    if 45<marks<50:
                        print("D")
                    else:
                            if 50<marks<60:
                                print("C")
                            else:
                                    if 60<marks<80:
                                        print("B")
                                    else:
                                        if marks>80:
                                                print("A")