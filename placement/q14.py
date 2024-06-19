#        1
#       212
#      32123
#     4321234
#    543212345  
   
   
n=int(input())
result=n*1
num=2
for i in range(n-1,0,-1):
    result+=2*i*num
    num+=1
print(result)
# 5
# res=5*1=5
# num=2
# i=4
# result=5+(2*i*num)