#lesson2
#1 Списки
list1=[]
weekdays=['Monday','Tuesday','Wensday','Thuersday','Friday','Saturday','Sanday']
big_birds=['emu','ostrich','cassowary']
first_names=['Graham','John','Terry','Terry','Michael']
print('Имя "Terry" встречается в списке - ', first_names.count('Terry'), 'раз(а)')
#2
list2=list('cat')
print(list2)
list3=('cat','vitamins','umbrella')
list4=(list(list3))
print(list4)
#3
birthday='1/6/1952'
print(birthday.split('/'))
print('***'.join(birthday))
print(weekdays[0])
print(weekdays[0:5])
print(weekdays[-1::-1])
weekdays[4]='Пятница'
print(weekdays)
print(weekdays[0:2])
#4 .append
big_birds.append('albatross')
print(big_birds)
other_big_birds=['black volture','emperor penguin']
big_birds += other_big_birds
print(big_birds)
big_birds.insert(0,'andean condor')
print(big_birds)
big_birds.remove('andean condor')
print(big_birds)
print(big_birds.index('albatross'))
print('Находится ли "альбатрос" в списе -','albatross' in big_birds)
# Сортировка
numbers=[5, 99, 24, 34, 63, 12]
numbers.sort()
print('Отсортированные значения:', numbers)
numbers.sort(reverse=True)
print('Отсортированные значения по убыванию:', numbers)
sorted_dayweeks=sorted(weekdays)
print(sorted_dayweeks)
print(len(weekdays))
#
old_numbers=numbers.copy()
print(old_numbers)
#Кортежи
marx_tuple='Groucho','Chico','Harpo'
print(marx_tuple)
# tuple
marx_list=['Groucho','Chico','Harpo']
print(tuple(marx_list))
#Словарь
empty_dict={}
print(empty_dict)
#
lol=[['a','b'],['c','d'],['e','f']]
print('Преобразование в словарь:',dict(lol))
#Список, содержащий двухэлементныйе кортежи
lot=[('a','b'),('c','d'),('e','f')]
print(dict(lot))
#Кортеж, включающий двухэлемнтные строки
tol=(['a','b'],['c','d'],['e','f'])
print(dict(tol))
#Список, содержащий двухэлементные строки 
los=['ab','cd','ef']
print(dict(los))
#Кортеж, содержащий двухсимвольные строки
tos=('ab','bc','ef')
print(dict(tos))
#Объединение словарей
firstNames='Chapman','Cleese','Gilliam','Idle','Jones','Palin'
surnames='Graham','John','Terry','Eric','Terry','Michael'
dictionary_of_pythons=dict(zip(surnames,firstNames))
print('Словарь из ключей-фамилий и имён-значений:\n',dictionary_of_pythons)
print(dictionary_of_pythons['John'])
otherNames='Groucho','Moe'
otherSurnames='Marx','Howard'
otherPeople=(dict(zip(otherSurnames,otherNames)))
print('Список комиков: \n', otherPeople)
dictionary_of_pythons.update(otherPeople)
print('Cписок всех людей:\n', dictionary_of_pythons)
#
del dictionary_of_pythons ['Marx']
print(dictionary_of_pythons)
del dictionary_of_pythons ['Howard']
print(dictionary_of_pythons)
print('Terry' in dictionary_of_pythons)
print(dictionary_of_pythons['John'])
#
years_list=['1995','1996','1997','1998','1999','2000']
third_birthday=years_list[3]
print('Моё третье ДР было в этом году -', third_birthday)
last_year=years_list[5]
print('Из перечисленных годов, старше я была в этом -', last_year)
things=['mazzarella','cinderella','salmonella']
things.remove('cinderella')
things.insert(1,'Cinderella')
print('Золушка в списке с большой буквы',things)
things.remove('salmonella')
things.insert(2,'SALMONELLA')
print('Теперь сальмонелла капсом',things)
del things [2]
print('Список без сальмонеллы',things)
surprise='Groucho','Chico','Harpo'
surprise_list=list(surprise)
print(surprise_list)
surprise_list[2]='harpo'
print('Последнее имя с маленькой буквы', surprise_list)