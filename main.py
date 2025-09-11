umur = 17                 
tinggi_badan = 170.5    
nama = "Averill"          
makanan_kesukaan = ["Sushi", "Pizza", "Ice Cream"]  

print("=== 1. Variabel dan Tipe Data ===")
print("Tipe data umur:", type(umur))
print("Tipe data tinggi_badan:", type(tinggi_badan))
print("Tipe data nama:", type(nama))
print("Tipe data makanan_kesukaan:", type(makanan_kesukaan))



belanja = ["beras", "minyak", "telur"]
belanja.append("gula")
belanja.append("kopi")

print("\n=== 2. List dan Manipulasi ===")
print("Daftar belanja:")
for item in belanja:
    print("-", item)



harga_belanjaan = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}

print("\n=== 3. Dictionary ===")
total = sum(harga_belanjaan.values())
print("Total harga belanjaan:", total)



def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

print("\n=== 4. Fungsi ===")
luas, keliling = persegi_panjang(10, 5)
print("Luas persegi panjang:", luas)
print("Keliling persegi panjang:", keliling)


print("\n=== 5. Percabangan ===")
usia = int(input("Masukkan usia Anda: "))

if 0 <= usia <= 13:
    print("Anak")
elif 14 <= usia <= 24:
    print("Remaja")
elif 25 <= usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")
