#import preprocessing
def make_inverted():
    keywords=[]
    for i in range(2572):
        try:
            searchfile = open("A:/IR1/F5000/New Folder/freq-t"+str(i+1)+".txt", "r")
        
            for line in searchfile:
                line=line.split(":")
                if line[0] not in keywords:
                    keywords.append(line[0])
            searchfile.close()
        except Exception: pass
    
    ii=open("A:/IR1/F5000/New Folder/invertedindex.txt", "a")
    for word in keywords:
        print(word)
        line=word+ " : "
        for i in range(2572):
            try:
                searchfile = open("A:/IR1/F5000/New Folder/freq-t"+str(i+1)+".txt", "r")
                for line1 in searchfile:
                    if word in line1:
                        line=line+" file"+str(i+1)+","
                        break
                searchfile.close()
            except Exception: pass
        
        ii.write(line+"\n")
    ii.close()

def search_word(word):
    file=open("A:/IR1/F5000/New Folder/invertedindex.txt","r")
    for line in file:
        line = line.split(":")
        if word in line[0]:
            print(line[1])
            break
        
    file.close()
    
#word=input("Enter a word : ")
#search_word(word)