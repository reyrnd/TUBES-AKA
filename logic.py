import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(1100)

def generate_label(n):
    label = ""
    while n >= 0:
        label = chr(n % 26 + 65) + label
        n = n // 26 - 1
    return label

def generate_jalur_shopee(n):
    jalur_pengiriman = {}
    estimasi_sisa_jarak = {}

    for i in range(n):
        label_sekarang = generate_label(i)
        
        if i < n - 1:
            label_berikutnya = generate_label(i + 1)
            jalur_pengiriman[label_sekarang] = [label_berikutnya]
        else:
            jalur_pengiriman[label_sekarang] = []

        estimasi_sisa_jarak[label_sekarang] = (n - 1) - i

    return jalur_pengiriman, estimasi_sisa_jarak

def cek_resi_iteratif(jalur, h, posisi_awal, tujuan):
    titik_dilalui = []
    posisi_sekarang = posisi_awal

    while True:
        titik_dilalui.append(posisi_sekarang)

        if posisi_sekarang == tujuan:
            return titik_dilalui

        titik_transit = jalur[posisi_sekarang]
        titik_next = titik_transit[0]

        if h[titik_next] < h[posisi_sekarang]:
            posisi_sekarang = titik_next

def cek_resi_rekursif(jalur, h, posisi, tujuan, jalur_dilalui=None):
    if jalur_dilalui is None:
        jalur_dilalui = [posisi]

    if posisi == tujuan:
        return jalur_dilalui

    if posisi not in jalur or len(jalur[posisi]) == 0:
        return None

    titik_next = jalur[posisi][0]

    if h[titik_next] < h[posisi]:
        return cek_resi_rekursif(jalur, h, titik_next, tujuan, jalur_dilalui + [titik_next])

    return None

def ukur_waktu(fungsi, jalur, h, posisi_awal, tujuan):
    awal = time.time()
    print(awal)
    func = fungsi(jalur, h, posisi_awal, tujuan)
    print(func)
    akhir = time.time()
    print(akhir)
    waktu = akhir-awal
    return waktu, func

# def main():

#     ukuran_rute = [50, 100, 200, 400, 600, 800, 1000]
#     waktu_iteratif = []
#     waktu_rekursif = []

#     for n in ukuran_rute:
#         jalur, h = generate_jalur_shopee(n)
#         print(jalur, h)

#         posisi_awal = generate_label(0)
#         tujuan = generate_label(n - 1)


#         print("iteratif")
#         t_iteratif = ukur_waktu(cek_resi_iteratif, jalur, h, posisi_awal, tujuan)
#         waktu_iteratif.append(t_iteratif)

#         print("rekursif")
#         t_rekursif = ukur_waktu(cek_resi_rekursif, jalur, h, posisi_awal, tujuan)
#         waktu_rekursif.append(t_rekursif)
    
#     plt.figure(figsize=(10, 6))
#     plt.plot(ukuran_rute, waktu_iteratif, marker='o', label="Iterative")
#     plt.plot(ukuran_rute, waktu_rekursif, marker='o', label="Recursive")

#     plt.title("Perbandingan Iterative vs Recursive")
#     plt.xlabel("Input Size (n)")
#     plt.ylabel("waktu eksekusi (seconds)")
#     plt.grid(True)
#     plt.legend()
#     plt.show()


# if __name__ == "__main__":
#     main()