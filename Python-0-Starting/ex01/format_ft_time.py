import time
import datetime

currtime = time.time()
print(f"Seconds since January 1, 1970: {currtime:,.4f} or {currtime:.2e} in \
scientific notation")

now = datetime.date.today()
print(now.strftime("%b %d %Y"))
