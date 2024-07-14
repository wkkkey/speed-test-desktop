from tkinter import *
from tkinter import ttk
from speedtest_cli import *

def finish():
    app.destroy()
    print("Приложение закрыто")

def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    label_download.config(text="Скорость загрузки:\n" + str(download_speed) + " Мб/c")
    label_upload.config(text="Скорость отдачи:\n" + str(upload_speed) + " Мб/c")

app = Tk()
app.title("Speed Test - Desktop")
app.iconbitmap(r'src\performance.ico')
app.geometry("300x300")
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", finish)


label_title = Label(text="Speed Test", font=("Arial", 20))
label_download = Label(text="Скорость загрузки:\n-", font=("Arial", 10))
label_upload = Label(text="Скорость отдачи:\n-", font=("Arial", 10))
label_ping = Label(text="Пинг:\n-", font=("Arial", 10))
go_btn = Button(text="Старт", font=("Arial", 10), width=30, height=2, command=test)

label_title.pack(side=TOP, pady=15)
label_download.pack(pady= (10, 0))
label_upload.pack()
go_btn.pack(side=BOTTOM, pady=20)

app.mainloop()
