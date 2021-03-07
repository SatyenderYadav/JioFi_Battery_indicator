from bs4 import BeautifulSoup 
import requests

url = "http://jiofi.local.html/"
url_contents = requests.get(url)
soup = BeautifulSoup(url_contents.text, 'html.parser')
div = soup.find("input", {"id": "batterylevel"})
battery = int(div['value'].split('%')[0])

def window_notify(status):
	from win10toast import ToastNotifier
	toaster = ToastNotifier()

	toaster.show_toast("JioFi Battery Status", status, threaded=True, duration=3) 

	toaster.notification_active()

if (battery < 50):
	window_notify("Battery is less than 50 %")
elif(battery < 20):
	window_notify("Battery is less than 20 % Put it on charge")
elif(battery < 10):
	window_notify("Anytime it can shutdown")
else:
	pass

