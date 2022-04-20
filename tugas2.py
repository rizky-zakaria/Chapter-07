nama_file = str(input("Masukkan path lokasi dan nama file : "))

try:
    open(nama_file, "r")

except:
    print("lokasi file tidak tersedia / file tidak ditemukan !")

else:
    while True:
        data = str(input("Data yang mau ditambahkan : "))
        file = open(nama_file, "a")
        file.write("\n"+data)
        file.close()

        cont = input("Mau menambahkan lagi (y/n) : ")
        while cont.lower() not in ("y", "n"):
            cont = input("masukan anda salah, masukan hanya n atau y : ")
        if cont == "n":
            break
