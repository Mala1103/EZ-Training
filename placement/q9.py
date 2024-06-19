'''
You are given an integer array of size N, representing jars of chocolates. Three
students A, B, and C respectively, will pick chocolates one by one from each chocolate
jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task
is to fine and return an integer value representing the total number of chocolates that
student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format :
input1: An integer array representing the quantity of chocolates in each jar.
input2: An integer value N representing the number of jars.
Output Format:
Return an integer value representing the total number of chocolates that student A
will have, after all the chocolates are picked.
Example:
Input:
10 20 30
3
Output:
21
'''
arr =list(map(int,input()))
n=int(input())
c=0
for i in range(n):
 if i==0:
    continue
 if(i<=3):
    c=c+1
 else:
  if(1%3==0):
      c=c+i//3
  else:
      c=c+(i//3)+1
print(c)