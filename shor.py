import socket
import math
import fractions
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
		while val != 1 and i < 100:
			val = pow(self.x, ri*i, self.n)
			i += 1

		order = -99999
		if val == 1:
			order = ri * i
			print "ORDER: " , str(ri * i)


	def get_fact(self, order):
		r = pow(self.x, order//2, self.n)
		p = fractions.gcd(r+1, self.n)
		q = fractions.gcd(r-1, self.n)

		print "P= " , p
		print "Q= " , q

		if p*q = self.n:
			print "HELL YEAH"
			return True
		else:
			return False


	def pick_q(self, n):
		q = 1
		while True:
			q *= 2
			if q > 2 * (n**2):
				q = q/4*3
				return q


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



# Shors().get_convergents(153.0, 53.0)
Shors().run()

#p=185364785458718473673869817353794739759759694469944693553023355798714789707935739673967533556179173691389589175669346913473252469328469715353536696692923
#q=144719647181652240174721647397597732469938492358364715975025971438477151847750591521964721639753752085604016951293515964699596161939739753583839452159323


