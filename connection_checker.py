import urllib.request

def check_internet_connection():
	try:
		urllib.request.urlopen('http://google.com', timeout=1)
		return True
	except urllib.request.URLError: return False
