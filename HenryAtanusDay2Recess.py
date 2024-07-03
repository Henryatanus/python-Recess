# control structures
# if ,elif, else
import math
age=40
if age < 18:
     print ("Go home,read books please!!")
elif age >=18&age<=75:
     print("You can bet and drink")  
else:
     print("Go rest, your too old to reason")  
love=80
if love>=95:
     print("This is true love")
elif love>=80:
     print("They really love each other")
elif love>=75:
     print("They are dating")
else:
     print ("Might be gayz")  
# exercise two


def drink_alcohol(age):
     if age < 18:
         return age*0
     elif age >= 18 and age <= 75:
         return age*500
     elif age >= 75 and age <= 100:
         return age*1500
     else:
         return math.pi

age = int(input("Enter your age: "))
price = drink_alcohol(age)
print(f"Your movie price is: {price}")

# loops for loop and while loop
cars=["Tesla","Audi","BMW","Jeep","RangeRover"]
  # exercise   colors=["Blue", "black","aqua"]
colors =["blue","yellow","aqua"]  
for color in colors:
    print (color)
    
counting=5
while counting>=1:
    print("count 5 to 1",counting)
    counting-=1
    
# Reversing using for loop
colors = ["blue", "yellow", "aqua"]  # List of colors
reverse_color = colors[::-1]  # Reverse the list using slicing
for color in reverse_color:
    print(color)
    
    

# using while loop
Fruits = ["Apple", "Orange", "Mango","Pineapple"]  

index = len(Fruits) - 1  #  last index
while index >= 0:
    print(Fruits[index])
    index -= 1