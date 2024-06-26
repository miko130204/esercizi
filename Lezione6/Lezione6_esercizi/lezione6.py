from typing import Tuple

class Person:

    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender
        self._ssn: str = self.compute_ssn()

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        raise Exception("You cannot modify the name! ")
    
    def get_ssn(self):
        return self._ssn
    
    def set_ssn(self, ssn: str):
        """
        This function set the ssn
        input: ssn : str, the parameter contains the user's ssn
        return: none
        """
        self._ssn = ssn

    def compute_ssn(self) -> bool:
        first_three_name_char = self._name[:3]
        last_three_surname_char = self._surname[-3:]
        self._ssn = first_three_name_char + last_three_surname_char
        return self._ssn



person_1: Person = Person(name = "Miko", surname = "Garbatello", birth_date = "22/10/99", birth_place = "Italy", gender = "Male")

person_2: Person = Person(name = "Giuseppe", surname = "Magliana", birth_date = "10/02/89", birth_place = "France", gender = "Man")

queue: list[Person] = [person_1, person_2]

for person in queue:
    print(person.get_ssn())

###########################################################à

class Student:
    
    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        self._name: str = name
        self._studyProgram: str = studyProgram
        self._age: int = age
        self._gender: str = gender

    def get_info(self):
        return self._name, self._studyProgram, self._age, self._gender

student_1: Student = Student("Giovanni", "Nothing", 25, "UOMO")
student_left: Student = Student("Edgar", "Cyber", 24, "UOMO")
student_right: Student = Student("Spartaco", "Cloud", 23, "UOMO")

students = [student_1, student_left, student_right]
for x in students:
    print(x.get_info())


###########################################

class Animal:

    def __init__(self, name: str):
        self._name: str = name
        self._legs: str = self.set_legs()

    def set_legs(self):
        self._legs = 4

    def get_legs(self) -> int:
        return self._legs
    
    def PrintInfo(self):
        return (f"Name: {self._name}, legs: {self._legs}")
    

animal1: Animal = Animal("Fox")

print(animal1.PrintInfo())


#####################################

class Food:
    def __init__(self, name: str, price: float, description: str):
        self._name: str = name
        self._price: float = price
        self._description: str = description

class Menu:
    def __init__(self, food_list: list = []):
        self._foodlist: list = food_list

    def addFood(self, food = Food):
        self._foodlist.append(food)
    
    def removeFood(self, index: int):
        del self._foodlist[index]

    def printPrices(self):
        for food in food_list:
            print(food._price)

    def get_average_price(self) -> float:
        sium: float = 0
        for food in food_list:
            sium += food._price
        avg = sium/len(food_list)
        return avg

food1: Food = Food("Peach", 5, "Fruit")
food2: Food = Food("Meat", 10, "BONO")
food3: Food = Food("Pasta", 15, "CARBONARA")
food4: Food = Food("Cianuro", 100, "NON TOSSICO")
food5: Food = Food("Plutonio", 40, "yes")

food_list: list = [food1, food2, food3]
menu_fesso: Menu = Menu([food_list])

menu_fesso.addFood(food4)
menu_fesso.addFood(food5)
menu_fesso.removeFood(0)

print(menu_fesso.get_average_price())

