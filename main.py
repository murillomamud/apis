#%%
#imports
import requests
import json
import backoff
import random
import logging


url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url)

#%%

if ret:
    print(ret.text)
else:
    print('error')

# %%

dollar = json.loads(ret.text)['USDBRL']

# %%

print(f" 20 Dollars today costs {float(dollar['bid'])*20} reais")

# %%

def quotation(value, curr):
    url = f'https://economia.awesomeapi.com.br/last/{curr}' 
    #url = 'https://economia.awesomeapi.com.br/last/{}'.format(curr) 
    ret = requests.get(url)
    retJson = json.loads(ret.text)[curr.replace('-','')]
    print(f" {value} {curr[:3]} today costs {float(retJson['bid'])*20} {curr[-3:]}")
# %%
quotation(20, 'USD-BRL')
# %%
quotation(20, 'JPY-BRL')
# %%
try:    
    quotation(10, 'XXX')
except:
    pass    
# %%
try:    
    quotation(10, 'XXX')
except Exception as e:
    print(e)
else:
    print('ok')

# %%

lst_money = [
    "USD-BRL",
    "EUR-BRL",
    "BTC-BRL",
    "RPL-BRL",
    "JPY-BRL"

]

value = 20

for curr in lst_money:
    url = f'https://economia.awesomeapi.com.br/last/{curr}' 
    ret = requests.get(url)
    retJson = json.loads(ret.text)[curr.replace('-','')]
    print(f" {value} {curr[:3]} today costs {float(retJson['bid'])*value} {curr[-3:]}")
# %%

for curr in lst_money:
    try:
        url = f'https://economia.awesomeapi.com.br/last/{curr}' 
        ret = requests.get(url)
        retJson = json.loads(ret.text)[curr.replace('-','')]
        print(f" {value} {curr[:3]} today costs {float(retJson['bid'])*value} {curr[-3:]}")
    except:
        print(" error in currency:{}".format(curr))
# %%

def mult_currency(newValue):
    lst_money = [
    "USD-BRL",
    "EUR-BRL",
    "BTC-BRL",
    "RPL-BRL",
    "JPY-BRL"
]

    for curr in lst_money:

        url = f'https://economia.awesomeapi.com.br/last/{curr}' 
        ret = requests.get(url)
        retJson = json.loads(ret.text)[curr.replace('-','')]
        print(f" {newValue} {curr[:3]} today costs {float(retJson['bid'])*newValue} {curr[-3:]}")



# %%
mult_currency(100)
# %%

def error_check(func):
    def inner_func(*args, **kargs):
        try:
            func(*args, **kargs)
        except:
            print(f"{func.__name__} failed")
    return inner_func

@error_check
def single_curr(newValue, curr):
    url = f'https://economia.awesomeapi.com.br/last/{curr}' 
    ret = requests.get(url)
    retJson = json.loads(ret.text)[curr.replace('-','')]
    print(f" {newValue} {curr[:3]} today costs {float(retJson['bid'])*newValue} {curr[-3:]}")    


single_curr(20, 'USD-BRL')
single_curr(20, 'EUR-BRL')
single_curr(20, 'BTC-BRL')
single_curr(20, 'RPL-BRL')
single_curr(20, 'JPY-BRL')


# %%
def test_func(*args, **kargs):
    rnd = random.random()
    print(f"""
        RND:{rnd}
        args: {args if args else 'no args'}
        kargs: {kargs if kargs else 'no kargs'}
        """)
    if rnd < .2:
        raise   ConnectionAbortedError('Connection was terminated')
    elif rnd < .4:
        raise ConnectionRefusedError('Connection was refused')
    elif rnd < .6:
        raise TimeoutError('Timeout Error')
    else:
        return ('ok')
# %%
test_func()
# %%
test_func(42)

# %%
test_func(42, 51, name="john")
# %%

@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_funcNew(*args, **kargs):
    rnd = random.random()
    print(f"""
        RND:{rnd}
        args: {args if args else 'no args'}
        kargs: {kargs if kargs else 'no kargs'}
        """)
    if rnd < .2:
        raise   ConnectionAbortedError('Connection was terminated')
    elif rnd < .4:
        raise ConnectionRefusedError('Connection was refused')
    elif rnd < .6:
        raise TimeoutError('Timeout Error')
    else:
        return ('ok')
# %%
test_funcNew()
# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%
@backoff.on_exception(backoff.expo, (ConnectionAbortedError, ConnectionRefusedError, TimeoutError), max_tries=10)
def test_funcNewLog(*args, **kargs):
    rnd = random.random()
    log.debug(f"RND:{rnd}")
    log.info(f"args: {args if args else 'no args'}")
    log.info(f"kargs: {kargs if kargs else 'no kargs'}")

    if rnd < .2:        
        log.error('Connection was terminated')
        raise   ConnectionAbortedError('Connection was terminated')
    elif rnd < .4:
        log.error('Connection was refused')
        raise ConnectionRefusedError('Connection was refused')
    elif rnd < .6:
        log.error('Timeout Error')
        raise TimeoutError('Timeout Error')
    else:
        return ('ok')
# %%
test_funcNewLog()
# %%
