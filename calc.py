# импортирование библиотеку tkinter и ее модули
from tkinter import ttk
from tkinter import Tk
from tkinter.messagebox import showerror

# создание окна приложения
window=Tk() # связывание переменной с объектом
window.title("Сумма чисел") # название окна
window.geometry("300x100") # размер окна
window.configure(bg="#e6e6fa") # цвет окна

# Функция расчета
def raschet(): # создаем функцию
    # прверка правильности введенных значений
    try:
        chislo1=float(ent.get()) # считывание первого слагаемого из первого поля ввода
        chislo2=float(ent2.get()) # считывание второго слагаемого из второго поля ввода
    except ValueError: # указываем, какой вид ошибки обрабатывается
        showerror("ОШИБКА!", "Введите число!") # сообщение об ошибке и указание о том, как ее исправить
        return [None] # выход из функции
    
    summa=chislo1+chislo2 # формула расчета суммы
    
    lblvivod=ttk.Label(window, text=f"Сумма равна: {summa}") # поле вывода результата
    lblvivod.grid(column=1, row=3) # размещение поля вывода

# Создание указания пользователю
lbl=ttk.Label(window, text="Введите первое слагаемое:") # Указание пользователю о вводе первого слагаемого
lbl.grid(column=0, row=0) # Размещение указания
lbl2=ttk.Label(window, text="Введите второе слагаемое:") # Указание пользователю о вводе второго слагаемого
lbl2.grid(column=0, row=1) # размещение второго указания

# Добавление поля ввода значений
ent=ttk.Entry(window) # создание поля ввода для первого слагаемого
ent.grid(column=1, row=0) # размещение поля ввода
ent2=ttk.Entry(window) # создание поля ввода для второго слагаемого
ent2.grid(column=1, row=1) # размещение второго поля ввода

# Создание кнопки расчета
btn=ttk.Button(window, text="Расчитать сумму чисел") # кнопка расчета
btn.grid(column=1, row=2) # расположение кнопки в окне

window.mainloop() # бесконечный цикл для окна приложения
