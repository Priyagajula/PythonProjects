from mwomen import *
from mmen import *
from mundefined import *

gender = str(input("what is your gender? woman/men/undefined")).lower()
if gender == "woman":
    person = Women()
elif gender == "men":
    person = Men()
else:
    person = Undefined()