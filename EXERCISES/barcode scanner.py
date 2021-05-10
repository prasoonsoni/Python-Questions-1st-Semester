barcode_number = input()
last_digit = int(barcode_number[-1])
if len(barcode_number) !=12:
    print("Cannot be Proceed")
else:
    list_of_numbers = []
    for i in range(12):
        list_of_numbers.append(int(barcode_number[i]))
    odd_posi = []
    even_posi = []
    for i in range(0,12,2):
        odd_posi.append(list_of_numbers[i])
    for i in range (1,11,2):
        even_posi.append(list_of_numbers[i])
    odd_sum = sum(odd_posi)*3
    even_sum = sum(even_posi)
    dig_sum = str(odd_sum + even_sum)
    diglist = []
    for i in dig_sum:
        diglist.append(int(i))
    if diglist[-1]==0:
        check_digit = 0
    else:
        check_digit = 10 - diglist[-1]
    if last_digit==check_digit:
        print("Validated")
    else:
        print("Error in barcode")

