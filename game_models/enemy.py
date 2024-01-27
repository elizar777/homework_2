from player import Player    
    
       
class Enemy(Player):
    def __init__(self, name, health):
        super().__init__(name, health)

    def fight(self):
        print("Ты увидел впереди врагов:")
        print("1. Гоблин (23 HP)")
        print("2. Эндермен (100 HP)")
        print("3. Ведьма (50 HP)")
        
        while True:
                users_choice = input("Выберите врага, с которым будете сражаться: ")
                if users_choice == "1":
                        print("Ты выиграл (:")
                elif users_choice == "2":
                        print("Ты проиграл ):")
                        print("Начни все сначала!")
                        break
                elif users_choice == "3":
                        print("Ты выиграл (:")
                else:
                        print("Ошибка. Выберите врага еще раз!")



player = Player("Женщина или Мужчина", 60)
enemy = Enemy("Враг", 0)
player.greeting()
enemy.fight()