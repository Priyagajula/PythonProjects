from mperson import *
import json
class Men(Person):
    def __init__(self):
        print("inside men class")
        # self.hands = 2
        # print(f"hands are {self.hands}")
        self.person_standards = json.load(open("person_standards.json"))
        super().__init__("men")
        self.setMan()

    def setMan(self):
        print("Watching TV")