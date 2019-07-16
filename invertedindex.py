#import preprocessing

#The directories you want to see files from. Inverted index-ing them. If it is for the same system. Use only one of them. You can also make invert-index files for all the systems by specifing them the DIRn.
DIR1 = "...dest_Folder..." 
# DIR2 = "...dest_Folder..."
# DIR3 = "...dest_Folder..."
# DIR4 = "...dest_Folder..."

def make_inverted(DIR):
    keywords=[]
    for i in range(1707):
        try:
            searchfile = open(DIR+"/freq-t"+str(i+1)+".txt", "r")
        
            for line in searchfile:
                line=line.split(":")
                if line[0] not in keywords:
                    keywords.append(line[0])
            searchfile.close()
        except Exception: pass
    
    ii=open(DIR+"/invertedindex.txt", "a")
    for word in keywords:
        print(word)
        line=word+ " : "
        for i in range(1707):
            try:
                searchfile = open(DIR+"/freq-t"+str(i+1)+".txt", "r")
                for line1 in searchfile:
                    if word in line1:
                        line=line+" file"+str(i+1)+","
                        break
                searchfile.close()
            except Exception: pass
        
        ii.write(line+"\n")
    ii.close()
    

make_inverted(DIR1)
#make_inverted(DIR2)
#make_inverted(DIR3)
#make_inverted(DIR4)
