import os, time, sys

if not os.geteuid() == 0:
    sys.exit("""\033[1;91m\n[!] Wifi Spam must be run as root. \n\033[1;m""")
os.system('clear')

print('''\033[1;36m__          ___  __ _  _____                       
\ \        / (_)/ _(_)/ ____|                      
 \ \  /\  / / _| |_ _| (___  _ __   __ _ _ __ ___  
  \ \/  \/ / | |  _| |\___ \| '_ \ / _` | '_ ` _ \ 
   \  /\  /  | | | | |____) | |_) | (_| | | | | | |
    \/  \/   |_|_| |_|_____/| .__/ \__,_|_| |_| |_|
                            | |                    
                            |_|                    \033[1;m''')
print('\n\033[1;36mCreator: Mrva (@_mrvic_)\n\033[1;m')
print('''\033[1;91mOptions:
[1] wlan0
[2] wlan1\033[1;m''')
y = input('\033[1;91mEnter number: \033[1;m')
if "1" in y:
	print('Configuring the adapter...')
	os.system('airmon-ng start wlan0')
	time.sleep(3)
	os.system('clear')
	print('''\033[1;36m__          ___  __ _  _____                       
\ \        / (_)/ _(_)/ ____|                      
 \ \  /\  / / _| |_ _| (___  _ __   __ _ _ __ ___  
  \ \/  \/ / | |  _| |\___ \| '_ \ / _` | '_ ` _ \ 
   \  /\  /  | | | | |____) | |_) | (_| | | | | | |
    \/  \/   |_|_| |_|_____/| .__/ \__,_|_| |_| |_|
                            | |                    
                            |_|                    \033[1;m''')
	print('\n\033[1;36mCreator: Mrva (@_mrvic_)\n\033[1;m')	
	print('''\033[1;91mOptions:
	[1] Random spam
	[2] Create your spam\033[1;m''')
	x = input('\033[1;91mSelect an option: \033[1;m')
	if "1" in x:	
		time.sleep(1)
		print('\033[32m[+] Spam is running !!!\033[32m')
		print('\033[32m[+] Press Ctrl + C to stop spam.\033[32m')
		os.system('mdk3 wlan0mon b -c 2 -s 10000')
	if "2" in x:
		time.sleep(1)
		print('\033[32m[+] Spam is running !!!\033[32m')
		print('\033[32m[+] Press Ctrl + C to stop spam.\033[32m')	
		os.system('mdk3 wlan0mon b -c 2 -f /home/kali/WifiSpam/MySpam.txt')
if "2" in y:
	print('Configuring the adapter...')
	os.system('airmon-ng start wlan1')
	time.sleep(3)
	os.system('clear')
	print('''\033[1;36m__          ___  __ _  _____                       
\ \        / (_)/ _(_)/ ____|                      
 \ \  /\  / / _| |_ _| (___  _ __   __ _ _ __ ___  
  \ \/  \/ / | |  _| |\___ \| '_ \ / _` | '_ ` _ \ 
   \  /\  /  | | | | |____) | |_) | (_| | | | | | |
    \/  \/   |_|_| |_|_____/| .__/ \__,_|_| |_| |_|
                            | |                    
                            |_|                    \033[1;m''')	
	print('''\033[1;91mOptions:
	[1] Random spam
	[2] Create your spam\033[1;m''')
	x = input('\033[1;91mSelect an option: \033[1;m')
	if "1" in x:	
		time.sleep(1)
		print('\033[32m[+] Spam is running !!!\033[32m')
		print('\033[32m[+] Press Ctrl + C to stop spam.\033[32m')
		os.system('mdk3 wlan1mon b -c 2 -s 10000')
	if "2" in x:
		time.sleep(1)
		print('\033[32m[+] Spam is running !!!\033[32m')
		print('\033[32m[+] Press Ctrl + C to stop spam.\033[32m')	
		os.system('mdk3 wlan1mon b -c 2 -f /home/kali/WifiSpam/MySpam.txt')
