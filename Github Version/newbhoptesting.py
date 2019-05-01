import keyboard
import pymem
import pymem.process
import time
import sys

dwForceJump = (0x5188988) #offsets updated 4/27/19
dwLocalPlayer = (0xCD4774)
m_fFlags = (0x104)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll

five = 5
while five == 5:
    def Bhop():
        print("Where's my phoon? Thanks Snaacky for the code as starting point. Working from here.")

    while True:
        try:
            player = pm.read_int(client + dwLocalPlayer)
            force_jump = client + dwForceJump
            on_ground = pm.read_int(player + m_fFlags)

            if keyboard.is_pressed("space"):
                if on_ground == 257: #on ground
                    pm.write_int(force_jump, 5)
                    time.sleep(0.17)
                    pm.write_int(force_jump, 4)
            time.sleep(0.002)
            if keyboard.is_pressed("space"):
                if on_ground == 263: #on ground crouched
                    pm.write_int(force_jump, 5)
                    time.sleep(0.17)
                    pm.write_int(force_jump, 4)
            time.sleep(0.002)
        except pymem.exception.MemoryReadError:
            pass


if __name__ == 'Bhop':
    main()




#To do,
# 1) More bhopping options, ie when crouch done 4/21/19
# 2) Triggerbot
# 3) ESP?
