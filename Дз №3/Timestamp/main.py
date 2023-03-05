import time

timestamp = int(time.time())
years = 0
month = 0
days = -1
hours = 0
minutes = 0
seconds = 0
key = 2

while timestamp > 0:  # перевод timestamp в года, месяцы, дни и тд.
    if key != 4:
        if timestamp >= 31536000:  # не високосный год
            timestamp -= 31536000
            years += 1
            key += 1
        elif timestamp >= 86400:
            timestamp -= 86400
            days += 1
        elif timestamp >= 3600:
            timestamp -= 3600
            hours += 1
        elif timestamp >= 60:
            timestamp -= 60
            minutes += 1
        elif timestamp >= 1:
            timestamp -= 1
            seconds += 1
    else:
        if timestamp >= 31622400: # не високосный год
            timestamp -= 31622400
            years += 1
            key = 0
        elif timestamp >= 86400:
            timestamp -= 86400
            days += 1
        elif timestamp >= 3600:
            timestamp -= 3600
            hours += 1
        elif timestamp >= 60:
            timestamp -= 60
            minutes += 1
        elif timestamp >= 1:
            timestamp -= 1
            seconds += 1

if days <= 31:
    month = 1
elif days <= 59 and key != 4: # не високосный год
    month = 2
    days -= 31
elif days <= 90 and key != 4:
    month = 3
    days -= 59
elif days <= 120 and key != 4:
    month = 4
    days -= 90
elif days <= 151 and key != 4:
    month = 5
    days -= 120
elif days <= 181 and key != 4:
    month = 6
    days -= 151
elif days <= 212 and key != 4:
    month = 7
    days -= 181
elif days <= 243 and key != 4:
    month = 8
    days -= 212
elif days <= 273 and key != 4:
    month = 9
    days -= 243
elif days <= 304 and key != 4:
    month = 10
    days -= 273
elif days <= 334 and key != 4:
    month = 11
    days -= 304
elif days <= 365 and key != 4:
    month = 12
    days -= 334
elif days <= 60 and key == 4:  # високосный год
    month = 2
    days -= 31
elif days <= 91 and key == 4:
    month = 3
    days -= 60
elif days <= 121 and key == 4:
    month = 4
    days -= 91
elif days <= 152 and key == 4:
    month = 5
    days -= 121
elif days <= 182 and key == 4:
    month = 6
    days -= 152
elif days <= 213 and key == 4:
    month = 7
    days -= 182
elif days <= 244 and key == 4:
    month = 8
    days -= 213
elif days <= 274 and key == 4:
    month = 9
    days -= 244
elif days <= 305 and key == 4:
    month = 10
    days -= 274
elif days <= 335 and key == 4:
    month = 11
    days -= 305
elif days <= 366 and key == 4:
    month = 12
    days -= 335

years += 1970
hours += 4  # перевод в наш часовой пояс

if month < 10:  # редактирование отображения
    months = "0" + str(month)
if days < 10:
    days = "0" + str(days)
if hours < 10:
    hours = "0" + str(hours)
if hours == 24:
    hours = "00"
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
    
print(f"{years} - {months} - {days} \n{hours} : {minutes} : {seconds}")
