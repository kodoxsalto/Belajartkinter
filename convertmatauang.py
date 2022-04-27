import tkinter as tk
#Membuat fungsi
def usdtoid():
    angka = textbox.get()
    dollar = float(angka)*144005.5
    text.set("RP. "+ str(dollar))
    label2.config(font=("Helvetica",12,"bold"),fg="green")


#wajib ada adalah window
window = tk.Tk()

#ganti judul
window.title("USD TO RUPIAH CONVERTER")
#Ganti ukuran window panjang x tinggi
window.geometry("800x300")

#Membuat Widget
#Membuat label dan meletakkan pada window window
label1 = tk.Label(window, text="USD",font=("Helvetica",12,"bold"))
#untuk memunculkan label yang dibuat
label1.pack()
#Membuat teks box
textbox = tk.Entry(window,font=("Helvetica",15,"bold"),width=5,justify=tk.CENTER)
textbox.pack()
#Membuat tombol
btn = tk.Button(window,text="TO ", command=usdtoid)
btn.pack()

text=tk.StringVar()
text.set("IDR")

label2 = tk.Label(window,font=("Helvetica",12,"bold"), textvariable=text)
label2.pack()

#perlu di looping setiap saat agar muncul di window
window.mainloop()