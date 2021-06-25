class New():
  def __init__(self,title: str, day: int, month: int ,year: int = 2021):
    self.title=title
    if day<10:
      newday="0"+str(day)
    else:
      newday=str(day)
    if month<10:
      newmonth="0"+str(month)
    else:
      newmonth=str(month)
    self.date=newmonth+"/"+newday+"/"+str(year)
    self.place="Santiago, Chile"
    self.text=""
    self.tags=[]
  def tag(self, text: str):
    try:
      self.tags.append(text)
    except:
      print("A tagging bug was happen")
  def format(self):
    t="### "+self.title+"\n#### "+self.date+" "+self.place
    t+="\n##### Tags: "
    try:
      for i in self.tags:
        t+="["+i+"](https://github.com/topics/"+i+")"
    except:
      pass
    t+="\n"+self.text
    return t
  def add(self):
    try:
      T=self.format()
      try:
        f=open("README.md","a")
        f.write(T)
        f.close()
        print("New added succesfully")
        print("Title: "+self.title)
        print("Date: "+self.date)
        print("Content: "+self.text)
      except:
        print("A writting bug was happen")
    except:
      print("A formatting bug was happen")
    
