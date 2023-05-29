import tkinter as tk

x = int(input("введите номер задания:"))

#12.1
def f1():
    class Restaurant:
        def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"{self.name} is a {self.cuisine_type} restaurant.")
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine_type, flavors):
            super().__init__(name, cuisine_type)
            self.flavors = flavors
        def display_flavors(self):
            print("У нас есть следующие вкусы мороженого:")
            for flavor in self.flavors:
                print(flavor)
    my_ice_cream_stand = IceCreamStand("Scoops", "Ice Cream Cafe", ["ванильный", "шоколадный", "клубничный"])
    my_ice_cream_stand.describe_restaurant()
    my_ice_cream_stand.display_flavors()
if x == 1:
    f1()

# 12.2
def f2():
    class IceCreamStand:
        def __init__(self, name, flavors, location, working_hours, type_flavors):
            self.name = name
            self.flavors = flavors
            self.location = location
            self.working_hours = working_hours
            self.type_flavors = type_flavors
        def show_flavors(self):
            print("Список доступных сортов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f'Сорт {flavor} добавлен в список')
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f'Сорт {flavor} удален из списка')
            else:
                print(f'Сорт {flavor} не найден в списке')
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f'Сорт {flavor} есть в списке')
            else:
                print(f'Сорта {flavor} нет в списке')
        def describe_stand(self):
            print(f"Стенд мороженного {self.name}")
            print(f"Место: {self.location}")
            print(f"Время работы: {self.working_hours}")
        def show_Typesflavors(self):
            print("Список доступных типов мороженого:")
            for types in self.type_flavors:
                print("- " + types)
    my_stand = IceCreamStand("Кафе-мороженное", ['ванильное', 'шоколадное', 'клубничное'], 'Ударников проспект','10.00 - 17.00', ['эскимо', 'стакан'])
    my_stand.describe_stand()
    my_stand.show_flavors()
    my_stand.show_Typesflavors()
    my_stand.check_flavor("клубничное")
    my_stand.check_flavor("ванильное")
    my_stand.add_flavor("фисташковое")
    my_stand.check_flavor("шоколадное")
    my_stand.remove_flavor("клубничное")
    my_stand.check_flavor("ванильное")
if x==2:
    f2() 

#12.3
def f3():
    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def get_menu(self):
            menu = "Добро пожаловать в наше кафе-мороженое " + self.name + "\n"
            menu += "У нас есть следующие сорты мороженого:\n"
            for flavor in self.flavors:
                menu += "- " + flavor + "\n"
            return menu
    my_stand = IceCreamStand("Мир морожки", ["ванильный", "шоколадный", "клубничный"])
    root = tk.Tk()
    root.title("Мир сладкого")
    root.geometry('400x250')
    menu_label = tk.Label(root, text=my_stand.get_menu())
    menu_label.pack()
    root.mainloop()
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")