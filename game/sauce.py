def sauce():
    print("Виды соусов")
    print("кетчуп", "горчица")
    user = input("Ввеберите соус: ")
    if user == "кетчуп":
        print("Тесто с кетчупом")
    elif user == "горчица":
        print("Тесто с горчисей")
    else:
        print("Ошибка, такого соуса пока нет")
    