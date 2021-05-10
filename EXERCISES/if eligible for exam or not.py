"""A student will not be allowed to sit in exam if his/her attendence is less
 than 75%.
Take following input from user
1.Number of classes held
2.Number of classes attended.
3.And print
      (i)percentage of class attended
      (ii)Is student is allowed to sit in exam or not."""


held = int(input("NO OF CLASSES HELD = "))
attend = int(input("NO OF CLASSES ATTENDED = "))
percentage = (attend / held) * 100

if percentage > 75:
    print(" You are eligible for exam ")
else:
    print(" Sorry!! You are not eligible for exam ")

