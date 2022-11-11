
# find the largest number from a list
#method 1:
number = [20,50,40,30,70,60]
number.sort()
#number = [20,30,40,50,60,70]
print("Largest element is: ",number[-1])


#method 2:
print("largest number is: ",max(number))


#method 3:
marks = []
num = int(input("Enter number of students:  "))
for i in range(1,num+1):
    element = int(input("Enter element: "))
    marks.append(element)
print("Largest element is: ",max(marks))


#method 4
def myMax(list):
    max = list[0]

    for x in list:
        if x > max:
            max = x

    return max
list = [20,50,40,30,70,60]
print("Largest number is: ",myMax(list))