import socket
import math
from decimal import *

class Shors:

	def __init__(self):
		self.n = 26825926351488399110544112048484691246984742691774090660107762225282840929762385037237484102637951592668796347757856945214753994377357682664648613794306195119897925017866009997263150512915863644811383848031675519987679409974919170391509730554029294470146117971727639921754779476671008586376903725402571129
		self.x = 1234567899002948572095479072038957423098574389025702943570429857023498574029572409857243890574395847208395798204309845704239570293485904852742095872043348674239085730489574239085709348574823957483957204985709438570948237504982357204395782394573042985704293875209457023944857394857423095423498572034857329
		self.exponent = 2048
		# self.exponent = int(2 * math.log(self.n, ))

	def run(self):
		self.c = Decimal(self.get_num_from_server())
		q = Decimal(self.pick_q(self.n))
		print "\n\n" , q
		if q > 2 * (self.n**2) and q < 3 * (self.n**2):
			print "YOU KNOW IT BOYYYYY"
		else:
			print "BADDDD"
			raw_input()

		print "Q: " , len(str(q))
		print "C: " , len(str(self.c))
		ps, qs = self.get_convergents(self.c, q)
		r = -9999
		for i in range(len(qs)):
			if qs[i] > n:
				r = qs[i-1]

		print "ORDER: " , r

	def pick_q(self, n):
		l = 1
		while True:
			q = 2**l
			if q > 3 * (n**2):
				q = q/4*3
				continue

			if q > 2 * (n**2):
				return q

			l += 1


	def get_num_from_server(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("annai.cs.colorado.edu", 443))
		s.send(str(self.x) + " " + str(self.exponent) + "\n")

		while True:
			c = s.recv(2048)
			if len(c) > 5:
				print c
				raw_input()
				return c


	def get_continued_fraction(self, num, denom):
		getcontext().prec = 500
		num = long(num)
		denom = long(denom)
		ans = []
		while denom > 0:
			print "num: " , num
			print "denom: " , denom
			a = num // denom
			if denom != 0:
				ans.append(a)
				print "ans: " , ans
				raw_input()
 
 			print num
 			print a
 			remain = num - (denom * a)
			num = denom
			denom = remain

	def get_convergents(self, num, denom):
		a = self.get_continued_fraction(num, denom)
		p = []
		q = []
		index = len(a)
		p.append(a[0])
		p.append(a[0] * a[1] + Decimal(1))
		q.append(1)
		q.append(a[1])

		for i in range(2, index):
			pval = a[i] * p[i-1] + p[i-2]
			qval = a[i] * q[i-1] + q[i-2]
			print "QVAL: " , qval
			print self.c
			if qval > self.n:
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



Shors().get_convergents(153.0, 53.0)
# Shors().run()