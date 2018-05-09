import threading
import bs4
import requests
from datetime import date
import calendar

parsed = {}

links = ["https://astrostyle.com/daily-horoscopes/aries-daily-horoscope/",
         "https://astrostyle.com/daily-horoscopes/taurus-daily-horoscope/",
         "https://astrostyle.com/daily-horoscopes/gemini-daily-horoscope/",
         "https://astrostyle.com/daily-horoscopes/cancer-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/leo-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/virgo-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/libra-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/scorpio-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/sagittarius-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/capricorn-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/aquarius-daily-horoscope/",
         "http://astrostyle.com/daily-horoscopes/pisces-daily-horoscope/" ]

date_today=date.today()
day=calendar.day_name[date_today.weekday()].lower()
if day=='sunday':
        day='saturday' #site has same horoscope for both days, sunday ko off hoga employees ka

def worker(i):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'}
        res = requests.get(i,headers=headers)
        soup = bs4.BeautifulSoup(res.content,'lxml')
        zodiac = soup.title.string.split(' ', 1)[0].upper()
        para = soup.find(id=day).p.string
        parsed[zodiac]=para

def defunct():
	threads = []
	for i in links:
		t = threading.Thread(target=worker, args=(i,))
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	return(parsed)
