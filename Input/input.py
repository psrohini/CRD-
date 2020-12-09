import time


d={} # 'd' empty dictionary

#create data operation

def createdata(key,value,ttl=0): #perform creation of key value pair
    if key in d:
        print("key already exists.Error") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):  #file size less than 1 gb and jason less than 16 kb
                if ttl == 0:
                    a = [value,ttl]
                else:
                    a = [value, time.time()+ttl]
                if len(key) <= 32:  #key name should be greater than or equal to 32 chars
                    d[key] = a
            else:
                print("Memory limit exceeded.Error")
        else:
            print("Invalid key.Error")  #key name must contain only alphabets and no numbers or special characters





#read data operation

def readdata(key):  #perform readdata operation
    if key not in d:
        print("Enter a valid key, Key doesn't exist in database") #key does'nt exist in database
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:  #compare 
                string = str(key)+":"+str(b[0])  #jason object format "key:value"
                return string
            else:
                print("Time to live of",key,"has expired")
        else:
            string = str(key)+":"+str(b[0])
            return string





#delete data operation

def deletedata(key):  #perform deletedata operation
    if key not in d:
        print("Enter a valid key. Key doesn't exist in database")  #key doesn't exist in database
    else:
        b = d[key]
        if b[1] != 0:
            if time.time() < b[1]:  #compare
                del d[key]
                print("Key deleted successfully")
            else:
                print("Time to live of",key,"has expired")
        else:
            del d[key]
            print("Key deleted successfully")

