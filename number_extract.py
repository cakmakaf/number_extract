



Assume that we have list of strings such \as

{321","ahmet","1983afc","25","python"}

We will extract only the number out of this list







Mylist = ["321","ahmet","1983afc","25","python"]

for entry in Mylist:
    
    try: 
        entry = int(entry) 
        print(entry)
    except:
        pass 

