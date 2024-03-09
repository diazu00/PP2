import datetime

cur_date = datetime.date.today()

new_date = cur_date - datetime.timedelta(days=5)

print("Current date:", cur_date)
print("Five days ago:", new_date)