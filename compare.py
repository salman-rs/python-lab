list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))
print("Same length:", len(list1) == len(list2))
print("Sum equal:", sum(list1) == sum(list2))
common = False
for x in list1:
     if x in list2:
         common = True
         break
print("Common present:", common)
