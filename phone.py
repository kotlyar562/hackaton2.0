from tkinter import *
import datetime

window = Tk()
window.geometry("400x700")
window.title("HakatonPhone")
window.resizable(False, False)

# функция изменения времени
def checkClock():
    time = datetime.datetime.now()
    if time.second % 2 == 0:
        clockNumbers.config(text=time.strftime("%H:%M"))
    else:
        clockNumbers.config(text=time.strftime("%H %M"))
    window.after(1000, checkClock)

# функция смены на рабочий стол
def switchToDesktop(event):
    showItems()

# функция смены на экрана блокировки
def switchToLockScreen():
    hideItems()
    button1.place_forget()
    button2.place_forget()
    startBackground.pack()
    clockNumbers.place(x=95, y=40)

# функция смены на приложение 'Темы'
def switchToTheme():
    hideItems()

# функция показа всех кнопок приложений
def showItems():
    startBackground.pack()
    clockNumbers.place(x=95, y=40)
    app1.place(x=315, y=550)
    app2.place(x=215, y=550)
    app3.place(x=115, y=550)
    app4.place(x=15, y=550)
    app5.place(x=315, y=450)
    app6.place(x=215, y=450)
    app7.place(x=115, y=450)
    app8.place(x=15, y=450)
    app9.place(x=315, y=350)
    button1.place(x=80, y=655)
    button2.place(x=280, y=655)

# функция прятания всех кнопок и приложений
def hideItems():
    startBackground.pack_forget()
    clockNumbers.place_forget()
    app1.place_forget()
    app2.place_forget()
    app3.place_forget()
    app4.place_forget()
    app5.place_forget()
    app6.place_forget()
    app7.place_forget()
    app8.place_forget()
    app9.place_forget()

# загрузка изображений в программу
background1 = PhotoImage(file="static/backgrounds/background1.png")
background2 = PhotoImage(file="static/backgrounds/background2.png")
background3 = PhotoImage(file="static/backgrounds/background3.png")
themeIcon = PhotoImage(file="static/icons/ThemeIcon.png")

# создание заднего фона
startBackground = Label(image=background1)
startBackground.pack()

# создение часов
clockNumbers = Label(font=('Courier New', 50, 'bold'))
clockNumbers.place(x=95, y=40)

# создание кнопок приложений
app1 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Theme", command=switchToTheme)
app2 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app3 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app4 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app5 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app6 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app7 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app8 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")
app9 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name")

# создание кнопки 'назад на рабочий стол' и 'блокировки'
button1 = Button(text="<", width=3, font=('Arial', 15, 'bold'), command=switchToLockScreen)
button1.place_forget()
button2 = Button(text="O", width=3, font=('Arial', 15, 'bold'), command=showItems)
button2.place_forget()

# биндим функцию на двойной клик
startBackground.bind('<Double-Button-1>', switchToDesktop)

# вызываем функцию изменения времени
checkClock()

window.mainloop()