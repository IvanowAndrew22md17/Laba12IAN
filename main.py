import tkinter as tk

x = int(input("введите номер задания:"))

#12.1
def f1():
    class Restaurant:
        def __init__(self, name, k_type):
            self.name = name
            self.k_type = k_type
        def describe_restaurant(self):
            print(f"Название ресторана:{self.name} тип кухни:{self.k_type}")
    class IceCreamStand(Restaurant):
        def __init__(self, name, k_type, flavors):
            super().__init__(name, k_type)
            self.flavors = flavors
        def sh_flavors(self):
            print("У нас есть такие вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)
    new_ice_cream_stand = IceCreamStand("Baskin-Robbins", "Ice Cream", ["ванильный", "шоколадный", "фисташковое"])
    new_ice_cream_stand.describe_restaurant()
    new_ice_cream_stand.sh_flavors()
if x == 1:
    f1()

# 12.2
def f2():
    class IceCreamStand:
        def __init__(self, name, flavors, location, w_hours, type):
            self.name = name
            self.flavors = flavors
            self.location = location
            self.w_hours = w_hours
            self.type = type
        def show_flavors(self):
            print("Список вкусов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f'Вкус {flavor} добавлен в список')
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f'Вкус {flavor} удален из списка')
            else:
                print(f'Вкус {flavor} не найден в списке')
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f'Вкус {flavor} есть в списке')
            else:
                print(f'Вкус {flavor} нет в списке')
        def describe_stand(self):
            print(f"Стенд мороженного {self.name}")
            print(f"Адрес: {self.location}")
            print(f"Часы работы: {self.w_hours}")
        def show_Types(self):
            print("Список доступных типов мороженого:")
            for types in self.type:
                print("- " + types)
    new_stand = IceCreamStand("Carvel", ['ванильное', 'шоколадное', 'фисташковое'], 'Благодатная улица 30','12.00 - 23:00', ['на палочке', 'стакан', 'рожок'])
    new_stand.describe_stand()
    new_stand.show_flavors()
    new_stand.show_Types()
    new_stand.add_flavor("клубничное")
    new_stand.check_flavor("фисташковое")
    new_stand.check_flavor("клубничное")
    new_stand.remove_flavor("фисташковое")
    new_stand.check_flavor("фисташковое")
    new_stand.check_flavor("шоколадное")
if x==2:
    f2() 

#12.3
def f3():
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def g_menu(self):
            menu = "Добро пожаловать в " + self.name + "\n"
            menu += "У нас есть такие вкусы мороженого:\n"
            for flavor in self.flavors:
                menu += "- " + flavor + "\n"
            return menu
    my_stand = IceCreamStand("Kona ice", ['ванильное', 'шоколадное', 'фисташковое'])
    root = tk.Tk()
    root['bg'] = 'blue3'
    root.title("IceCreamStand")
    root.geometry('300x250')
    menu_label = tk.Label(root, text=my_stand.g_menu(), bg='pink')
    menu_label.pack()
    root.mainloop()
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")