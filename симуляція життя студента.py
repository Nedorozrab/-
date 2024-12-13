import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.knowledge = 0
        self.energy = 100

    def live_day(self):
        action = random.choice(["work", "study", "rest"])
        if action == "work":
            self.money += 50
            self.energy -= 20
        elif action == "study":
            self.knowledge += 10
            self.energy -= 15
        elif action == "rest":
            self.energy += 30
            self.money -= 20
        print(f"{self.name} {action}. Гроші: {self.money}, Знання: {self.knowledge}, Енергія: {self.energy}")

    def live_year(self):
        for day in range(365):
            if self.energy <= 0:
                print(f"{self.name} занадто втомився.")
                break
            self.live_day()
        print(f"Рік завершено. Гроші: {self.money}, Знання: {self.knowledge}, Енергія: {self.energy}.")

# Створення студента
student = Student(name="Олег")
student.live_year()
