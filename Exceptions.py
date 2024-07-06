try:
   x= int(input("Enter the first number: "))
   y=int(input("Enter the second number: "))
   print(x/y)
except:
   print("Number cannot be divided by 0")    
#Instead of a statement we can pass the Exception

try:
   print(7/0)
except:
   pass
print("Way maker")

try:
   print(7/0)
except ZeroDivisionError as e:
    print(e)
    print("Goodness of God")

try:
   print(7/"Hell")
except TypeError as e:
    print(e)
    print("This is a type error")

try:
   print(int(6/0))
except ValueError as e:
    print(str(e))
    print("This is a Exception")   
except Exception as e:
   print("I love his Mercy")    

try:
   print(6/int("j"))
except (ValueError, ZeroDivisionError )as e:
    print(str(e))
    print("This is a Exception")  
    #raise 
except Exception as e:
   print("I love his Mercy") 

try:
   print(int(6/0))
except ValueError as e:
    print(str(e))
    print("This is a Exception")   
except Exception as e:
   print("I love his Mercy")    
finally:
   print("Thanx for listening")

try:
   print(int(6/7))
except ValueError as e:
    print(str(e))
    print("This is a Exception")   
except Exception as e:
   print("I love his Mercy")    
else:
   print("The love of God")



class myException(Exception):
   pass
try:
   age=(int(input("Enter your age please: ")))
   if (age<18):
      raise myException
except:
   print("Go do housework kid!!!!") 
else:
   print("Hey,you can even sip 20 bottles")  

