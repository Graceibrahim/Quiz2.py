def list_comprehension():
	a=[100, 110, 120, 130,140,150]
	for x in a:
		h[x]=x%3
	return h
def sorted():
	a=["apple", "banana","mango"]
	b=["avocado","peach", "orange"]
	c=["pineapple","lemon"]
	d = list(set(a+b+c))
	print(d)

def divisible_by_three(n):
	range_divisible=(1,n+1)
	divisible=(range_divible)%3
	print (divisible)

def flatten():
	x=[[1,2],[3,4],[5,6]]
	for a in x:
	for b in a:
		x.append(b)

def smallest():
    a = [1,3,6,8,2,4,5.7]
    print(min(a))

def removes():
	x=['a','b','a', 'e', 'd','b', 'c','e', 'f', 'g', 'h']
	for a in x:
		if(a==a)
		x.append(a)
	return x
		
def squares():
	x=range(149,159)
	for a in range x:
		print{a:a**2}