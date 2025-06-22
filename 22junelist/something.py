words = ["hello", "niklo", "ohhoo", "chalhat", "sunja"]

for i in words:
    print(i[0])


first_letters = [word[0] for word in words]   

print(first_letters)

number = words[:2]

print(number)

import random

new_list = random.sample(words, 2)

print(new_list)