# functions arguments
def average(a,b):
    print("The average is ", (a+b)/2)
    
average(7,9)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
         sum = sum + i
    print("*average is: " ,sum/len(numbers))


average(9,8)