money = int(input('Введите сумму ')) #ввод суммы, которую планируем класть под проценты
per_cent = {'TKB':5.6, 'SKB':5.9, 'VTB':4.28, 'SBER':4.0}
TKB = int ((per_cent['TKB'])*(money/100)) #считаем депозит ТКБ
SKB = int ((per_cent['SKB'])*(money/100)) #считаем депозит СКБ
VTB = int ((per_cent['VTB'])*(money/100)) #считаем депозит ВТБ
SBER = int ((per_cent['SBER'])*(money/100)) #считаем депозит Сбера
deposit = [TKB, SKB, VTB, SBER] #порядок вывода дохода
print (deposit) #вывод в заданном порядке дохода
i = max(iter(deposit)) #выбор максимального значения из списка
print (i) #вывод на экран максимально возможной суммы, которую можно заработать