import win32api
import win32gui
import win32process
import pymem
import sys
import os

dwEntityList = (0x4CE54EC) #for wallhack
dwGlowObjectManager = (0x5225718)
m_iGlowIndex = (0xA3F8)
m_iTeamNum = (0xF4) #end wallhack

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll

F6=win32api.GetKeyState(0x75)
while(win32api.GetKeyState(0x75)==F6):
    def wallhack():
        print("ESP on.")

    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)

        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow


    if __name__ == 'Wallhack':
        main()
