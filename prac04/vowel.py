__author__ = 'jc450453'
vowelcount=0
vowel="aeiouAEIOU"
name=input("Enter your name")
for i in name:
        if i in vowel:
            vowelcount +=1
print("number of vowels in name are {}".format(vowelcount))