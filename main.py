import json

nilai_json = []

with open("nilai_mahasiswa.json", "r") as file:
    nilai_json = json.load(file) 

def tampilkan_data():
    if len(nilai_json) == 0:
        print("belum ada data nilai")
    else:
        print("ini data nilai mahasiswa: ")
        for i in nilai_json:
            print(i["nama"], i["nim"], i["nilai"])


def tambah_data():
    nama_mahasiswa = input("masukan nama mahasiswa: ")
    nim_mahasiswa = input("masukan nim mahasiswa: ")
    nilai_mahasiswa = int(input("masukan nilai mahasiswa: "))

    nilai_json.append({
        "nama" : nama_mahasiswa,
        "nim" : nim_mahasiswa,
        "nilai" : nilai_mahasiswa
    })

    with open("nilai_mahasiswa.json", "w") as file:
        json.dump(nilai_json, file, indent = 4)
        print("DATA MAHASISWA TELAH DI TAMBAHKAN")


while True:
    print("PILIH ANGKA 1-3. ANGKA 1 UNTUK LIHAT DATA, ANGKA 2 UNTUK MENAMBAH DATA, DAN ANGKA 3 UNTUK KELUAR")
    pilih_input = input("pilihan angka: ")

    if pilih_input == "1":
        tampilkan_data()
    if pilih_input == "2":
        tambah_data()
    if pilih_input == "3":
        print("anda telah keluar")
        break