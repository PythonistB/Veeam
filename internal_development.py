import os
import hashlib
import time

d1 = 'C:\\Users\\user\\Desktop\\Source\\file.txt'
d2 = 'C:\\Users\\user\\Desktop\\Replica\\file.txt' 

if os.path.exists("C:\\Users\\user\\Desktop\\Source\\file.txt") and os.path.exists("C:\\Users\\user\\Desktop\\Replica\\file.txt"):
     print('The files exist')
else:
     os.removedirs("C:\\Users\\user\\Desktop\\Source")
     os.removedirs("C:\\Users\\user\\Desktop\\Replica")

if d1 != os.path.exists("C:\\Users\\user\\Desktop\\Source\\file.txt") and d2 != os.path.exists("C:\\Users\\user\\Desktop\\Replica\\file.txt"):   
     d3 = os.mkdir( "C:\\Users\\user\\Desktop\\Source"); 
     d4 = os.mkdir( "C:\\Users\\user\\Desktop\\Replica"); 
    
if os.open(d1, os.O_CREAT):
    fd1 = os.open(d1, os.O_RDWR)
if os.open(d2, os.O_CREAT):  
    fd2 = os.open(d2, os.O_RDWR)

def compare(first_file, second_file):
      with open(first_file, 'rb') as f1:
            with open(second_file, 'rb') as f2:
                  if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
                      return True
                  else:
                      return False
    
str = b"Implemented  program that synchronizes two folders: source and replica wich in the both of folders contains file.txt"
os.write(fd1, str)
os.write(fd2, str)

print("Executed successfully")

while True :
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'File updating each 3 seconds [{now}] ')
        time.sleep(3)
        continue              