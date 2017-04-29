import os
import time
print(os.getcwd())
os.chdir('C:\\Users\\Sayem\\')
print(os.getcwd())
os.mkdir('os-xmp1')#can't make sub directory
time.sleep(3)#after 3 sec creates directory
os.makedirs('os-xmp2/sub-1.txt')#can make sun directory
os.rmdir()
time.sleep(5)#after 5 sec creates directory
os.removedirs('os-xmp2/sub-1.txt')
print(os.listdir())
print(os.stat('os-xmp2/sub-1.txt'))
from datetime import datetime
mod_time = os.stat('os-xmp2/sub-1.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
