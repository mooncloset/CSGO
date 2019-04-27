import keyboard
import pymem
import pymem.process
import time
import sys
from multiprocessing import Process
from Wallhack import wallhack
from newbhoptesting import bhop
#added 4/21/19
dwForceJump = (0x5188988) #offsets updated 4/27/19
dwLocalPlayer = (0xCD4774)
m_fFlags = (0x104)
dwEntityList = (0x4CE54EC) #for wallhack
dwGlowObjectManager = (0x5225718)
m_iGlowIndex = (0xA3F8)
m_iTeamNum = (0xF4) #end wallhack

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll
print("Hit")
one = 1
while one == 1:
    def main():
        def BhopPortion():
            newbhoptesting.bhop()
            print ("BhopPortion Loaded")
        def WallhackPortion():
            Wallhack.wallhack()
            print ("WallhackPortion Loaded")


#end
    if __name__ == 'main':
        p1 = Process(target=BhopPortion)
        p1.start()
        p2 = Process(target=WallhackPortion)
        p2.start()
        main()
