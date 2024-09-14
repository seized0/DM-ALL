# MADE BY uhq.s
# discord.gg/xhell


import requests
import colorama
from colorama import Fore
import time
import os
import fade

def dmall():
    os.system('cls')
    print(fade.water(text=r"""

 ________   ___      ___           __      ___      ___       
|"      "\ |"  \    /"  |         /""\    |"  |    |"  |      
(.  ___  :) \   \  //   |        /    \   ||  |    ||  |      
|: \   ) || /\\  \/.    |       /' /\  \  |:  |    |:  |      
(| (___\ |||: \.        |      //  __'  \  \  |___  \  |___   
|:       :)|.  \    /:  |     /   /  \\  \( \_|:  \( \_|:  \  
(________/ |___|\__/|___|    (___/    \___)\_______)\_______)    Made By uhq.s 
                                                              
                        discord.gg/xhell
"""))
    token = input(Fore.CYAN + '🐬 TOKEN ACCOUNT : ')  
    message = input(Fore.CYAN +'🐬 MESSAGE : ')

    headers = {
        'Authorization': token
    }
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
    
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/{channel["id"]}/messages',headers=headers,json={"content": message})  
            print(f"{Fore.LIGHTBLUE_EX}[ 🐬 ] ID: {channel['id']}")
            time.sleep(0.7)
        except Exception as e:
            print(f"ERROR :  {e}")
dmall()

