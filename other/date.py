from datetime import datetime

now = datetime.now()
print(f"{now.day}/{now.month}/{now.year} {now.strftime("%d/%m/%Y, %H:%M:%S")}")