'''  
QUESTION
        n   
  y =    E   ((x^i) + (iy))
        i=1  
        
        Note : from the above formula, the letter E is used to represent the summation sign
        Represent the above formula with a program in python
'''
x= int(input("x: "))
y= int(input("y: "))
n = int(input("last number: "))
num = 0
sum = 0
for i in range(1,n):
    print("i: ", i)
    num = (x**i) + (i*y)
    print(f"num: {num}")
    sum = sum + num
    print(f"sum: {sum}")
y = sum   
print(" ")
print(f"y = {y}")

      

      
