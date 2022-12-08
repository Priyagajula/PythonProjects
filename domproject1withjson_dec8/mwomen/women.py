from mperson import *
from mundefined.undefined import *
import json

class Women(Person):
    def __init__(self):
        print("test")
        #self.hands = 2
        #print(f"hands are {self.hands}")
        self.person_standards = json.load(open("person_standards.json"))
        super().__init__("Woman")
        self._is_Pregnent()

    def _is_Pregnent(self):
        print("inside is pregnent")
        pregnency = input("Enter yes if pregnent else no")
        if pregnency == "yes":
            print("You are pregnent")
        elif pregnency == "No":
            print("you are not pregnent")
        else:
            print("undefined")
            ud.undefined_status()





