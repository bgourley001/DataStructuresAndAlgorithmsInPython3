"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
	def __init__(self):
		self.items = []

	def addItem(self, item):
		# add item to items list
		self.items.append(item)

	# python 3 version
	def getClassiness(self):
		classiness = 0
		classiness_dict = {
			'': 0,
			'tophat': 2,
			'bowtie': 4,
			'monocle': 5
		}

		# get classiness sum
		for item in self.items:
			classiness += classiness_dict.get(item, 0)

		return classiness

# Python 2 back compatible version
#	def getClassiness(self):
#		classiness = 0
#		if len(self.items) > 0:
#			for item in self.items:
#				if item == "tophat":
#					classiness += 2
#				elif item == "bowtie":
#					classiness += 4
#				elif item == "monocle":
#					classiness += 5
#		return classiness

# Test cases
me = Classy()

# should be 0
print(me.getClassiness())

# add item to items
me.addItem('tophat')

# should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")

# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())