from logging import exception


file = open("mynumber.txt", "r")

bil1 = int(file.readline())
bil2 = int(file.readline())

hasil = bil1/bil2
try:
    print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)
except ZeroDivisionError:
    print("Number salah")
