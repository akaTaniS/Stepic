# x=int(input())
# h=int(input())
# m=int(input())
# H = x//60
# M = x%60
# Mm = (m+M)//60
# print (H+h+(Mm))
# print ((M+m)%60)

# z=60+5
# print (z%60)

# x = 5
# y = 10
# print(False or True)

# a = True
# b = False
# print (False or False)

# a=int(input())
# b=int(input())
# h=int(input())
# if h > b:
# 	print("Пересып")
# elif h < a:
# 	print("Недосып")
# else: 
# 	print('Это нормально')

# n=int(input())
# if 1900 <= n <= 3000:
# 	if (n % 4) == 0 and (n % 100) != 0 or (n % 400) == 0:
# 		print("Високосный")
# 	else:
# 		print("Обычный")

from math import sqrt
# a=int(input())
# b=int(input())
# c=int(input())
# p=(a+b+c)/2
# s=sqrt(p*(p-a)*(p-b)*(p-c))
# print(s)

# x = int(input())
# if x > -15 and x <= 12 or x > 14 and x <17 or x >= 19:
# 	print (True)
# else:
# 	print (False)

# x = float(input())
# y = float(input())
# z = input()
# if z =="+":
# 	print (x+y)
# elif z == "-":
# 	print (x-y)
# elif z== "/" and y != 0:
# 	print (x / y)
# elif z == "*":
# 	print (x*y)
# elif z == "mod" and y != 0:
# 	print (x%y)
# elif z == "pow":
# 	print (x**y)
# elif z == "div" and y != 0:
# 	print (x//y)
# else:
# 	print ("Деление на 0!")

# type = input()
# if type == "треугольник":
# 	a = int(input())
# 	b = int(input())
# 	c = int(input())
# 	p = (a+b+c)/2
# 	print (sqrt(p*(p-a)*(p-b)*(p-c)))
# elif type == "прямоугольник":
# 	a = int(input())
# 	b = int(input())
# 	print (a*b)
# elif type == "круг":
# 	r = int(input())
# 	print (3.14 * (r ** 2))

# a = int(input())
# b = int(input())
# c = int(input())
# if a >= c and b < c:
# 	print (a, b, c, sep="\n")
# elif a >= b and b >= c:
# 	print (a, c, b, sep="\n")
# elif b >= a and c <= a:
# 	print (b, c, a, sep="\n")
# elif b >= c and c >= a:
# 	print (b, a, c, sep="\n")
# elif c >= b and b <= a:
# 	print (c, b, a, sep="\n")
# elif c >= a and b >= a:
# 	print (c, a, b, sep="\n")

# n = int(input())
# x = n % 10
# if x == 0 or x == 5 or x == 6 or x == 7 or  x == 8 or x == 9 or (n >= 11 and n <= 20) or (n >= 111 and n <= 120) or (n >= 211 and n <= 220) or (n >= 311 and n <= 320) or (n >= 411 and n <= 420) or (n >= 511 and n <= 520) or (n >= 611 and n <= 620) or (n >= 711 and n <= 720) or (n >= 811 and n <= 820) or (n >= 911 and n <= 920):
# 	print (n, "программистов")
# elif x == 1:
# 	print (n, "программист")
# elif x == 2 or x == 3 or x == 4:
# 	print (n, "программиста")

# 0 5 6 7 8 9 10
# 		1 
# 		2 3 4

# num = float(input())
# x = num // 1000
# y = (num * 0.001)-x
# z = (y*1000)//1
# q = x//100
# w = ((x*0.01)-(x//100))*10 
# e = ((x*0.1)-(x//10))*10 
# r =  z//100
# t = ((z*0.01)-(z//100))*10
# s = ((z*0.1)-(z/10))*10 
# X = int(q) + int(w) + int(e)
# Y = int(r) + int(t) + int(s)
# if X == Y:
# 	print ("Счастливый")
# else: print ("Обычный")
# print (int(q), int(w), int(e), int(r), int(t),s, x, y,  z)

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# n=int(input())
# s=0
# while n!=0:
# 	s+=n
# 	n=int(input())
# print(s)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     print (i)
#     if s > 15:
#         break
#     i = i + 1

# while True:
# 	a = int(input())
# 	if a < 10:
# 		continue
# 	elif a > 100:
# 		break
# 	print (a)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a != b:
# 	print (" ",'\t', c,'\t', d)
# 	for i in range (a, b+1):
# 		print (i,'\t', c*i,'\t', d*i)
# else:
# 	print (" ",'\t', c,'\t')
# 	for i in range (a, b+1):
# 		print (i,'\t', c*i,'\t')

# a, b = (int(i) for i in input().split())
# s=0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b +1, 2):
#     s +=i
# print (s)

# a, b = (int(i) for i in input().split())
# s = 0
# x = 0
# if a % 3 != 0:
#     a += 1
# if a % 3 != 0:
# 	a += 1
# for i in range(a, b +1, 3):
#     s += i
#     x += 1
# print (s/x)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# header = list()
# for i in range(c, d+1):
# 	header.append(str(i))
# print(u"\t" + u"\t".join(header))
	
# for i in range(a, b+1):
# 	row = list()
# 	row.append(str(i))
# 	for j in range(c, d+1):
# 		row.append(str(i*j))
# 	print(u"\t".join(row))
# print(u"\t")

# gc = input()
# g = gc.lower().count("g")
# c = gc.lower().count("c")
# print((g+c)/len(gc)*100)
# print(g,c)

# num = str(input())
# if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
# 	print("Счастливый")
# else:
# 	print("Обычный")

# s = "abcdefghijk"
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-1:-10:-2])
# print(s[-3:])
# print(s[:-6])
# print(s[6])

# s = input()
# num = 1
# x = 1
# nexts = s[x:x+1]

# for i in s:
# 	if i in nexts:
# 		num += 1
# 	else:
# 		print(i, end="")
# 		print(num, end='')
# 		num = 1
# 	x += 1
# 	nexts = s[x:x+1]	

# students = ['Ivan', 'Masha', 'Sasha']
# num = [1]
# students += ['Olga']
# students += 'Olga'

# print(len(students))
# print(min(students), max(students))

# num = list(input().split())
# sum = 0
# for x in num:
# 	sum += int(x)
# print(sum)


# num = [int(i) for i in input().split()]
# fist = num[0-1] + num[1]
# end = num[-1-1] + num[0]
# print(fist, end=" ")

# for x in num:
# 	if x == num[-1]:
# 		print(end)
# 		break
# 	else:
# 		print(num[x-1] + num[x+1], end=" ")

# n = [int(i) for i in input().split()]
# m = 0
# for i in n:
# 	m = i

# print("Type integers, each followed by Enter; or ^D or ^Z to finish")
# total = 0
# count = 0
# while True:
# 	try:
# 		line = input()
# 		if line:
# 			number = int(line)
# 			total += number
# 			count += 1
# 	except ValueError as err:
# 		print(err)
# 		continue
# 	except EOFError:
# 		break
# if count:
# 	print("count =", count, "total =", total, "mean =", total / count)

# Задачи по материалам недели – Шаг 10

# sum1 = 0
# sum2 = 0
# while True:
# 	n = int(input())
# 	sum2 += n*n
# 	sum1 += n
# 	if sum1 == 0:
# 		print (sum2)
# 		break

# n = int(input())
# a = [i+1 for i in range(n)]
# s = []
# number = []
# for i in a:
# 	for j in range(i):
# 		s.append(i)
# for l in s:
# 	print (l, end =" ")
# 	number.append(l)
# 	if len(number) == n:
# 		break

# Списки – Шаг 11
# n = [int(i) for i in input().split()]
# n.sort()
# prev = None
# sort = []
# end = []
# for i in n:
# 	if n.count(i) > 1:
# 		sort.append(i)
# for i in sort:
# 	if prev != i:
# 		end.append(i)
# 	prev = i
# for i in end:
#     print(i, end = " ")

# def check(x):
# 	if x == []:
# 		print('Отсутствует')
# 	else:
# 		for i in x:
# 			print(i, end = ' ')
# lst = [int(i) for i in input().split()]
# x = int(input())
# lst1 = []
# count = 0
# for i in lst:
# 	if i == x:
# 		lst1.append(count)
# 	count += 1
# check(lst1)


# matrix= []
# while True:
#     inp = input()
#     if inp == 'end':
#         break
#     matrix.append(inp.split())
# print(matrix)

string = m = []
while string != 'end':
    string = input()
    m.append(list(map(int, string.split(' ')))) if string != 'end' else None
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]
[print(' '.join(map(str, row))) for row in new]

