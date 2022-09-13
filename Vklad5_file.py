#Подключаем дополнительные модули
import sys

# Создаем файл для записи
file3 = open(r"E:\Python_code\RESULT_VKLAD.txt", "w+")

# Этап ввода данных

print('Введите исходные данные \n ')

# Создаем функцию для выполнения проверки на ввод  
# отрицательного значения 

def input_check(text, limit):
	while True:
		value = float(input(text))
		if( value>limit ): 
			break
		print('Ввели неправильное значение, Значение должно быть больше', limit)
		while True:
			answer = input('Продолжить ввод данных? (да/нет): ').lower()
			if (answer == 'нет' or answer == 'н'):
				sys.exit()
			if (answer == 'да' or answer == 'д'):
				break
	return value		

# Присвоение значения основным элементам для расчета

summ = input_check('Укажите сумму вклада (руб) -> ',10000)
srok = input_check('Укажите срок вклада (месяцев) -> ', 0 )
stavka = input_check('Укажите процетную ставку в год -> ', 1)
dohod_all = 0

# Добавим функции перевода в рубли и копейки

def rub(val1):
	r = int(val1)
	return r

def kop(val2):
	tr = int(val2)
	k = int(round(val2 % tr  * 100, 2))
	return k

# Рассчитаем с учетом капитализации и запишем в файл

print('\nМесяц   |  Сумма вклада         |  Проценты')
print("_"*65+"\n")
file3.write('\nМесяц   |  Сумма вклада         |  Проценты\n')


for i in range(1,(int(srok)+1)):
    dohod_i = summ * stavka/100/12
    dohod_ir = rub(dohod_i)
    dohod_ik = kop(dohod_i)

    dohod_all += dohod_i
    dohod_allr = rub(dohod_all)
    dohod_allk = kop(dohod_all)

    itog_summ_i = dohod_i + summ
    itog_summ_ir = rub(itog_summ_i)
    itog_summ_ik = kop(itog_summ_i)

    print(f'{i:2d}      |  {itog_summ_ir} руб. {itog_summ_ik:2d} коп.  |  {dohod_ir} руб. {dohod_ik} коп.')
    file3.write(f'{i:2d}      |  {itog_summ_ir} руб. {itog_summ_ik:2d} коп.  |  {dohod_ir} руб. {dohod_ik} коп. \n')
    
    summ = itog_summ_i

print("_"*65+"\n")
print(f"Общий доход по вкладу составил:            {dohod_allr} руб. {dohod_allk} коп. ")
print(f"Итоговая сумма по окончанию срока вклада:  {itog_summ_ir} руб. {itog_summ_ik} коп. ")

file3.write("\n"+"_"*65)
file3.write("\nОбщий доход по вкладу составил:           %7d руб. %2d коп. "  %(dohod_allr,dohod_allk))
file3.write("\nИтоговая сумма по окончанию срока вклада: %7d руб. %2d коп. "  %(itog_summ_ir,itog_summ_ik))
	
file3.close()   