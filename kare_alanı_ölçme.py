import tkinter as tk
from tkinter import messagebox

# Hesaplama fonksiyonu
def alan_hesapla():
    try:
        kenar = float(kenar_girdisi.get())
        if kenar <= 0:
            messagebox.showerror("Hata", "Kenar uzunluğu pozitif bir sayı olmalı!")
        else:
            alan = kenar ** 2
            sonuc_label.config(text=f"Alan: {alan} cm²")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı gir!")

# Pencere oluşturma
pencere = tk.Tk()
pencere.title("Kare Alan Hesaplayıcı")
pencere.geometry("300x200")

# Başlık
baslik = tk.Label(pencere, text="🔲 Kare Alan Hesaplama", font=("Arial", 14))
baslik.pack(pady=10)

# Girdi
kenar_girdisi = tk.Entry(pencere, font=("Arial", 12))
kenar_girdisi.pack(pady=5)

# Buton
hesapla_butonu = tk.Button(pencere, text="Hesapla", command=alan_hesapla, font=("Arial", 12))
hesapla_butonu.pack(pady=5)

# Sonuç
sonuc_label = tk.Label(pencere, text="", font=("Arial", 12))
sonuc_label.pack(pady=5)

# Arayüzü çalıştır
pencere.mainloop()