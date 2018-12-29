#### OBJECTS

## Define
class Square(object):
	def __init__(self, length):
		self.length = length
	def area(self, length):
		print('Square area is: ' + str(self.length**2))
	def perimeter(self, length):
		print('Square perimeter is: '+str(4*self.length))
	
class Cube(Square):
	def volume(self, length):
		print('Cube volume is: '+ str(self.length**3))
	def perimeter(self, length):
		print('Cube perimeter is: '+ str(12*self.length))
		
## Start
while True:
	while True:
		try:
			length = float(raw_input('Introduce length: '))
			break
		except ValueError:
			print('Length must be a real number')
	while True:
		print('Current length: '+ str(length))
		main = raw_input('Chose one \n [s] Square, [c] Cube, [e] Exit, [n] New length \n Input: ')
		if main == 'e' or main == 'n':
			break
		elif main == 's':
			while True:			
				option = raw_input('Chose one \n [a] Area, [p] Perimeter, [c] Cancel \n Input: ')
				s = Square(length)
				if option == 'a':
					o = s.area(s.length)
					break
				elif option == 'p':
					o = s.perimeter(s.length)
					break
				elif option == 'c':
					break
				else:
					print('Choose one of the available options.')
		elif main == 'c':
			while True:
				option = raw_input('Chose one \n [v] Volume, [p] Perimeter, [c] Cancel \n Input: ')
				c = Cube(length)
				if option == 'v':
					o = c.volume(c.length)
					break	
				elif option == 'p':
					o = c.perimeter(c.length)
					break
				elif option == 'c':
					break
				else:
					print('Choose one of the available options.')
		else:
			print('Choose one of the available options.')
		while True:
			option = raw_input('Chose one \n [c] Calculation Menu [n] New length \n Input:')
			if option != 'c' and option != 'n':
				print('Choose one of the available options.')
			else:
				break
		if option == 'n':
			break
	if main == 'e':
		break
