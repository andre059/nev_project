from datetime import date

thedate = date(1970, 1, 5)

date_formatted = thedate.strftime("%d %B %Y ")  # День Месяц Год

print(date_formatted)
