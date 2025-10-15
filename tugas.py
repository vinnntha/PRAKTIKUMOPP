nilai = int(input("Masukkan nilai Anda: "))

if nilai >= 95:
        print("A")
elif nilai >= 80:
        print("B")
elif nilai >= 70:
        print("C")
elif nilai == 60:
        print("D")
else:
        print("E")

print(input("Mau isi nilai lain? y/n: "))