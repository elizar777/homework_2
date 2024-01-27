
class Computer:
    def __init__(self, cpu, memory):
        self.z__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu  
    
    
    @property
    def memory(self):
        return self.__memory 
    
    def __make_computations(self):
        print(f"Cложение: {self.cpu + self.memory}, Деление : {self.cpu / self.memory}")
        print(f" Умножение: {self.cpu * self.memory}, Разность: {self.cpu-self.memory}")
    
    @property
    def make_computations(self):
        return self.__make_computations
    
computer = Computer(3,5)
computer.make_computations()
    
    
class Laptop(Computer):
    def __init__(self, cpu, memory,memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    
    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"Процессор - {self.cpu}, Память = {self.memory}, Карта памяти = {self.memory_card} gb")

laptop = Laptop ("Ryzer 9", 2048, "32")
laptop.info()


    
    
    
    
# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
# 3. Добавить геттеры к существующим атрибутам.
# 4. Создать класс Laptop - который наследуется от класса Computer с приватным полем memory_card(карта памяти)
# 5. Добавить геттеры к существующему атрибуту.
# 6. Распечатать информацию о созданных объектах с помощью метода info
# 7. Опробовать все возможные методы каждого объекта
