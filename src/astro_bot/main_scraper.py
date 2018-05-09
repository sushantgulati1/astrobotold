import time
from astro_bot.scrapers.scrape1 import defunct as defunct1
from astro_bot.scrapers.scrape2 import defunct as defunct2
from astro_bot.scrapers.scrape3 import defunct as defunct3
from astro_bot.scrapers.scrape4 import defunct as defunct4
from astro_bot.data_service import put_horoscopes

one_large_dict = {}

def prep_db():
    one_large_dict['astrology.com'] = defunct1()
    one_large_dict['horoscope.com'] = defunct2()
    one_large_dict['tarot.com'] = defunct3()
    one_large_dict['astrostyle.com'] = defunct4()
    put_horoscopes(one_large_dict)

def update_db():
    while True:
        prep_db()
        time.sleep(36_000)