from mwomen import *
import json

class Person:
    def __init__(self, gender="undefined"):
        self.hands = self.get_hands()
        self.fingers = self.get_fingers()
        self.toes = self.get_toes()
        self.feet = self.get_feet()
        self.age = self.get_age()
        self.name = self.get_name()
        self.gender = gender



    def get_hands(self):
        hands = int(input("Enter hands to set"))
        while not (self.person_standards["person"]["hands"]["min"] <= hands <= self.person_standards["person"]["hands"]["max"]):
            hands = int(input("invalid hands,Enter value between 0 and 2"))
            if self.person_standards["person"]["hands"]["min"] <= hands <= self.person_standards["person"]["hands"]["max"]:
                print(f"hands are now  {hands}")
        return hands


    def get_fingers(self):
        fingers = int(input("Enter the no of fingers"))
        while not (self.person_standards["person"]["fingers"]["min"] <= fingers <= self.person_standards["person"]["fingers"]["max"]):
            fingers = int(input("Invalid fingers,Enter value between 1 and 10"))
            if self.person_standards["person"]["fingers"]["min"] <= fingers <= self.person_standards["person"]["fingers"]["min"]:
                print(f"fingers are set to  {fingers}")
        return fingers


    def get_toes(self):
        toes = int(input("Enter no of toes"))
        while not (self.person_standards["person"]["toes"]["min"] <= toes <= self.person_standards["person"]["toes"]["max"]):
            toes = int(input("invalid toes,Please enter value between 1 and 10"))
            if self.person_standards["person"]["toes"]["min"] < toes < self.person_standards["person"]["toes"]["max"]:
                print(f"toes are set to  {toes}")
        return toes


    def get_feet(self):
        feet = int(input("Enter no of feet"))
        while not(self.person_standards["person"]["feet"]["min"] <= feet <= self.person_standards["person"]["feet"]["max"]):
            feet = int(input("invalid feet,Enter value between 0 and 2"))
            if self.person_standards["person"]["feet"]["min"] <= feet <= self.person_standards["person"]["feet"]["max"]:
                print(f"feet are now {feet}")
        return feet

    def get_age(self):
        age = int(input("Enter the age"))
        while not self.person_standards["person"]["age"]["min"] < age < self.person_standards["person"]["age"]["max"]:
            if age < self.person_standards["person"]["age"]["min"]:
                age = self.person_standards["person"]["age"]["min"]
            elif age > self.person_standards["person"]["age"]["max"]:
                age = self.person_standards["person"]["age"]["max"]
            print(f"age is set to default {age}")
            break
        return age


    def get_name(self):
        name = input("Enter name")
        while not (self.person_standards["person"]["name"]["min"] <= len(name) <= self.person_standards["person"]["name"]["max"]):
            name = input("Invalid name, enter name again between 5 to 10 characters")
            if self.person_standards["person"]["name"]["min"] <= len(name) <= self.person_standards["person"]["name"]["max"]:
                print(f"new name is {name}")
        return name

    #def get_gender(self):
    #    gender = input("Enter the gender")
    #    if gender == "women":
    #        pass
    #    elif gender == "men":
    #        pass
    #    while not (gender == "women") and not (gender == "man"):
    #        gender = "undefined"
    #        print(f"setting gender to default as {gender}")
    #        break
    #    return gender

