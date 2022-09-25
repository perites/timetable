import time
from datetime import datetime
from datetime import date


time = datetime(datetime.now().year, datetime.now().month, datetime.now().day)



timetable = {0 : "Даня : Кира , Жабка \nНикита : Диана / Кира " ,
			 1 : "Даня : Англ , Кира / Диана \nНикита : Англ",
			 2 : "Даня : Жабка , Диана \nНикита : Жабка , Уборка",
			 3 : "Даня : Англ , Диана \nНикита : Англ",
			 4 : "Даня : Жабка \nНикита : Кира / Диана ",
			 5 : "Даня : Б , Кира / Диана \nНикита : Уборка , Кира / Диана",
			 6 : "Даня : Кира / Диана \nНикита : Кира / Диана"}



while True:
		
	q = input("Current date(1) or your day(year month day) ? : ")
	if q != "1":
		y,m,d=q.split()
		y = int(y)
		m = int(m)
		d = int(d)
		print(timetable[date(y,m,d).weekday()])
	else:
		print(timetable[time.weekday()])



