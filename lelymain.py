#edit GitHub
import tkinter as tk
import random

# Angka rahasia
angka_rahasia = random.randint(1, 100)

# Fungsi untuk mengecek tebakan
def cek_tebakan():
    try:
        tebakan = int(entry.get())
        if tebakan < angka_rahasia:
            hasil_label.config(text="Terlalu kecil!")
        elif tebakan > angka_rahasia:
            hasil_label.config(text="Terlalu besar!")
        else:
            hasil_label.config(text="Selamat! Tebakanmu benar!")
    except ValueError:
        hasil_label.config(text="Masukkan angka yang valid!")

# Buat window utama
window = tk.Tk()
window.title("Permainan Tebak Angka")

# Label instruksi
instruksi = tk.Label(window, text="Tebak angka antara 1 dan 100:")
instruksi.pack()

# Entry untuk input
entry = tk.Entry(window)
entry.pack()

# Tombol cek
cek_button = tk.Button(window, text="Cek Tebakan", command=cek_tebakan)
cek_button.pack()

# Label hasil
hasil_label = tk.Label(window, text="")
hasil_label.pack()

# Jalankan aplikasi
window.mainloop()
