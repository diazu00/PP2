import datetime

today = datetime.date.today()
yest = today - datetime.timedelta(days=1)
tmw = today + datetime.timedelta(days=1)

print("Yesterday:", yest)
print("Today:", today)
print("Tomorrow:", tmw)