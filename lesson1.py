# first lesson
poem='''I do not like thee, Doctor Fell.
The reason why, I cannot tell.
But this I know, and know full well:
I do not like thee, Doctor Fell.'''
print(poem)
#1
palindrome='A man.\nA plan.\nA canal:\nPanama.'
print(palindrome)
#2
start='Na'* 4+ '\n'
middle='Hey'*3+'\n'
end='Goodbye.'
print(start+start+middle+end)
#3
letters='akjbytdghhhkjkgtdgtrfhjbkjlkjgbhdcgfvh'
print(letters[-1::-1])
a=len(poem)
print("the poem lengh is",str(a))
#4
todos='get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(','))
#5
one_list=['Yeti','Bigfoot','NLO']
second_list=','.join(one_list)
print('Found and signing book deals:',second_list)
print(type(one_list))
#6 split
list1='Зонтик, телефон, ключи, ручка, блокнот'
list2=(list1.split(','))
print(list2)
# join
list3=['Навозный жук', 'Жук майский','Жужелица крымская']
list4='***'.join(list3)
print(list4)
#7
poem2='''Тихо струится река серебристая
В царстве вечернем зеленой весны.
Солнце садится за горы лесистые,
Рог золотой выплывает луны.

Запад подернулся лентою розовой,
Пахарь вернулся в избушку с полей,
И за дорогою в чаще березовой
Песню любви затянул соловей.

Слушает ласково песни глубокие
С запада розовой лентой заря.
С нежностью смотрит на звезды далекие
И улыбается небу земля.'''
print(poem2[0:13])
print(len(poem2))
print(poem2.startswith('Тихо строится река серебристая'))
print(poem2.startswith('Тихо струится река серебристая'))
print(poem2.endswith('небу земля.'))
word='песни'
print(poem2.find(word),poem2.rfind(word),poem2.count(word))
#8
duck='a duck goes into a bar...'
notaduck=duck.replace('duck','marmoset')
print(notaduck)
#9
secondsInMinute = 60
minutesInHour= 60
secondsInHour = secondsInMinute * minutesInHour
HoursInDay=24
secondsInDay=HoursInDay*secondsInHour
print('Секунд в часе:', secondsInHour,'Cекунд в сутках:', secondsInDay)