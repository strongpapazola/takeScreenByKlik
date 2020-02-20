import pyautogui
from pynput.mouse import Listener

#myScreenshot.save(r'C:\Users\Ron\Desktop\Test\screenshot1.png')

i = 1
print("[*] Status Active")
print('')

myScreenshot = pyautogui.screenshot()
pathDisk = ["C","D","E","F","G","H","I","J","K"]
disk = []
for pd in pathDisk:
	try:
		myScreenshot.save(r""+str(pd)+":\\6f62a19c7fe5725693d4a614e179c822\\"+str(i)+'_perClick.png')
		disk.append(str(pd))
		print('[+] Disk : '+str(pd)+" Selected")
	except:
		print('[-] Fail Set on disk : '+str(pd))


print("")
print("[*] Take Screen Started !")
print("")

while i >= 0:
	def on_click(x, y, button, pressed):
		global i
		global disk
		if pressed:
			global i
			global disk
			i = i + 1
			myScreenshot = pyautogui.screenshot()
			for pd in disk:
				myScreenshot.save(r""+str(pd)+":\\6f62a19c7fe5725693d4a614e179c822\\"+str(i)+'_perClick.png')
				print('[+] Pressed '+str(i)+' saved on '+str(pd))

	with Listener(on_click=on_click) as listener:
		listener.join()
