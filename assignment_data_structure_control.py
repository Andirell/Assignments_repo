# ====================== PYTHON BASICS ASSIGNMENT ======================
import time
#1
'''
student = {
    "name": "Andi",
    "age": 25,
    "course": "Computer Science",
    "score": "98"
    }

print(student)

'''

#2
'''
student["score"] = "99"
print(student)

'''

#3

# car = {
#        "brand": "Toyota",
#        "model": "Camry",
#        "details": {
#        "year": 2021,
#        "engine": "V6"
#        }
#    }

# print(
#     car["details"]["engine"]

# )

#4

# car["details"]["year"] = 2024
# print(car)

#5
'''
new_list = ["Andi", 25, True, ["A billionaire in the making"]]

print(new_list)

'''

#6
'''
names = ["Ali", "Bola", "Chidi", "Dami"]

names[2] = "Emeka"
print(names)

'''

#7

'''
names.append("Andi")
names.remove("Ali")
print(names)

'''

#8
'''
has_in = "Bola" in names
print(has_in)

'''

#9
'''

numbers_6 = (7, 3, 4, 1, 2, 9)
to_slice_1 = numbers_6[0:3]
to_slice_2 = numbers_6[-2: ]

print(to_slice_2)
'''

#10
'''
set1 = {1, 3, 5, 7}
set2 = {5, 7, 9, 11}

union = set1 | set2
intersect = set1 & set2
print(intersect)

'''

#11
'''
difference = set1 - set2
print(difference)

'''

#12
'''
mark = input("Whats your mark?: ")
if int(mark) >= 80:
    print("Excellent")
elif int(mark) > 50 and int(mark) <= 79:
    print("You passed")
else:
    print("You are a failure!")

print(mark)

'''

#13
'''
colors = ["red", "blue", "green", "yellow"]
for color in colors: 
    if color == "green":
        print("Green found")
        continue
    else:
        print(color)

'''

#14
'''
num = 1
while num < 7:
    print(num)
    num = num + 1
else: 
    print("Numbers less than 7")

'''

#15
'''
num = 0
while num < 5:
    num = num + 1
    print(num)
    time.sleep(1)
else:
    print("loop ended")

'''


    
   





