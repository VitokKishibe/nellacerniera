import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 20
        self.progress = 0
        self.eat = 10
        self.alife = True

    def to_sleep(self):
        print("nia miau nyaa..")
        self.gladness += 10
        self.progress += 1
        self.eat -= 3

    def to_find_food(self):
        print("myaaaa")
        self.gladness -= 5
        self.progress += 15
        self.eat += 25

    def to_chill(self):
        print("myaurrrr")
        self.gladness += 5
        self.progress -= 0.1
        self.eat += 5

    def is_alive(self):
        if self.progress < -10:
            print("nya...")
            print("ДЕД")
            self.alife = False
        elif self.gladness < -20:
            print("myaunia...")
            print("ДЕД")
            self.alife = False
        elif self.eat < -25:
            self.alife = False
            print("miau nyaa.....")
            print("ДЕД")

    def end_of_day(self):
        print(f"Progress = {round(self.progress, 4)}")
        print(f"Eat = {round(self.eat, 4)}")
        print(f"Gladness = {round(self.gladness, 4)}")

    def life(self, day):
        day = "Day " + str(day) + " of" + self.name + "life"
        print(f"{day:=^50}")
        life_cube = random.randint(1, 3)
        if life_cube == 1:
            self.to_find_food()
        elif life_cube == 2:
            self.to_sleep()
        elif life_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

bruno = Cat(name=" Bruno Bucciarati ")
for day in range(365):
    if bruno.alife == False:
        break
    bruno.life(day)
