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