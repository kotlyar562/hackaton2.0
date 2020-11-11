from tkinter import *
import datetime

window = Tk()
window.geometry("400x700")
window.title("HakatonPhone")
window.resizable(False, False)
window.config(bg="black")
root_calc = None

# функция изменения времени
def checkClock():
    time = datetime.datetime.now()
    if time.second % 2 == 0:
        clockNumbers.config(text=time.strftime("%H:%M"))
    else:
        clockNumbers.config(text=time.strftime("%H %M"))
    window.after(1000, checkClock)

# функция для возврата на рабочий стол
def backToDesktop():
    hideItems()
    showItems()

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

# функция показа следующей темы
def switchToNextTheme():
    global themeToSwitchId

    if themeToSwitchId < len(listOfThemes) - 1:
        themeToSwitchId += 1
        themeToSwitch.config(image=listOfThemes[themeToSwitchId]["preview"])
        themeName.config(text=listOfThemes[themeToSwitchId]["name"])

# функция показа предыдущей темы
def switchToPreviousTheme():
    global themeToSwitchId

    if themeToSwitchId > 0:
        themeToSwitchId -= 1
        themeToSwitch.config(image=listOfThemes[themeToSwitchId]["preview"])
        themeName.config(text=listOfThemes[themeToSwitchId]["name"])

# функция смены на приложение 'Темы'
def switchToTheme():
    hideItems()
    previousThemeButton.place(x=5, y=320)
    nextThemeButton.place(x=350, y=320)
    themeName.place(x=130, y=10)
    themeName.config(text=listOfThemes[themeToSwitchId]["name"], bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    themeToSwitch.place(x=59, y=50)
    themeToSwitch.config(image=listOfThemes[themeToSwitchId]["preview"])

# функция замены текущей темы
def replaceCurrentTheme(event):
    backToDesktop()
    window.config(bg=listOfThemes[themeToSwitchId]["bg"])
    clockNumbers.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    startBackground.config(image=listOfThemes[themeToSwitchId]["image"])
    app1.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app2.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app3.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app4.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app5.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app6.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app7.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app8.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    app9.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    button1.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    button2.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    nextThemeButton.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])
    previousThemeButton.config(bg=listOfThemes[themeToSwitchId]["bg"], fg=listOfThemes[themeToSwitchId]["fg"])

# функция перехода на калькулятор
def switchToCalc():
    hideItems()
    from modules.calc import root_calc
    global root_calc
    root_calc.pack()



# функция показа всех кнопок и приложений
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
    global root_calc
    if root_calc:
        root_calc.pack_forget()
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
    previousThemeButton.place_forget()
    nextThemeButton.place_forget()
    themeToSwitch.place_forget()
    themeName.place_forget()

# создание фонов и иконок
background1 = PhotoImage(file="static/backgrounds/background1.png")
background2 = PhotoImage(file="static/backgrounds/background2.png")
background3 = PhotoImage(file="static/backgrounds/background3.png")
darkTheme = PhotoImage(file="static/themes/darkTheme.png")
lightTheme = PhotoImage(file="static/themes/lightTheme.png")
orangeTheme = PhotoImage(file="static/themes/orangeTheme.png")
themeIcon = PhotoImage(file="static/icons/ThemeIcon.png")

# создание заднего фона
startBackground = Label(image=background1)
startBackground.pack()

# создание часов
clockNumbers = Label(font=('Courier New', 50, 'bold'), bg="black", fg="white")
clockNumbers.place(x=95, y=40)

# создание приложений
app1 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Themes", command=switchToTheme, bg="black", fg="white")
app2 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Calc", command=switchToCalc, bg="black", fg="white")
app3 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")
app4 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")
app5 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")
app6 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")
app7 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")
app8 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")
app9 = Button(width=65, height=65, image=themeIcon, compound=TOP, text="Name", bg="black", fg="white")

# создание кнопки 'назад на рабочий стол' и 'блокировки'
button1 = Button(text="<", width=3, font=('Arial', 15, 'bold'), command=switchToLockScreen, bg="black", fg="white")
button1.place_forget()
button2 = Button(text="O", width=3, font=('Arial', 15, 'bold'), command=backToDesktop, bg="black", fg="white")
button2.place_forget()

# создание элементов для приложения "Темы"
nextThemeButton = Button(text=">", width=3, font=('Arial', 15, 'bold'), command=switchToNextTheme, bg="black", fg="white")
previousThemeButton = Button(text="<", width=3, font=('Arial', 15, 'bold'), command=switchToPreviousTheme, bg="black", fg="white")
themeToSwitch = Label(width=280, height=550)
themeToSwitchId = 0
listOfThemes = [{"name":"Dark Theme", "preview":darkTheme, "image":background1, "bg":"black", "fg":"white"},
                {"name":"Light Theme", "preview":lightTheme, "image":background2, "bg":"white", "fg":"black"},
                {"name":"Orange Theme", "preview":orangeTheme, "image":background3, "bg":"orange", "fg":"black"}]
themeName = Label(font=('Courier New', 15, 'bold'))

# биндим функции
startBackground.bind('<Double-Button-1>', switchToDesktop)
themeToSwitch.bind('<Double-Button-1>', replaceCurrentTheme)

# вызываем функцию изменения времени
checkClock()

window.mainloop()