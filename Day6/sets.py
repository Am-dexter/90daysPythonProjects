#
shopping = {'cereals', 'milk', 'bread', 'butter', 'sodas', 'beer'}

#loop through the set
if 'milk' in shopping:
    print("Buddy, you already have milk! ")
else:
    print("You need to buy milk!")

#Add items to the set

shopping.add('oranges')

print(shopping)

#add multiple items to the set

shopping.update(['mangoes', 'beans', 'juice'])

print(shopping)

#remove an item from the set

shopping.remove('mangoes')

print(shopping)