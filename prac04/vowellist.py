__author__ = 'jc450453'
vowel=['a','e','i','o','u']
name=input("Enter your name")
vowelcount=0
for c in name:
    if c.lower() in vowel:
        vowelcount +=1
print("out of {} letters,{} has {} vowels".format(len(name),name,vowelcount))

