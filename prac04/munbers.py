__author__ = 'jc450453'
numbers=[]
for i in range(1,6):
 num=int(input("Enter number"))
 numbers.append(num)
print(numbers)
print("the first number is ",numbers[0])
print("the last number is ",numbers[-1])
print("the smallest number is ",min(numbers))
print("the largest number is ",max(numbers))