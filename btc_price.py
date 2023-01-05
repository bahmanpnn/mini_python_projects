import cryptocompare
from time import sleep
from pygame import mixer
import pyttsx3

mixer.init()
engine=pyttsx3.init()

# data=cryptocompare.get_price('btc',currency='usd',full=True)
# print(data["RAW"]["BTC"]["USD"]["HIGHHOUR"])


data=cryptocompare.get_price('btc',currency='usd')["BTC"]["USD"]
print(data)

variance=50
thresh_down=data-variance
thresh_up=(data)+variance

while True:
    btc_price=cryptocompare.get_price('BTC',currency='USD')["BTC"]["USD"]
    if btc_price<thresh_down:
        print("btc went low! btc_price=",btc_price)
        thresh_up-=variance
        thresh_down-=variance
        # mixer.music.load('down.mp3')
        # mixer.music.play(loops=0,start=1,fade_ms=5)
        engine.say("btc is {}".format(int(btc_price)))
        engine.runAndWait()
    elif btc_price>thresh_up:
        print("btc went high! btc_price=",btc_price)
        thresh_up+=variance
        thresh_down+=variance
        # mixer.music.load('up.mp3')
        # mixer.music.play(loops=0,start=1,fade_ms=1)
        engine.say("btc is {}".format(int(btc_price)))
        engine.runAndWait()
    else:
        print(thresh_down,"<",btc_price,"<",thresh_up)
    sleep(15)
# todo:make database for this app and save prices for it to show a diagram after some time in 1h or 4h!