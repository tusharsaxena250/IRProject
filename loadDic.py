#import IR_GUI as gui
import os

DIR1 = "A:/IR1/New Folder"
DIR2 = "//UTKARSH-1998/IR2"

print(os.scandir(DIR1))

#for roots, dirs, files in os.walk(DIRECTORY):
#    for file in files:
#        print("File = %s" %file)
#    for dir in dirs :
#        if (dir!='Users'): 
#            print("File = %s" %dir)

#roots = next(os.walk(DIR1))[0]
#print("Roots= %s" %roots)

#dirs = next(os.walk(DIR1))[1]
#for d in dirs:
#    dirfiles = next(os.walk(DIR1+"/"+d))[2]
#    print("DIRFiles= %s" %dirfiles)
#print("Directories = %s" %dirs)

#print(gui.BButtons.res)

#def parseDir(directory):
#    dirs = next(os.walk(directory))[1]
#    for d in dirs:
#        dirfiles = next(os.walk(directory+"/"+d))[2]
#        SearchConvertFiles(dirfiles, directory)
#        
#        nextDir = next(os.walk(dirs))[1]
#        if nextDir.size:
#            parseDir(nextDir)
#        else:
#            pass

def SearchConvertFiles():
    global i
     
    files = next(os.walk(DIR1))[2]
    for file in files:
        i = i+1
        f = open(file, "r", encoding='utf8')
        if f:
            contents = f.read()
            
            o = open("file"+str(i)+".txt", "w+", encoding='utf8')
            o.write(contents)
            o.close()
            
            f.close()
            os.remove(file)

i = 2273
            
SearchConvertFiles()

#import urllib.request
#import urllib.parse
#import re
#
#url = 'http://localhost:8000'
#values = {'s':'basics',
#          'submit':'search'}
#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
#req = urllib.request.Request(url, data)
#resp = urllib.request.urlopen(req)
#respData = resp.read()
#
#print(respData)