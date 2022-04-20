inputan = input("Masukan nama file : ")
file = open(inputan, "r")
try:
    print(file.read())
except FileNotFoundError:
    print("File Tidak DiTemukan")
