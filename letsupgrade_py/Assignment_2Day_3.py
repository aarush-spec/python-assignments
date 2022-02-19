# 1
a= 9
print (type(a))   # int

# 2
# int

# 3
a='9.'
print(type(a))   #str

# 4
a= (9)
print(type(a))  #int

# 5
a= False
print(type(a))   #boolean

# 6
a = [1, 2, 3, ]
print(type(a))  # list

#7
a=(1, 2, 3, )
print(type(a))  #tuple

#8
a = {'key':9}
print(type(a))     #dictionary

# 9
a= 1+ 9j
print(type(a))     #complex

#10
a=1
b=2
c=a/b
print(type(c))       #float

# 11
d = {'one': 1, 'two':2, 'three': 3}
print(d['two'])

# 12
t= (8, 9, 10)

# 13
# d = {one:1, two:2, three:3}
# d[one]
#Answer : here in dictionary
#         the key should be written between ' ' these because they are string
d = {'one':1, 'two':2, 'three':3}
print(d['one'])

# 14
# f = false not f
# Answer : Here the value stored in f are characters and they
#          should be included in  between these
#          inverted commas "  "
f = "false not f"
print(f)

# 15
lst = [1,3,5]
# lst[3]
# Answer : Error index out of range
#          Here in a list it is showing this error because in list the element
#          start counting from 0 and in the above list we only have 3 values
#          we have the index of 0, 1 and 2
#          if we have to print the last element we will write.
print(lst[2])