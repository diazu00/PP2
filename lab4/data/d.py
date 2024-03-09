import datetime

date1 = datetime.datetime(2023, 2, 20, 17, 50, 0)
date2 = datetime.datetime(2023, 2, 20, 17, 58, 0)

diff_in_seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", diff_in_seconds)