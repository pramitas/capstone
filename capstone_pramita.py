# NAMA : PRAMITA SEPTIYANI
# CAPSTONE MODUL 1

# Inisialisasi data siswa dalam bentuk data collection List
data_siswa = []

# Fungsi untuk menambahkan data siswa (CREATE)
def tambah_siswa(id, nama, kelas, mapel, nilai):
    # Cek apakah id siswa sudah ada dalam dict data siswa
    for data in data_siswa:
        if data['id'] == id.upper():
            print(f"ID siswa {id} sudah ada. Data tidak ditambahkan.")
            return
    
    # Jika id siswa belum ada, tambahkan ke dict data siswa
    siswa = {'id': id.upper(), 'nama': nama.upper(), 'kelas' : kelas.upper(), 'mapel': mapel.upper() , 'nilai': nilai}
    data_siswa.append(siswa)
    print(f"Data siswa {nama} berhasil ditambahkan.")

# Fungsi untuk menampilkan semua data siswa
def tampilkan_siswa_all():
    if not data_siswa:
        print("\nTidak ada data siswa.")
    else:
        idx=1
        for siswa in data_siswa:
            print(f"{idx}. ID: {siswa['id']} | Nama: {siswa['nama']} | Kelas: {siswa['kelas']} | Mapel: {siswa['mapel']} | Nilai: {siswa['nilai']}")
            idx += 1

# Fungsi untuk menampilkan data siswa berdasarkan ID / Nama
def tampilkan_siswa_byidnama(data):
    data = data.upper()
    for siswa in data_siswa:
        if siswa['id'] == data or siswa['nama'] == data:
            print(f"ID: {siswa['id']} | Nama: {siswa['nama']} | Kelas: {siswa['kelas']} | Mapel: {siswa['mapel']} | Nilai: {siswa['nilai']}")
            return
    print(f"Siswa dengan data : {data} tidak ditemukan.")

# Fungsi untuk memperbarui data siswa
def perbarui_siswa(data, nilai_baru):
    data = data.upper()
    for siswa in data_siswa:
        if siswa['id'] == data or siswa['nama'] == data:
            siswa['nilai'] = nilai_baru
            print(f"Nilai ID Siswa : {siswa['id']} dengan nama : {siswa['nama']} berhasil diperbarui.")
            return
    print(f"Siswa dengan data : {data} tidak ditemukan.")

# Fungsi untuk menghapus data siswa
def hapus_siswa(data):
    data = data.upper()
    for siswa in data_siswa:
        if siswa['nama'] == data or siswa['id'] == data:
            data_siswa.remove(siswa)
            print(f"Siswa dengan id : {siswa['id']} atau nama : {siswa['nama']} berhasil dihapus.")
            return
    print(f"Siswa dengan data : {data} tidak ditemukan.")

# Main program untuk CRUD
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah siswa")
        print("2. Tampilkan Semua Data siswa")
        print("3. Tampilkan Data siswa Berdasarkan ID / Nama")
        print("4. Perbarui nilai siswa")
        print("5. Hapus siswa")
        print("6. Keluar")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            id = input("Masukkan ID / Nomor Induk Siswa: ")
            nama = input("Masukkan  Nama siswa: ")
            kelas = input("Masukkan Kelas siswa: ")
            mapel = input("Masukkan Mata Pelajaran: ")
            try : 
                nilai = float(input("Masukkan nilai siswa: "))
                tambah_siswa(id, nama, kelas, mapel, nilai)
            except:
                print("nilai harus berupa angka!")
        elif pilihan == '2':
            tampilkan_siswa_all()
        elif pilihan == '3':
            data = str(input("Masukkan ID / Nama Siswa: "))
            tampilkan_siswa_byidnama(data)
        elif pilihan == '4':
            data = input("Masukkan ID / Nama siswa yang ingin diperbarui: ")
            try:
                nilai_baru = float(input("Masukkan nilai baru: "))
                perbarui_siswa(data, nilai_baru)
            except:
                print("nilai harus berupa angka!")
        elif pilihan == '5':
            data = input("Masukkan ID / Nama siswa yang ingin dihapus: ")
            hapus_siswa(data)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program utama
main()