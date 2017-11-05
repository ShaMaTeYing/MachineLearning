import re
f = open("txtdata.txt","r")
txt = f.read()
f.close()
txt=re.sub('\n',' ',txt)
w = open("output.txt","w")
w.write(txt)
