# импортировали библиотеку tkinter и ее модули
from tkinter import ttk
from tkinter import Tk
from tkinter.messagebox import showerror

# создание окна приложения
window=Tk() # связывание переменной с объектом
window.title("Сумма чисел") # название окна
window.geometry("300x100") # размер окна

# Создали указания пользователю
lbl=ttk.Label(window, text="Введите первое слагаемое:") # Указание пользователю о вводе первого слагаемого
lbl.grid(column=0, row=0) # Размещение указания
lbl2=ttk.Label(window, text="Введите второе слагаемое:") # Указание пользователю о вводе второго слагаемого
lbl2.grid(column=0, row=1) # размещение второго указания
