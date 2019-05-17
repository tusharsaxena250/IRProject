DIR1 = "--your directory locations--"
DIR2 = "--your directory locations--"
DIR3 = "--your directory locations--"
DIR4 = "--your directory locations--"

def search_word(word):
    file=open(DIR1+"/invertedindex.txt","r") #call for all the directories you wanna parse through
    for line in file:
        line = line.split(":")
        if word in line[0]:
            l = line[1].split(",")
            for i in l:
                print(DIR1+"/"+i)
            break
        
    file.close()
    
    file=open(DIR2+"/invertedindex.txt","r") #call for all the directories you wanna parse through
    for line in file:
        line = line.split(":")
        if word in line[0]:
            l = line[1].split(",")
            for i in l:
                print(DIR2+"/"+i)
            break
        
    file.close()
    
    file=open(DIR3+"/invertedindex.txt","r") #call for all the directories you wanna parse through
    for line in file:
        line = line.split(":")
        if word in line[0]:
            l = line[1].split(",")
            for i in l:
                print(DIR3+"/"+i)
            break
        
    file.close()
    
    file=open(DIR4+"/invertedindex.txt","r") #call for all the directories you wanna parse through
    for line in file:
        line = line.split(":")
        if word in line[0]:
            l = line[1].split(",")
            for i in l:
                print(DIR4+"/"+i)
            break
        
    file.close()
    
#word=input("Enter a word : ")
#search_word(word)
