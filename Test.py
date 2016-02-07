n = int(input())
a = [i+1 for i in range(n)]
s = []
number = []
for i in a:
	for j in range(i):
		s.append(i)
print (s)
while len(number) != n:
	for l in s:
		print (l)
		number.append(l)
print (number)
print (a)
print (n)
