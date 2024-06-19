str=input()
first=0
lst=['a','e','i','o','u']
for i in str:
    if(i in lst):
        first=i
        break
for i in str:
    if(i==first):
        print(i)