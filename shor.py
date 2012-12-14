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
		self.c = self.get_num_from_server()
		q = self.pick_q(self.n)

		ri = self.get_convergents(self.c, q)

		val = pow(self.x, ri, self.n)
		i = 1
		while val != 1 and i < 1024:
			val = pow(self.x, ri*i, self.n)
			i += 1

		if val == 1:
			print "ORDER: " , str(ri * i)
		
		

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
			a = num // denom
			if denom != 0:
				ans.append(a)
 
 			remain = num - (denom * a)
			num = denom
			denom = remain

		return ans

	def get_convergents(self, num, denom):
		a = self.get_continued_fraction(num, denom)
		print "a: " , a
		raw_input()
		p = []
		q = []
		index = len(a)
		p.append(a[0])
		p.append(a[0] * a[1] + 1)
		q.append(1)
		q.append(a[1])

		for i in range(2, len(a)):
			pval = a[i] * p[i-1] + p[i-2]
			qval = a[i] * q[i-1] + q[i-2]
			if qval > self.n:
				ri = q[i-1]
				print "ri: " , ri
				raw_input()
				return ri
			p.append(pval)
			q.append(qval)

		return False


	def simulated_shors():
		print "meow"



# Shors().get_convergents(153.0, 53.0)
Shors().run()