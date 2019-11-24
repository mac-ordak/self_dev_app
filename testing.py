#-----------------------------------------
#here I am just testing if it all works...
#-----------------------------------------

from main import Users, Goals, Daily_stats
from database_app import create_stats_table, create_entry, update_entry
#from gui import *

x = Daily_stats(77, 5300, 1800)

# print(x.date)
# print(x.weight)
# print(x.steps)
# print(x.kcals)
# print(type(x.date))

create_stats_table("new_database", "test_table", "id", "n2", "n3", "n4")

create_entry("new_database", "test_table", x, "id", "n2", "n3", "n4", "id", x.date)
