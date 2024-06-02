def kena_razia(date, data):
    locations = ["Gajah Mada", "Hayam Wuruk", "Sisingamangaraja", "Panglima Polim", "Fatmawati", "Tomang Raya"]
    result = []

    for kendaraan in data:
        if kendaraan['type'] == 'Mobil':
            tilang = 0
            for rute in kendaraan['rute']:
                if check_location(rute, locations):
                    last_digit = get_last_digit(kendaraan['plat'])
                    if check_odd_even(date, last_digit):
                        tilang += 1
            if tilang > 0:
                result.append({'name': kendaraan['name'], 'tilang': tilang})

    return result

def check_location(rute, locations):
    for loc in locations:
        if compare_strings(rute, loc):
            return True
    return False

def get_last_digit(plat):
    last_char = ''
    i = len(plat) - 1
    while plat[i].isdigit():
        last_char = plat[i] + last_char
        i -= 1
    return int(last_char)

def check_odd_even(date, last_digit):
    if date % 2 == 0:
        return last_digit % 2 != 0
    else:
        return last_digit % 2 == 0

def compare_strings(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

# Meminta input dari pengguna untuk tanggal
tanggal = int(input("Masukkan tanggal (1-31): "))

# Meminta input dari pengguna untuk data kendaraan
data_kendaraan = []
jumlah_kendaraan = int(input("Masukkan jumlah kendaraan: "))

for i in range(jumlah_kendaraan):
    name = input("Masukkan nama kendaraan: ")
    plat = input("Masukkan nomor plat kendaraan: ")
    tipe = input("Masukkan tipe kendaraan (Mobil/Motor): ")
    rute = input("Masukkan rute kendaraan (pisahkan dengan koma): ")
    data_kendaraan.append({'name': name, 'plat': plat, 'type': tipe, 'rute': rute})

# Memanggil fungsi kena_razia dan menampilkan hasilnya
hasil_razia = kena_razia(tanggal, data_kendaraan)
if len(hasil_razia) > 0:
    print("Hasil razia:")
    for hasil in hasil_razia:
        print(f"{hasil['name']} mendapat tilang sebanyak {hasil['tilang']}")
else:
    print("Tidak ada pelanggaran razia pada tanggal tersebut.")
