import datetime

current_date=datetime.datetime.now()
current_datetime=str(datetime.datetime.now()).split()

formatted_date= current_date.strftime('%d %m %Y')
current_time= current_datetime[1]

print(current_time)
print(current_date)