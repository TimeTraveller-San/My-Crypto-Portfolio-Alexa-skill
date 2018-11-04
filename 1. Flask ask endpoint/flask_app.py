from flask import Flask, render_template
from flask_ask import(Ask,
            statement,
            question,
            delegate,
            session as ask_session,
            context as ask_context
)
import json
import requests
import time
import unidecode
import logging
import random
import bs4

logging.getLogger('flask_ask').setLevel(logging.DEBUG)

app = Flask(__name__)
ask = Ask(app, "/crypto_portfolio")

def convertDate(date):
    parts = date.split('-')
    return parts[2]+"/"+parts[1]+"/"+parts[0]

# def get_news():
#     hdr = {'User-Agent': 'Mozilla/5.0'}
#     page = requests.get(
#                         "https://news.google.com/topics/CAAqBwgKMIjl9gowp9zVAg",
#                         headers=hdr
#                         )
#     soup = bs4.BeautifulSoup(page.content, 'html.parser')
#     headings = soup.body.find_all('a', attrs={'class': ["ipQwMb" ,"Q7tWef"]})
#     response = {}
#     news = []
#     for heading in headings:
#         news.append(heading.text.strip())
#     response['news'] = news
#     return response

def get_news():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get("https://news.google.com/search?q=cryptocurrency", headers=hdr)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    headings = soup.body.find_all('p', attrs={'class': ["HO8did" ,"Baotjf"]})
    response = {}
    news = []
    for heading in headings:
        news.append(heading.text.strip())
    response['news'] = news
    return response

def strings(sample):
    statements = {'welcome': {1: "Welcome to crypto portfolio",
                              2: "Welcome to crypto portfolio, what would you like- a news briefing or a portfolio summary",
                              3: "Hi, welcome to your crypto portfolio",
                              4: "Ohaio, this is crypto portfolio"},
                  'bye': {1: "Bye, have a nice day",
                          2: "Farewell"},
                  'functions': {1: "Check price of a crypto currency."
                                "\nCheck market cap of a crypto"
                                "\nPredict price of crypto currency."
                                "\Check my unconfirmed transactions"
                                "\nGive a news briefing.\nGive an update on your portfolio."},
                  'help': {1: "you can ask me to: check or predict price of a crypto currency, read the news, or portfolio related enquiries"}}
    key = random.randint(1, len(statements[sample]))
    return statements[sample][key]

def currencyCode(currency):
    dictionary = {'bitcoin': 'btc',
                  'litecoin': 'ltc',
                  'namecoin': 'nmc',
                  'swiftcoin': 'stc',
                  'bytecoin': 'bcn',
                  'peercoin': 'ppc',
                  'dogecoin': 'doge',
                  'feathercoin': 'ftc',
                  'gridcoin': 'grc',
                  'primecoin': 'xpm',
                  'ripple': 'xrp',
                  'nxt': 'nxt',
                  'skycoin': 'sky',
                  'auroracoin': 'aur',
                  'coinye': 'koi',
                  'dash': 'ash',
                  'neo': 'neo',
                  'mazacoin': 'mzc',
                  'monero': 'xmr',
                  'nem': 'xem',
                  'potcoin': 'pot',
                  'synereo amp': 'amp',
                  'titcoin': 'tit',
                  'verge': 'xvg',
                  'stellar': 'xlm',
                  'vertcoin': 'vtc',
                  'ether': 'eth',
                  'ethereum': 'eth',
                  'ethereum classic': 'sdt',
                  'tether': 'neu',
                  'neucoin': 'dcr',
                  'decred': 'lsk',
                  'lisk': 'zec',
                  'zcash': 'bcc',
                  'bitconnect': 'bch',
                  'bitcoin cash': 'eos',
                  'cardano': 'ada',
                  'bitcoin private': 'tcp',
                  }
    return dictionary[currency]


@app.route('/')
def homepage():
    return "hi there, looking for my crypto portfolio?"

@ask.launch
def start_skill():
    welcome_message = strings('welcome')
    return question(welcome_message).reprompt("I didn't get that").simple_card(
                    title="Things you may ask me",content=strings('functions')
                    )


@ask.intent('AMAZON.HelpIntent')
def helping():
    msg = "I can do various things. Ask my about crypto news, current price, market cap or predicted price of crypto currencies."
    msg += " If you've linked your account with us, I can also tell your total or particular crypto holdings in your portfolio"
    msg += ". I can also tell about your unconfirmed transactions if any"
    msg += ". For more information please read the skill description or visit our website."
    return question(msg).simple_card(title="Help",content=msg)

@ask.intent('AMAZON.FallbackIntent')
def fall_back():
    msg = "I am sorry I can not understand!"
    return question(msg).simple_card(title="Help",content=msg)

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def no_intent():
    bye_text = 'Goodbye, farewell'
    return statement(bye_text)

@ask.intent("GetPrice",convert={'currency':str})
def fetchPrice(currency):
    if(currency != None):
        # print("session: ")
        # print(ask_session)
        currency = currencyCode(currency)
        URL = "http://alexaskill.pythonanywhere.com/?action=price&crypto="+currency
        #    print('given currency is:',currency)
        r = requests.get(URL)
        data = r.json()
        change = data['change']
        curPrice = data['price']
        percent = abs(change/data['price_old'])
        delta = ""
        if(change>0):
            delta = "an increase of {:.3f} percent from last 24 hours".format(percent)
        elif(change<0):
            delta = "an increase of {:.3f} percent from last 24 hours".format(percent)
        else:
            delta = "same as yesterday"
        msg = str(curPrice)+" US dollars"+" which is "+str(delta)
        return question(msg).simple_card(title="Current Price",content=msg)
    else:
        if(ask_session['dialogState'] != "COMPLETED"):
            return delegate()

@ask.intent("News")
def NewsIntent():
    num = 0
    if 'past' in ask_session.attributes:
        num = ask_session.attributes['past']
        ask_session.attributes['past'] = num+1
    else:
        num = num+1
        ask_session.attributes['past'] = num
    # url = "http://alexaskill.pythonanywhere.com/?action=news"
    # r = requests.get(url)
    # data = r.json()
    data = get_news()
    # print("\nWE GOT:\n\n",data,'\n\n\n\n')
    News = ""
    for i in range(num, num+6):
        News = News+str(i)+". "+(data['news'][i])+"\n"
    speech_text = News
    return question(speech_text).reprompt("what would you like to do?").simple_card(title="News Headline",content=speech_text)

@ask.intent("GetMarketCap",convert={'currency':str})
def GetMarketCapIntent(currency):
    if currency != None:
        code = currencyCode(currency)
        url = "http://alexaskill.pythonanywhere.com/?action=cap&crypto="+code
        r = requests.get(url)
        data = r.json()
        cap = data['cap']
        if cap[-1] == 'B':
            cap = cap[:-1]+'billion'
        else:
            cap = cap[:-1]+'million'
        msg = "Current market cap of "+str(currency)+" is "+cap
        return question(msg).simple_card(title="Market Cap",content=msg)
    else:
        if(ask_session['dialogState'] != "COMPLETED"):
            return delegate()

@ask.intent("PredictPrice",convert={'predictCurrency':str,'date':str})
def PredictPriceIntent(predictCurrency,date):
    # print(date)
    # print("\n\ncurrency is: ",predictCurrency)
    if (predictCurrency and date) != None:
        predictCode = currencyCode(predictCurrency)
        date = convertDate(date)
        print("date is:{}".format(date))
        url = "http://alexaskill.pythonanywhere.com/?action=predict&date="+date+"&crypto="+predictCode
        r = requests.get(url)
        status = requests.head(url)
        if status == 500:
            msg = "sorry currently i can predict prices only for bitcoin, "
            "ethereum, litecoin and dogecoin"
            return question(msg+" would you like to anything else?").simple_card(
                title="Oops",content=msg)
        data = r.json()
        predictedPrice = data['prediction']
        if(predictedPrice == 'invalid date'):
            return question(
                "sorry, the specified date is invalid, you may"
                " specify any date upto 30 days from today "
                "in dd/m m/yyyy format").simple_card(
                                "Oops!", "it seems that you have specified "
                                "a date in past or upto 30 days from today in"
                                " dd/mm/yyyy format")

        when = data['days_from_now']
        URL = "http://alexaskill.pythonanywhere.com/?action=price&crypto="+predictCode
        #print('given currency is:',currency)
        r = requests.get(URL)
        data = r.json()
        curPrice = data['price']
        change = float(predictedPrice) - float(curPrice)
        percent = round(abs(change/curPrice),2)
        if change < 0:
            delta = "down by {:.4f}".format(percent) + " percent to {}".format(predictedPrice)
        else:
            delta = "up by {:.4f}".format(percent) + " percent to {}".format(predictedPrice)

        percent = abs(change/data['price_old'])
        msg = predictCurrency+" will be "+delta
        cardBody = 'Predicted price: '+str(predictedPrice)
        return question(msg).simple_card(
            "Price Prediction", cardBody)
    elif ask_session['dialogState'] != "COMPLETED":
        return delegate()

@ask.intent("PortfolioTransactions",convert={'question':str})
def PortfolioTransactionsIntent():
    if 'accessToken' not in ask_context['System']['user']:
        return statement('Please link your account in the Alexa app')\
        .link_account_card()
    #print("accessToken found")
    url = "https://api.amazon.com/user/profile?access_token="+ask_context['System']['user']['accessToken']
    r=requests.get(url)
    msgTitle = ""
    # print("checking alexa api status code\n")
    # print(r.status_code)
    # print("response-content")
    # print(r.content)
    if r.status_code == 200:
        data = r.json()
        print("user data is: ")
        print(data)
        userEmail = data['email']
        # print("userEmail: "+userEmail)
        url = "http://alexaskill.pythonanywhere.com/?action=unconfirmed&id="+userEmail
        r = requests.get(url)
        data = r.json()
        #print("dengue's db's response:")
        #print(data)
        msgTitle = ""
        msgBody=""
        if 'response' in data:
            speech = ("It seems you have not registered yourself with me for your portfolio"
                    " please go to the link provided in the skill's description to register")
        #user is registered
        else:
            if data['total'] == '0':
                speech = "you don't have any unconfirmed transactions"
            else:
                speech = str(data['total'])+" unconfirmed transactions "
                if float(data['btc']):
                    speech.join(","+str(data['btc'])+" bitcoin ")
                    msgBody = msgBody.join("\nBitcoin: "+str(data['btc']))
                if float(data['doge']) :
                    speech.join(","+str(data['doge'])+" dogecoins ")
                    msgBody = msgBody.join("\nDogecoin: " + str(data['doge']))
                if float(data['ltc']) :
                    speech.join(","+str(data['btc'])+" litecoins, ")
                    msgBody = msgBody.join("\nlitecoin: " + str(data['ltc']))
                if float(data['eth']) :
                    speech.join("."+str(data['btc'])+" etheruem ")
                    msgBody = msgBody.join("\nEthereum: " + str(data['eth']))
            if question:
                if data['total'] != 0:
                    speech = "Yes there are total " + speech
            else:
                speech = "You have "+speech
            msgTitle = "Unconfirmed Transactions:"
            if msgBody != "":
                msgBody = ("Total: "+str(data['total']))+msgBody
            else:
                msgBody = "No transactions are pending"
        output=question(speech)
        if msgTitle != "":
            output=question(speech).simple_card(
                title="Unconfirmed Transactions",content=msgBody)
        return output
    else:
        print("never reached there not even once")
        return statement("Kindly make sure that you have logged "
            "into the alexa app using the same email provided "
            "at the time of registration for portfolio").simple_card(
            title="User Not Registered",content="If you are a new user "
            "please register at the link provided in the app description")

@ask.intent("PortfolioPrice",convert={'currency':str})
def PortfolioPriceIntent(currency):
    if 'accessToken' not in ask_context['System']['user']:
        return statement('Please link your account in the Alexa app').link_account_card()
    if currency in ['bitcoin','litecoin','dogecoin','ethereum','ether']:
        code = currencyCode(currency)
        url = "https://api.amazon.com/user/profile?access_token="+ask_context['System']['user']['accessToken']
        r=requests.get(url)
        status = r.status_code
        msgTitle = ""
        # print("email status: ")
        # print(status)
        if status == 200:
            data = r.json()
            userEmail = data['email']
            url = "http://alexaskill.pythonanywhere.com/?action=fetch&id="+str(userEmail)+"&crypto="+str(code)
            r = requests.get(url)
            data = r.json()
            #if user has  not registered- that is a new user
            if 'response' in data :
                speech = ("It seems you have not registered yourself with me for your portfolio"
                            " please go to the link provided in the skill's description to register")
                msgTitle = "User not registered"
                return question(speech).simple_card(title=msgTitle,content=msgBody)
            elif str(code) not in data:
                speech = ("You haven't registered your {} address with us").format(currency)
                msgTitle = "No address found"
                return question(speech).simple_card(title=msgTitle,content=speech)

            else:
                coin = str(code)
                usd = str(code)+"_USD"
                coin_c = "{:.4f}".format(data[coin])
                coin_usd = "{:.2f}".format(data[usd])
                speech = "you have " + coin_c + " " + coin + " worth $" + coin_usd
                msgTitle = "Portfolio details: "
                msgBody = "Coins: " + coin_c + coin + "\nWorth $" + coin_usd
                return question(speech).simple_card(title=msgTitle,content=msgBody)
        else:
            return statement(
                "Kindly make sure that you have logged "
                "into the alexa app using the same email provided "
                "at the time of registration for portfolio").simple_card(
                title="User Not Registered",content="If you are a new user "
                "please register at the link provided in the app description"
                )
    speech = "Sorry but I currently support only bitcoin, ethereum, dogecoin and litecoin"
    msgTitle = "Sorry"
    msgBody = ("Currently we support the following for portfolio details: \nbitcoin\nlitecoin\nethereum\ndogecoin")
    return question(speech).simple_card(title=msgTitle,content=msgBody)


@ask.intent("PortfolioSummary")
def PortfolioSummaryIntent():
    if 'accessToken' not in ask_context['System']['user']:
        return statement('Please link your account in the Alexa app')\
        .link_account_card()
    url = "https://api.amazon.com/user/profile?access_token="+ask_context['System']['user']['accessToken']
    r=requests.get(url)
    status = r.status_code
    msgTitle = ""
    if status == 200:
        data = r.json()
        userEmail = data['email']
        ask_session.attributes['email'] = userEmail
        url = "http://alexaskill.pythonanywhere.com/?action=fetch&id="+str(userEmail)+"&crypto=all"
        r = requests.get(url)
        data = r.json()
        if(data == ''):
            speech = ("It seems you have not registered the address with me for "+currency+
                    " please go to the link provided in the skill's description to add new address")
            msgTitle = ""
        #if user has  not registered- that is a new user
        elif ('response' in data):
            if (data['response'] == "user does not exist"):
                speech = ("It seems you have not registered yourself with me for your portfolio"
                    " please go to the link provided in the skill's description to register")
                msgTitle = ""
        else:
            #setting a session attribute for dialog
            ask_session.attributes['summary'] = "set"
            speech = "Your net balance is: ${:.2f}".format(data['balance'])
            speech = speech + " would you like a breakdown of the details?"
            msgTitle = "Portfolio details: "
            msgBody = "Net balance is: ${:.2f}".format(data['balance'])
        if msgTitle:
            return question(speech).simple_card(title=msgTitle,content=msgBody)
        return question(speech)
    else:
        return statement("Kindly make sure that you have logged "
            "into the alexa app using the same email provided "
            "at the time of registration for portfolio").simple_card(
            title="User Not Registered",content="If you are a new user "
            "please register at the link provided in the app description")

@ask.intent("Yes")
def YesIntent():
    if 'summary' in ask_session.attributes:
        userEmail = ask_session.attributes['email']
        print(userEmail)
        url = "http://alexaskill.pythonanywhere.com/?action=fetch&id="+str(userEmail)+"&crypto=all"
        r = requests.get(url)
        data = r.json()
        print(data)
        msgTitle=""
        msgBody = ""
        if(data == ''):
            speech = ("It seems you have not registered the address with me for "+currency+
                    " please go to the link provided in the skill's description to add new address")
            msgTitle = ""
        #if user has  not registered- that is a new user
        elif ('response' in data):
            if (data['response'] == "user does not exist"):
                speech = ("It seems you have not registered yourself with me for your portfolio"
                    " please go to the link provided in the skill's description to register")
                msgTitle = ""
        else:
            speech = "You have"
            c_codes = ['btc','doge','eth','ltc']
            c_names = ['bitcoins','dogecoins','ethers','litecoins']
            for c_code, c_name in zip(c_codes, c_names):
                if c_code in data:
                    coin_worth = "{:.4f}".format(data[c_code])
                    coin_usd = "{:.2f}".format(data[c_code+"_USD"])
                    speech +=", "+coin_worth+" "+c_name+" worth "+coin_usd+" dollars"
                    msgBody += "\n"+c_name+": "+coin_worth+" = $"+coin_usd


            # if 'btc' in data:
            #     print("btc was found in data")
            #     speech = speech+", "+str(data['btc'])+" bitcoins worth "+str(data['btc_USD'])+" dollars"
            #     msgBody = msgBody+"\nBitcoin: "+str(data['btc'])+" = $"+str(data['btc_USD'])
            # if 'doge' in data:
            #     speech = speech+", "+str(data['btc'])+" dogecoins worth "+str(data['doge_USD'])+" dollars"
            #     msgBody = msgBody+"\nDogecoin: "+str(data['doge'])+" = $"+str(data['doge_USD'])
            # if 'ltc' in data:
            #     speech = speech+", "+str(data['eth'])+" etheruem worth "+str(data['eth_USD'])+" dollars"
            #     msgBody = msgBody+"\nEthereum: "+str(data['eth'])+" = $"+str(data['eth_USD'])
            # if 'eth' in data:
            #     speech = speech+", "+str(data['ltc'])+" litecoins worth "+str(data['ltc_USD'])+" dollars"
            #     msgBody = msgBody+"\nLitecoin: "+str(data['ltc'])+" = $"+str(data['ltc_USD'])
        if msgTitle:
            return question(speech).simple_card(title=msgTitle,content=msgBody)
        return question(speech)

#@ask.intent("PortfolioUpdate")
#def PortfolioUpdateIntent():
#    if 'accessToken' not in ask_context['System']['user']:
#        print("accessToken not found")
#        return statement('Please link your account in the Alexa app') \
#    .link_account_card()#

#    #user is logged in:
#

if __name__ == '__main__':
    app.run(debug=True)
