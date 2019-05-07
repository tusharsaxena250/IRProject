#import IR_GUI as gui
import os

DIR1 = "/A..."
DIR2 = "/B..."

print(os.scandir(DIR1))

def SearchConvertFiles():
    global i
     
    files = next(os.walk(DIR1))[2]
    for file in files:
        i = i+1
        try:
            f = open(file, "r", encoding='utf8')
            if f:
                contents = f.read()

                o = open("file"+str(i)+".txt", "w+", encoding='utf8')
                o.write(contents)
                o.close()

                f.close()
                os.remove(file)
        except Exception: pass 
i = 0
            
SearchConvertFiles()
