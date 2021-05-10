number_of_books = int(input())
author = {}
date_of_purchase = {}
accession_number = {}
availability_status = {}
for i in range(number_of_books):
    name = input()
    author[name] = input()
    date_of_purchase[name] = input()
    accession_number[name] = int(input())
    availability_status[name] = input()

