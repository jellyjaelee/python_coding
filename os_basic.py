import os
from datetime import datetime

os.getcwd()

mod_time = os.stat("class.py").st_mtime

print(datetime.fromtimestamp(mod_time))
