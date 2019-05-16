# coding: utf-8

people = 30
cars = 40
buses = 15

if cars > people:
	print u'train a car'
elif cars < people:
	print u'no train car'
else:
	print u'we dont choose'

if cars > buses:
	print u'too many bases'
elif cars < buses:
	print u'go to the bus'
else:
	print u'we dont choose again'

if people > buses:
	print u'ok, train the bus'
else:
	u'fine, stay at home'