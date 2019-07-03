nm1 = ("kamal")
nm2 = ("raja_sir")
print(id(nm1))#jst to know the identity of the given string;
print(id(nm2))
#lets try on list
list1 = [23,23,56,78,45,67]
if(id(list1[0]) == id(list1[1])):#checking identity of a number in the list;
  print("ture")
else:
  print("false")