# coding: utf-8
# схема связей аббревиатур с названиями стран
countries = {	u'Россия': 'RU',
	u'Германия': 'DE',
	u'Франция': 'FR',
	u'Китай': 'CN',
	u'Япония': 'JP'
}
# создание базового набора стран и некоторых городов в них
cities = {	'FR': u'Париж',
	'JP': u'Токио',
	'DE': u'Дрезден'
}
# добавление некторых городов
cities['CN'] = u'Шанхай'
cities['RU'] = u'Москва'
# вывод некоторых городов
print '- ' * 10
print u'В стране CN есть город', cities['CN']
print u'В стране RU есть город', cities['RU']
# вывод некоторых стран
print '- ' * 10
print u'Аббревиатура Китая: ', countries[u'Китай']
print u'Аббревиатура России: ', countries[u'Россия']
# выполняется с учётом страны и словаря городов
print '- ' * 10
print u'В Китае есть город: ', cities[countries[u'Китай']]
print u'В Германии есть город: ', cities[countries[u'Германия']]
# вывод абревиатур всех стран
print '- ' * 10
for country, abbrev in countries.items():
	print u'%s имеет аббревиатуру %s' % (country, abbrev)
# вывод всех городов в странах
print '- ' * 10
for abbrev, city in cities.items():
	print u'В стране %s, есть город: %s' % (abbrev,city)
# а теперь сразу оба типа данных
print '- ' * 10
for country, abbrev in countries.items():
	print u'В стране %s с аббревиатурой %s есть город %s' % (country, abbrev, cities[abbrev])
print '- ' * 10
# безопасное получение аббревиатуры страны, которая не предствлена
country = countries.get(u'США', None)
if not country:
	print u'Прошу прощения, США не обнаружено.'
# получение города со значеним по умолчанию
city = cities.get('US', u'не существует')
print u'В стране "US" есть город: %s' % city