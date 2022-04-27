
from cgitb import text
import tkinter as tk
from tkinter import ttk#buat widget 

def save_password():
    db = None
    try:
        file = open("password1.txt", "r") #string r untuk melihat file
        db = file.read()
        file.close()
    except:
        pass

    nama_akun = entry.get()
    password = entry2.get()

    file = open("password1.txt" , "w") #string w untuk menulis file write
    file.write(f"{db}{nama_akun} : {password} \n")
    file.close()

def show_password():
    dbtext.delete("1.0","end")
    file = open("password1.txt", "r")
    db = file.read()
    file.close()
    dbtext.insert(tk.END, db)

def hide_password():
    dbtext.delete("1.0" , "end")


window = tk.Tk()
window.geometry("800x500")
window.title("Mini Database")

#buat framae biar rapi kaya div lah modelnya
mainframe = tk.Frame(window)
mainframe.pack(fill=tk.BOTH) #BOTH : MEMENUHI SISI HORIZONTAL DAN VERTIKAL KALAU MAU SISI VERTICAL SAJA ATAU HORIZONTAL SAZA BISA PAKAI tk.X /Y

mlabel = tk.Label(mainframe,text="Password Saver",font=("Helvetica",20,"bold"))
mlabel.pack(side=tk.TOP) #menaruh label di poisisi spesifik

#FRAME 1 --------------------------
frame1 = tk.Frame(mainframe)
frame1.pack(fill=tk.X, pady=5)
label1 = tk.Label(frame1, text="Nama Akun",font=("Helvetica",15,"bold"),width=10)
label1.pack(side=tk.LEFT,padx=5) #MEnambahkan Padding x biar ga mepet kiri

entry = ttk.Entry(frame1, font=("Helvetica",12))
entry.pack(side=tk.LEFT , fill = tk.X, expand=True , padx = 10) #Fill biar dia memenuhi satu baris ke sb X. expand untuk m

#FRAME 2 --------------------------
frame2 = tk.Frame(mainframe,pady=5)
frame2.pack(fill=tk.X)

label2 = tk.Label(frame2, text="Password",font=("Helvetica",15,"bold"),width=10)
label2.pack(side=tk.LEFT,padx=5) #MEnambahkan Padding x biar ga mepet kiri

entry2 = ttk.Entry(frame2, font=("Helvetica",12))
entry2.pack(side=tk.LEFT , fill = tk.X, expand=True , padx = 10) #Fill biar dia memenuhi satu baris ke sb X. expand untuk m

#FRAME 3 --------------------------
frame3= tk.Frame(mainframe,pady=5)
frame3.pack(fill=tk.X)

savebtn = ttk.Button(frame3,text="Save" ,command=save_password)
savebtn.pack(side=tk.RIGHT,padx=10)

hidebtn = ttk.Button(frame3,text="Hide", command=hide_password)
hidebtn.pack(side=tk.RIGHT,padx=10)

showbtn = ttk.Button(frame3,text="Show", command=show_password)
showbtn.pack(side=tk.RIGHT,padx=10)

#FRAME 4 --------------------------
frame4 = tk.Frame(mainframe,pady=5)
frame4.pack(fill=tk.X)

label4 = tk.Label(frame4, text="DATABASE",font=("Helvetica",15,"bold"),width=10)
label4.pack(side=tk.LEFT,padx=5) #MEnambahkan Padding x biar ga mepet kiri

dbtext = tk.Text(frame4, font=("Helvetica",12))
dbtext.pack(side=tk.LEFT , fill = tk.BOTH, expand=True , padx = 10) #Fill biar dia memenuhi satu baris ke sb X. expand untuk m



window.mainloop()