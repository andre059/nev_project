from datetime import date

the_date = date(2027, 10, 5)
date_formatted = the_date.strftime("%d %B of %Y")

print(date_formatted)