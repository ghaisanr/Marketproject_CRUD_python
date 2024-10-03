harga_apel=10000
harga_jeruk=15000
harga_anggur=20000

jumlah_apel=int(input("masukkan jumlah apel="))
jumlah_jeruk=int(input("masukkan jumlah jeruk="))
jumlah_anggur=int(input("masukkan jumlah anggur="))

total_apel=harga_apel*jumlah_apel
total_jeruk=harga_jeruk*jumlah_jeruk
total_anggur=harga_anggur*jumlah_anggur
total=total_apel+total_jeruk+total_anggur

print("===detail Belanja===")
print("apel: ",jumlah_apel," x ",harga_apel," = ",total_apel)
print("jeruk: ",jumlah_jeruk," x ",harga_jeruk," = ",total_jeruk)
print("anggur: ",jumlah_anggur," x ",harga_anggur," = ",total_anggur)

print("total belanja: ",total)
