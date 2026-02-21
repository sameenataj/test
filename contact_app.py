import json

# people = [
#     {'name':'john','email':'john@gmail.com','age':'25'},
#     {'name':'bob','email':'bon@gmail.com','age':'52'},
#     {'name':'johnny','email':'johnny@gmail.com','age':'34'},
#     {'name':'beth','email':'betn@gmail.com','age':'25'},
# ]

def display_people(people):
    for i,person in enumerate(people):
        print(i+1,'-',person['name'],'|',person['age'],'|',person['email'])

def add_person():
    display_people(people)
    name = input('Name: ')
    email = input('Email: ')
    age = input('Age: ')

    person = {"name":name, "email":email,"age":age}
    return person   

def delete_contact(people):
    display_people(people)
    while True:
        print('No of contacts in the list: ',len(people))
        number = input('enter a number to delete: ')
        try :
            number = int(number)
            print('number entered is: ',number)
            if number<=0 or number > len(people):
                print('invalid number')
            else:
                break
        except:
            print('invalid number')
    people.pop(number - 1)
    print('entry deleted.')

def search_person(people):
    display_people(people)
    search_name = input("Enter name/part of name: ").lower()
    results = []

    for person in people:
        name = person["name"].lower()
        if search_name in name:
            results.append(person)
    print('-----search results---')
    display_people(results)


print("Welcome to contact management app")
print()


with open("contacts.json","r") as f:
    people = json.load(f)["contacts"]

print("No. of contact: ", len(people))
print()

while True:
    command = input('Command (add/delete/search/Q for quit): ').lower()
    if command == 'add':
        person = add_person()
        people.append(person)
        print('person added')
        display_people(people)
    elif command == 'delete':
        delete_contact(people)
    elif command == 'search':
        search_person(people)
    elif command == 'q':
        break
    else:
        print('invalid command')

with open("contacts.json","w") as f:
    people = json.dump({"contacts":people},f)