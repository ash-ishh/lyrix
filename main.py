import urllib.request
import re


song = input('Song Name? (singforthemoment)\n')
artist = input('Artist Name? (eminem)  \n')

url="http://www.azlyrics.com/lyrics/"+artist+"/"+song+".html"

try:
 req = urllib.request.urlopen(url)
 data = str(req.read()) #full_webpage
except:
 abc = input('Not Found! Close and Try Again')

path = open('/sdcard/lyrics/test.txt','w')
path.write(data)
path.close()
#^full webpage to test.txt

path = open('/sdcard/lyrics/test.txt','r')
loc = '/sdcard/lyrics/'+song+'.html'
path1 = open(loc,'w')
#^Creating file for sorted data


#↓HTML tags in it
path1.write('''
<html>
<style type="text/css">
body {
background-color:#51caf2;
color:white
}


</style>

<body>
''')
path1.close()


lyrics = re.findall(r'<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->(.{1,})<form id="addsong"',path.read())
lyrics = lyrics[0]
#Relacing \n \r n \
lyrics_newline = lyrics.replace("\\n","<br />")
lyrics_slash = lyrics_newline.replace("\\","")
lyrics_final = lyrics_slash.replace("\\r","")

path1 = open(loc,'a')
head = song+" BY "+artist+"<br />"
head = head.upper()
path1.write(head)
path1.write(lyrics_final)
path1.write('''
</body>
</html>
'''
)
path1.close()

print("Done :) Check the lyrics Folder!")
