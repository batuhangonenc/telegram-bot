import requests
from datetime import datetime
import time


def send_msg(text):
	
	#token of your telegram bot
	token = ""

	chat_id=""

	url_req =f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"


	try:
		results = requests.get(url_req)
		print(results.json())
	except:
		print("---\nsomething went wrong.")



datalist = [

["lesson name","zoomid","password","teacher name"], # ["math","000 000 0000","1234","Mr. Peterson"]

]


datadict = {

"lesson name":datalist[0]
 }




weekly_program = [

["lesson name","hour : min","day of month"]# ["physics","08 : 55","07"]

]


while 1:
	today = datetime.now().strftime("%x")[3:5]

	hourmin = datetime.now().strftime("%H : %M")
	
	for lesson in weekly_program:
		
		lessonBackup = lesson

		name = lesson[0]

		sending_time = lesson[1]

		day = lesson[2]

	
		if (today == day) and (hourmin == sending_time ):
			print("yes !")
			text = ""
			for i in datadict[name]:
				text += i

				if (i == datadict[name][3]):
					break
	
				text += "\n\n"

			text += " is inviting you.\n\n"

			text += datetime.now().strftime("%x %H : %M")


		
			send_msg(text)

			print(f"---\nmessage sent successfully :\n{text}")

			weekly_program.remove(lessonBackup)

			break
