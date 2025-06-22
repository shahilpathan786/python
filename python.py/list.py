nums = [2 , 3 , 6 , 8]
#print(nums[3])

#print(nums[0:3])

nums[2] = 5
#print(nums)

nums.append(9)
nums.insert(2 , 10)

#print(nums)

nums.remove(5)

#print(len(nums))

# for i in nums :
#     print(i)

# if 5 in nums:
#     print("found")    
# else :
#     print("not found")   

# nums.sort()    #use it for arrange in ascending order

nums.sort(reverse=True)

# print(nums)

#use combine a and b to combine the list

#count even numbers --------------------

nums2 = [2, 4, 5, 9, 21, 34, 33]

# even_number = 0

# for i in nums2 :
#     if i % 2 == 0 :
#         even_number += 1

# print(even_number)        

#we use pop() to remove the last elemnet inn the list

#......................To Do list...........................#

# tasks = []

# def add_task(task):
#     tasks.append(task)

# def show_tasks():
#     for i , task in enumerate(tasks) :
#         print(f"{i + 1}.{task}") 

# add_task("Buy milk")      
# add_task("go for walk")    
# show_tasks()

import random

number = random.randint(1, 10)

guesses = []

while True :
    guess = int(input("Guess: "))
    guesses.append(guess)
    if guess == number :
        print("correct")
        break
    else:
        print("Try again")

print("Your guesses : " , guesses)   

# .........///////////./////////////////.......conatct book ................,,,,,,,,,,,,,,,......#

contact = []

def show_menu() :
    print("\n ---Contact Book")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name :")
    number = input("Enter your number : ")
    contact.append([name , number])
    print("Contact added")

def view_contacts():
    if not contact:
        print("NO CONTACT ADDED")
    else:
        print("\n ------All contacts------")
        for i, contact in enumerate(contact , start= 1):
            print(f"{i}.Name : {contact[0]} , phone: {contact[1]}")

def search():
    name = input("Enter the name to search")
    found = False
    for contacts in contact:
        if contact[0].lower() == name.lower():
            contact.remove(contacts)
                        
    









