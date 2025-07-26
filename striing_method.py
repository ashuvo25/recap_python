# upprer method

str = "my name is  shuvo".upper()
print(str)

#lower method
str = "SHE IS MY LOVE".lower()
print(str)

#cap italaization method
str = "sHe iS mY LOvE".capitalize()
print(str)

#count substring
str = "sHe iS .mY LOvE".capitalize().lower()
print(str.count("s"))


#String  multiplication and string addition

str1  = "shuvo"
intr = 3
intr2 = "5"
print (str1 * intr)
print (str1 + intr2)

 
# if , else  elif
str1 = "shuvo"
if str1.count('s') == 1:
    print(" S is present '-'")

# mint = int(input("Press an integer : "))
mint =25

if  mint  == 25 :
    print("Shuvo's fav num")
elif mint <=20  :
    print("Mint is not good")
else :
    print("Mint is good")


# Collection -------------------

litss = ['shuvo', 25, True]
print(litss)

#addint item in list
litss.append("It's me shuvo")
print(litss)

#Extending list
litss.extend([1,2,3,4])
print(litss)

#pop method
print(litss.pop())
print(litss)

#touple
tpl = ("shuvo", 25, True)
print(tpl) 

# loops
for  i in range(5, 10):
    print(i,end = " ")
print()
# iterating through list
for  i in litss:
    print(i,end = " ,")
print()

#print index  with items
for  i,element in enumerate(litss):
    print(i,element , end = " \n")
print()

#Slicing --------------------------
str1 = "shuvo is my name"
# [start: stop: stepS]
print(str1[:2])
# reversing  a string 
rev = str1[::-1]
print(rev)


# Set in python --------------------
sets = {1, 2,2,2, 3, 4, 5}
print(type(sets))
print(sets)
print(2 in sets, "2 is present in sets")
sets.remove(2)
print(sets)
print(2 in sets," 2 is not present in sets")
sets.add(2)
print(sets)
print(2 in sets, "2 is present in sets again")
#set methoda
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others


# Dictionary in python --------------------

    # dict {"key1": "value1",}
dicts = {"name " : "shuvo",
         "age": 25        
           }
print(dicts)
print("key      Value")
for i,j in dicts.items():
    print(i, j)
del dicts["age"]
print(dicts)
print("only keys")
for i in dicts:
    print(i)
for i in dicts:
    print(i,dicts[i])

#lambda function in python --------------------
x = lambda a,b : a+b*b
print(x(2,3))

#map and filter function in python --------------------

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.extend([11, 12, 13, 14, 15])
print(x)
# increase each element value by 2 using lambda
new_x = map(lambda i:i+2 , x)

print(list(new_x))
#filter 
new_x = filter(lambda i:i%2 , x)

print(list(new_x))


#  F string formatting in python --------------------
var = f'Hello {5+5+5} world {69} '
print ( var)