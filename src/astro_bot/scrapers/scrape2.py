import threading
import bs4
import requests

parsed = {}

links=[
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=5",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=6",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=8",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=11",
	"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12",]

def worker(i):
	res = requests.get(i)
	soup = bs4.BeautifulSoup(res.content,'lxml')
	zodiac = soup.title.string.split(' ', 1)[0].upper()
	soup.p.b.decompose() # Removing date inside the horoscope
	para = soup.p.get_text().strip()
	parsed[zodiac] = para

def defunct():
	threads = []
	for i in links:
		t = threading.Thread(target=worker, args=(i,))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	return(parsed)