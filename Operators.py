# operators -
"""
1) arithmetic operators  +, -, *, /-3.5, //- floor division(3),%modulo (you will get remainder)
2)Assignment operators +=,-=
3)comparison operators
4)logical operators
5)Bitwise Oper - Binary numbers 
6)Special Op- 1) Identity operators 2) memebership operators
"""

"""
a=10
b=3
print(a%b)


a+=5
print(a)
a-=5
print(a)

a=10

"""

# compariosn operator - >,>=,<,<=,==,!=


"""
a=50
b=25
print(a>b)# condition
"""
"""
a=18
b=18
print(a>=b)# true will be output
print(a==b)# o/p will be true
print()a!b)# true

"""


#logical operators
#and- True and True  = True
#or - True or False = True
#Not - opposite
""""
a=10
b=20
print((a>50) and (b>=15))

print((a>50) or (b>=15))

print(not a) ## negatives
"""

###Biwise Operators - bitwise and = "&", bitwise or "|",bitwise Not - "~", bitwise xor - "^"
##bitwise right shift>>, bitwise left shift<<
"""
a=10
b=4
print(a|b)#output is o
"""

# Bitwise not -~
"""
a=10
print(~a)#(+1)=-(11) one increment and neggate the value
"""

# special operators 

# ##bitwise right shift>>
"""
a=10
print(a<<2)
print(a>>1)
"""
""
a=50
print(a>>1)

""
"""
a=4
print(a>>1)
"""

"""
a=10
print(a<<1)
"""

#speial operators- identity operators - is / is not / memebership operators -  in/ not in

user_id = 150
print(id(user_id))
print(user_id)

user_id2 = 150
print(id(user_id2))
print(user_id2)

print(user_id is user_id2)

lst1=[1,2,3]
print(id(lst1))
lst2=[1,2,3]
print(id(lst2))
print(lst1 is lst2)

#membership operator - in and not in

greetings = "python programming"
print ('python' in greetings)































