#----------------------------------------
#just functions reaused in various files
#----------------------------------------

from datetime import date

def current_date():
	return date.today().strftime("%d.%m.%Y")
