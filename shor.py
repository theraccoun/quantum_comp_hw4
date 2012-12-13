import socket
import math
from decimal import *

class Shors:

	def __init__(self):
		self.n = 26825926351488399110544112048484691246984742691774090660107762225282840929762385037237484102637951592668796347757856945214753994377357682664648613794306195119897925017866009997263150512915863644811383848031675519987679409974919170391509730554029294470146117971727639921754779476671008586376903725402571129
		self.exponent = int(2 * math.log(self.n, ))
		print "exp: " , self.exponent

	def run(self):
		self.c = Decimal(self.get_num_from_server())
		q = Decimal(self.pick_q(self.n))
		print "\n\n" , q
		if q > 2 * (self.c**2) and q < 3 * (self.c**2):
			print "YOU KNOW IT BOYYYYY"

		ps, qs = self.get_convergents(self.c/q)
		r = -9999
		for i in range(len(qs)):
			if qs[i] > n:
				r = qs[i-1]

		print "ORDER: " , r

	def pick_q(self, n):
		l = 1
		q = 2**l
		print "n: " , n
		while True:
			if q > 3 * (n**2):
				q = 3*q/4
				continue

			if q > 2 * (n**2):
				return q

			q = 2**l
			l += 1


	def get_num_from_server(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("annai.cs.colorado.edu", 443))
		s.send("123456 " + str(self.exponent) + "\n")

		while True:
			n = s.recv(2048)
			if len(n) > 5:
				return int(n)


	def get_continued_fraction(self, x):
		getcontext().prec = 500
		k = 1
		xk = x
		ans = []
		a = Decimal(math.floor(x))
		while True:
			print "a: " , Decimal(a)
			if (len(str(a)) > 200):
				return ans
			ans.append(a)
			# if Decimal(xk) - Decimal(a) < 1e-12:
			# 	return ans
			remainder = Decimal(xk) - Decimal(a)
			xk = Decimal(1) / remainder
			a = Decimal(1) // remainder
			k += 1

	def get_convergents(self, x):
		p = []
		q = []
		a = self.get_continued_fraction(x)
		index = len(a)
		p.append(a[0])
		p.append(a[0] * a[1] + Decimal(1))
		q.append(1)
		q.append(a[1])

		for i in range(2, index):
			pval = a[i] * p[i-1] + p[i-2]
			qval = a[i] * q[i-1] + q[i-2]
			print "QVAL: " , qval
			if qval > self.c:
				print "ORDER: " , qval
				raw_input()
				return qval
			p.append(pval)
			q.append(qval)

		# print "p: " , p
		# print "q: " , q
		return p[index-1]/q[index-1]

		# return a[i] * self.get_convergents(x, i-1) , a[i] * 


	def simulated_shors():
		print "meow"



# Shors().get_convergents(153.0/53.0)
Shors().run()