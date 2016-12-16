__author__ = 'jc450453'
scores=[]
score=int(input("enter score"))
while score>=0:
    scores.append(score)
    score=int(input("enter score"))
if scores!=[]:
  print("your highest score is:",max(scores))
#print("your highest score is:",sum(scores))