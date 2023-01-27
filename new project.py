list1 = []
list1.append(2)

say = 3

list2 = []

prime = True
while True:
    prime = True
    for eded in range(2,int(say**0.5)):
        if say % eded == 0:
            prime = False
            break
    
    
    if prime :
        list1.append(say)
        if len(list1) == 1000:
            break
    say+=1
for i in list1:
    if str(i).startswith("3") and str(i).endswith("7"):
        list2.append(i)
print(*list2)
print(len(list2))

