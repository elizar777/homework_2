def fillings():
    print("Начинки")
    print("Есть 3 вида")
    print("колбаса", "грибы", "оливки")
    user = input("Ввеберите начинку")
    if user == "колбаса":
        print("тесто с колбасой")
    elif user == "грибы":
        print("тесто с грибы")
    elif user == "оливки":
        print("тесто с оливками")
    else:
        print("Нету")
    