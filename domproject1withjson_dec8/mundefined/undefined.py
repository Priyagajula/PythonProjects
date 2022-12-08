from mperson import *
import json


class Undefined(Person) :
    def __init__(self):
        print("inside undefined class")
        self.person_standards = json.load(open("person_standards.json"))
        super().__init__()
        self.undefined_status()

    def undefined_status(self):
        print("You are not either men or women")

