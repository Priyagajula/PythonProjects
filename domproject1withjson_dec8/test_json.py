import json

person_standards = json.load(open("person_standards.json"))
#print(json.dumps(json_data,indent=2))
#print(json_data["person"]["age"])
#print(person_standards["person"]["age"]["min"])
#print(person_standards["person"]["fingers"]["min"])
print(person_standards["person"]["name"]["min"])
