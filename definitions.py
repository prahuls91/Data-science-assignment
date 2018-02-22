#lambda is a simple 1 line function
#do not use def or return keywords

# lambda function 
#lambda x:2*x
# traditional approach def double(x):
	#return x*2 
#max of x,y
max=lambda x,y:x if x>y else y
print(max(8,5))
#map 
#apply same function to each element of a sequence and returns the modified list
n=[4,3,2,1]
print(list(map(lambda x:x**2,n)))
#list comprehension
print([x**2 for x in n])
#filter
#Filter items out of a sequence.It has a condition and a value.
print(list(filter(lambda x:x>2,n)))
#list comprehension
print([x for x in n if x>2])
# reduce applies the same operations to items in the sequence
#returns an item not list
#n=[4,3,2,1]
#print(reduce(lambda x,y:x*y,n))
#nestedfor
for i in range(0,3):
	for j in range(0,4):
		print (i,j)