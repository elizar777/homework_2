

class Player:
    def __init__(self, pol, health):
        self.pol = pol 
        self.gun =' Копе - Лук - Меч'
        self.health = health
   
    
    def greeting(self):
        print("Добро пожаловать дрогой игрок! И ты единственный выживший!")
        player_name = input("Введите ваше имя: ")
        
        users_person = input(f"{player_name} для начало выберите персонажа {self.pol}: ")
                
        if users_person == "Женщина":
                print("Ваш персонаж Женщина")
        elif users_person == "Мужчина":
                print("Ваш персонаж Мужчина!")
        else:
                print("Ошибка. Попробуйте еще раз!")
       
        print(f"Игрок: {player_name}, у вас {self.health}hp  выберите любой предмет чтобы выживать! ")
        
        player_guns = input(f"Вы можете выбрать {self.gun}: ")
        if player_guns == "Копе":
                print("Вы выбрали копе!")
        elif player_guns == "Лук":
                print("Вы выбрали лук!")
        elif player_guns == "Меч":
                print("Вы выбрали меч!")
        else:
                print("Ошибка. Попробуйте еще раз!")
        
        
