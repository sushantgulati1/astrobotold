import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0, decode_responses=True)
r = redis.Redis(connection_pool=pool)

def put_horoscopes(one_large_dict):
    for big_key in one_large_dict:
        r.hmset(big_key, one_large_dict[big_key])

def get_horoscopes(zodiac):
    a = []
    a.append(r.hget('astrology.com', zodiac.upper()))
    a.append(r.hget('tarot.com', zodiac.upper()))
    a.append(r.hget('horoscope.com', zodiac.upper()))
    a.append(r.hget('astrostyle.com', zodiac.upper()))
    return a

def set_sign(user, zodiac):
    r.hmset('users', {user: zodiac})

def reset_sign(user):
    r.hdel('users', user)

def get_all_daily():
    return r.hgetall('users').items()
