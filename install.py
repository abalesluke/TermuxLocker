import os, time
os.system('pkg install python')
os.system('pkg install pip')

try:
	import colorama
	from colorama import Fore,Back

except ImportError:
	os.system("pip install colorama")

os.system('clear')

f = Fore
r = f.RED
g = f.GREEN
m = f.MAGENTA
c = f.CYAN
y = f.YELLOW

print(r+"""
╔╦╗┌─┐┬─┐┌┬┐┬ ┬─┐ ┬  ╦  ┌─┐┌─┐┬┌─┌─┐┬─┐
 ║ ├┤ ├┬┘││││ │┌┴┬┘  ║  │ ││  ├┴┐├┤ ├┬┘
 ╩ └─┘┴└─┴ ┴└─┘┴ └─  ╩═╝└─┘└─┘┴ ┴└─┘┴└─
 Termux Locker By: AL104 | Anikin Luke
""")
print(f"{c}By: Anikin Luke")
time.sleep(1)
print(f"{m} Loading...")
time.sleep(5)

while True:
	print("Enter the password you want for lock.")
	ui = input("Password: ")
	ui2 = input("ReType Password: ")
	
	if(ui == ui2):
		print("loading..")
		time.sleep(.2)
		print('creating...')
		o = open('lock.py', 'a')
		pload = """
import os, time
os.system('clear')
try:
	import colorama
	from colorama import Fore

except ImportError:

	print("colorama or pip is not installed!!")
	print('auto installing colorama or pip')
	time.sleep(2)
	os.system('pkg install pip3')
	os.system('pip3 install colorama')

paz = 'ptestp'

f = Fore
r = f.RED
g = f.GREEN
c = f.CYAN
b = f.BLUE
y = f.YELLOW

while True:
	try:
		print(c+b+"Enter password to proceed!")
		ui = input(g+"AL104~: ")

		if(ui == paz):
			print(g+"Nice! Welcome Back!!")
			time.sleep(2)
			os.system("clear")
			break

		else:
			print("ERROR!! wrong password!!")
			time.sleep(5)
			os.system('clear')

	except KeyboardInterrupt:
		print(r+"Error cannot be bypass!!")
		
		try:
			time.sleep(3)
			os.system("clear")

		except KeyboardInterrupt:
			for i in range (100):
				try:

					time.sleep(.1)
					print("INTRUDER!! GO AWAY SCRIPT KIDDIE!!")

				except KeyboardInterrupt:
					print("LOL YOU WISH YOU CAN!!")




			"""
		payload = pload.replace('ptestp', ui2)
		o.write(payload)
		print("Installing..pls wait")
		os.system('echo python3 lock.py >> /data/data/com.termux/files/usr/etc/bash.bashrc')
		time.sleep(3)
		os.system('mv lock.py /data/data/com.termux/files/home/')
		
		print("\n installation done! pls restart termux!")
		print('Important Note! Do not delete the file name lock.py \n')
		print("pls restart TERMUX")

		break

	else:
		print("\nReTyped Password not match in Password\nTRY AGAIN!\n\n")


