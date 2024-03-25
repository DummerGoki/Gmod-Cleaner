import os,threading,psutil,shutil
from cfg import *
from getpass import getpass
os.system("title Gmod cleaner")
if steam.endswith("/"):
    sfix=""
else:
    sfix="/"
#----------------------------------------------------------------------#.
f1=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/downloadlists/" #|downloadlists -- downloaded server content 
f2=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/downloads/"     #|downloads     -- downloaded server content
f3=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/download/"      #|download      -- downloaded server content
f4=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/data/"          #|data          -- stored addon data
f5=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/cache/"         #|cache         -- Lua/Workshop cache
f6=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/cfg/"           #|cfg           -- configuration
f7=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/settings/"      #|settings      -- configuration
f8=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/cl.db"          #|cl.db         -- SQLite database
f9=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/sv.db"          #|sv.db         -- SQLite database
fy=f"{steam}{sfix}steamapps/common/GarrysMod/garrysmod/mn.db"          #|mn.db         -- SQLite database
#----------------------------------------------------------------------#'



#here is the hl2.exe basicly just for starting gmod
__main__=f"{steam}/steamapps/common/GarrysMod/hl2.exe"
lg="""
   _____         _____ _                            
  / ____|       / ____| |                           
 | |  __ ______| |    | | ___  __ _ _ __   ___ _ __ 
 | | |_ |______| |    | |/ _ \/ _` | '_ \ / _ \ '__|
 | |__| |      | |____| |  __/ (_| | | | |  __/ |   
  \_____|       \_____|_|\___|\__,_|_| |_|\___|_|   
                                                    """
print(lg)
print("#------------------------------------------------------------#")

def remove_files():
    pid=[]
    for p in psutil.process_iter(['pid', 'name']):
        if (str(p.info['name'])=="gmod.exe" or str(p.info['name'])=="hl2.exe"):
            pid.append(p.info['pid'])
    if pid==[]:
        pass
    else:
        for i in pid:
            os.kill(i, 9)

    threads=[]
    def dx(FX):
        error=False
        if (os.path.exists(FX)==True):
            if (os.path.isfile(FX)==True):
                try:
                    os.remove(FX)
                except:
                    error=True
                icon="📄"
            elif (str(FX).endswith("cfg/") or str(FX).endswith("settings/")):
                try:
                    shutil.rmtree(FX)
                except:
                    error=True
                icon="⚙️"
            else:
                try:
                    shutil.rmtree(FX)
                except:
                    error=True
                icon="📂"
            if (os.path.exists(FX)==False and error==False):
                print(f"{icon}  ✅\033[0;92m {str(FX).replace(f'{steam}{sfix}steamapps/common/GarrysMod/garrysmod/','')}\033[0m")
            if (os.path.exists(FX)==True and error==False or os.path.exists(FX)==False and error==True):
                print(f"{icon}  ⚠️\033[0;93m {str(FX).replace(f'{steam}{sfix}steamapps/common/GarrysMod/garrysmod/','')}\033[0m")
            if (os.path.exists(FX)==True and error==True):
                print(f"{icon}  ❌\033[0;91m {str(FX).replace(f'{steam}{sfix}steamapps/common/GarrysMod/garrysmod/','')}\033[0m")
        else:
            print(f"📄  ⚠️\033[0;93m {str(FX).replace(f'{steam}{sfix}steamapps/common/GarrysMod/garrysmod/','')} Does not exist!\033[0m")

    threads.append(threading.Thread(target=dx,args=[f1]))
    threads.append(threading.Thread(target=dx,args=[f2]))
    threads.append(threading.Thread(target=dx,args=[f3]))
    threads.append(threading.Thread(target=dx,args=[f4]))
    threads.append(threading.Thread(target=dx,args=[f5]))
    if (config==1):
        threads.append(threading.Thread(target=dx,args=[f6]))
        threads.append(threading.Thread(target=dx,args=[f7]))
    else:
        pass
    threads.append(threading.Thread(target=dx,args=[f8]))
    threads.append(threading.Thread(target=dx,args=[f9]))
    threads.append(threading.Thread(target=dx,args=[fy]))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    if (start==1):
        os.startfile(__main__)
    else:
        pass
remove_files()
getpass("Press Enter to close the Program:\n")