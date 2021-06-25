'''
Just write here:
'''

title="Hello world"
day=24
month=6
tags=["hello-world","uwu"]
content="bienvenido\nuwu"
































































































































































'''
Don't touch this:
'''
#Imports
from resources.news import New
from resources.config import files,year
from resources.utils import clearConsole,sleep
print("Running...")
sleep(10)
clearConsole()

#New
new=New(title,day,month,year,files)
for i in tags:
  new.tag(i)
new.text=content
new.add()