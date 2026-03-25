import random
from datetime import datetime, timedelta
def g_date():
    A = datetime.today()
    s_date = A - timedelta(days=5*365)
    s_days = random.randint(0, (A - s_date).days)
    return s_date + timedelta(days=s_days)
dates = [str(g_date().date()) for _ in range(10)]
date_f = "%Y-%m-%d"
dates.sort()
for i in range(len(dates) - 1):
    date_s1 = dates[i]
    date_s2 = dates[i + 1]
    date1 = datetime.strptime(date_s1, date_f)
    date2 = datetime.strptime(date_s2, date_f)
    days_d = abs((date2 - date1).days)
    print(f"Разница между {date_s1} и {date_s2}: {days_d} дней")
