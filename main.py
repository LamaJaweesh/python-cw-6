person = { 
  "name": "lama",
  "age": 17,
  "hobbies": ["reading", "volleyball", "arguing"]
}
print(person["name"])
print(person["age"])

person["age"] = 18
person["country"] = "syria"

print(person)
print(len(person))
person["hobbies"].append("cooking")

def check_hobbies(person):
    if len(person["hobbies"])> 3:
        print("DAMNNN YOU ARE TALENTED")
        
check_hobbies(person)