import datetime

cur_datetime = datetime.datetime.now()
new_datetime = cur_datetime.replace(microsecond=0)

print("Current datetime:", cur_datetime)
print("New datetime:", new_datetime)