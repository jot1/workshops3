__author__ = 'jc450453'
n=0
temp_file = open("numbers.txt","w")
while n>=0:
    n=int(input("enter number"))
    if n>=0:
      print(str(n), file=temp_file)
temp_file.close()