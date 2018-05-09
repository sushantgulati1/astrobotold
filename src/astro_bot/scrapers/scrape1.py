import threading
import bs4
import requests

parsed = {}

links = ["https://www.astrology.com/horoscope/daily/aries.html",
         "https://www.astrology.com/horoscope/daily/today/taurus.html",
         "https://www.astrology.com/horoscope/daily/today/gemini.html",
         "https://www.astrology.com/horoscope/daily/today/cancer.html",
         "https://www.astrology.com/horoscope/daily/today/leo.html",
         "https://www.astrology.com/horoscope/daily/today/virgo.html",
         "https://www.astrology.com/horoscope/daily/today/libra.html",
         "https://www.astrology.com/horoscope/daily/today/scorpio.html",
         "https://www.astrology.com/horoscope/daily/today/sagittarius.html",
         "https://www.astrology.com/horoscope/daily/today/capricorn.html",
         "https://www.astrology.com/horoscope/daily/today/aquarius.html",
         "https://www.astrology.com/horoscope/daily/today/pisces.html"]

def worker(i):
    res = requests.get(i)
    soup = bs4.BeautifulSoup(res.content, 'lxml')
    para = soup.p.string
    zodiac = soup.h3.string.upper()
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

    
