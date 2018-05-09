import threading
import bs4
import requests

parsed = {}

links = ["https://www.tarot.com/daily-horoscope/aries",
		"https://www.tarot.com/daily-horoscope/taurus",
		"https://www.tarot.com/daily-horoscope/gemini",
		"https://www.tarot.com/daily-horoscope/cancer",
		"https://www.tarot.com/daily-horoscope/leo",
		"https://www.tarot.com/daily-horoscope/virgo",
		"https://www.tarot.com/daily-horoscope/libra",
		"https://www.tarot.com/daily-horoscope/scorpio",
		"https://www.tarot.com/daily-horoscope/sagittarius",
		"https://www.tarot.com/daily-horoscope/capricorn",
		"https://www.tarot.com/daily-horoscope/aquarius",
		"https://www.tarot.com/daily-horoscope/pisces"]

def worker(i):
	res = requests.get(i)
	soup = bs4.BeautifulSoup(res.content,'lxml')
	zodiac = soup.title.string.split(' ', 1)[0].upper()
	para = soup.find("p",class_="js-today_interp_copy").string
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