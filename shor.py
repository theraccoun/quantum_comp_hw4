import socket
import math
from decimal import *

class Shors:

	def __init__(self):
		self.n = 26825926351488399110544112048484691246984742691774090660107762225282840929762385037237484102637951592668796347757856945214753994377357682664648613794306195119897925017866009997263150512915863644811383848031675519987679409974919170391509730554029294470146117971727639921754779476671008586376903725402571129
		self.x = 12345678990029485720954790720389574230985743890257029435704298570234985740295724098572438905743958472083957982043098457042395702934859048527420958720433486742390857304895742390857093485748239574839572049857094385709482375049823572043957823945730429857042938752094570239448573948574230954234985720348573298
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
				return ri
			p.append(pval)
			q.append(qval)

		return False


	def simulated_shors():
		print "meow"



# Shors().get_convergents(153.0, 53.0)
Shors().run()