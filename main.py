import sys
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from GUIAKA import Ui_MainWindow
import logic as logika

class TampilanGUI:
    def __init__(self, ui):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(ui)

        self.ukuran_rute = []
        self.waktu_iteratif = []
        self.waktu_rekursif = []

        self.ui.pushButton.clicked.connect(self.publish)
    
    def publish(self):
        try:
            inputSize = self.ui.inputSize.text()
            n = int(inputSize)

            self.ukuran_rute.append(inputSize)

            jalur, h = logika.generate_jalur_shopee(n)
            print(jalur, h)

            posisi_awal = logika.generate_label(0)
            tujuan = logika.generate_label(n - 1)

            print("iteratif")
            t_iteratif, rute_iteratif = logika.ukur_waktu(logika.cek_resi_iteratif, jalur, h, posisi_awal, tujuan)
            self.waktu_iteratif.append(t_iteratif)

            print("rekursif")
            t_rekursif, rute_rekursif = logika.ukur_waktu(logika.cek_resi_rekursif, jalur, h, posisi_awal, tujuan)
            self.waktu_rekursif.append(t_rekursif)

            self.tabel_waktu()
            self.tabel_jalur(rute_iteratif, rute_rekursif)
            self.tampilkan_grafik()

            self.ui.inputSize.clear()
        except:
            print("ERROR: Input tidak valid")
            return
    
    def tabel_waktu(self):
        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row)

        n = self.ukuran_rute[-1]
        t_iter = self.waktu_iteratif[-1]
        t_rek = self.waktu_rekursif[-1]

        self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(n))
        self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{t_iter:.6f}"))
        self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{t_rek:.6f}"))
    
    def tabel_jalur(self, rute_iteratif, rute_rekursif):
        row = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(row)

        n = self.ukuran_rute[-1]
        iteratif = rute_iteratif
        rekursif = rute_rekursif

        self.ui.tableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(n))
        self.ui.tableWidget_2.setItem(row, 1, QtWidgets.QTableWidgetItem(f"{iteratif}"))
        self.ui.tableWidget_2.setItem(row, 2, QtWidgets.QTableWidgetItem(f"{rekursif}"))

    
    def tampilkan_grafik(self):
        plt.figure(1, figsize=(10, 6))
        plt.clf()
        plt.plot(self.ukuran_rute, self.waktu_iteratif, marker='o', label="Iterative")
        plt.plot(self.ukuran_rute, self.waktu_rekursif, marker='o', label="Recursive")

        plt.title("Perbandingan Iterative vs Recursive")
        plt.xlabel("Input Size (n)")
        plt.ylabel("waktu eksekusi (seconds)")
        plt.grid(True)
        plt.legend()
        plt.show()
        plt.pause(0.1)


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    gui = TampilanGUI(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()