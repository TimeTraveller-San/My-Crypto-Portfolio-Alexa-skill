# My crypto porfolio
[FAQ](https://mycryptoportfolio.netlify.com/faq.html)

[Terms of use](https://mycryptoportfolio.netlify.com/terms.html)

[Privacy Policy](https://mycryptoportfolio.netlify.com/privacy.html)

## Watch the video
[![Watch the video](https://img.youtube.com/vi/8ZVksOpH16A/maxresdefault.jpg)](https://www.youtube.com/watch?v=8ZVksOpH16A)

## User docs:
My Crypto Currency is a one-stop skill for all crypto related queries and personal portfolio details. With several features specifically crafted for managing and making queries regarding various cryptocurrencies. From getting complete portfolio updates and crypto news in the early morning to fetching unconfirmed transactions you may be worried about during congested mempool, my crypto portfolio alexa skill is there to help! What's more? It even enables you to make trading decisions with help of machine learning algorithms taking into consideration the huge trading data of the past to make predictions. Although, it is to be noted that any methodology with complex mathematics at it's core isn't devoid of error and must be trusted with care.  

You can command our skill to do various things for you as follows:
#### Commands:
Note: Each of the following commands can be invoked with several statements. For brevity facilitates reasoning, we're only including a single command in each of the example.
**Account independent commands:**
- Invocation:

`start my crypto portfolio`
- Fetch price:

`what is the price of bitcoin`

You can replace bitcoin with any of [supported crypto](https://mycryptoportfolio.netlify.com/support.html) (https://mycryptoportfolio.netlify.com/support.html). Alexa not only speaks up the current price but also the net gain/loss within past 24 hours which is very handy.

- Fetch market cap:

`what is bitcoin's current market cap`

You can replace bitcoin with any of [supported crypto](https://mycryptoportfolio.netlify.com/support.html) (https://mycryptoportfolio.netlify.com/support.html)
- Get predictions:

 `predict the price of bitcoin on 26th october`
 
You can get price prediction for 4 cryptos (btc, eth, ltc, doge) upto 30 days from the current date

*Account dependent commands:**

To run these commands you need to register your email along with your crypto addresses to our database [here](https://mycryptoportfolio.netlify.com/index.html) (https://mycryptoportfolio.netlify.com/index.html)

- Unonfirmed transactions:

`How many unconfirmed transactions do i have?`

- Portfolio value:

`how many bitcoins am i holding?` 

You can replace bitcoin with (litecoin, ether, dogecoin)

- net portfolio summary

`what is the net worth of my portfolio` 

returns the total worth in USDs and asks ``do you need detailed explanation?`` on answering yes to which, you get a complete summary of every coin, it's amount and it's amount in USDs you're holding.







## Developer docs
### Data flow
![](https://i.imgur.com/XvZDaYw.jpg)
- Our skill's endpoint is created in python using flask_ask and flask library. It is hosted at pythonanywhere. 
- We have created from scratch a completely new API dedicated to My Crypto Portfolio skill, this API has several features and it's docs can be viewed here. 
https://github.com/TimeTraveller-San/alexa-skill-API/blob/master/README.md
- We maintain a database for our API storing the email address and corresponding crypto addresses of users for dynamically tracking the changes in the wallet. It must be noted, if the users don't want to share their email with us, the skill is still usable but with limited functionalities. 

### How our registration model works?
There have been previous attempts made to create crypto portfolio skills using alexa but all of them were static in the sense that any change made in your actual crypto wallet does not show over the skill and needs to be updated explicitly but our skill uses a tracking model where any change made in your actual wallet is automatically reflected into the skill making it much more dynamic, robust and usable. 
User registers his email along with the public keys of four of his cryptocurrency wallets through the form [here](http://mycryptoportfolio.netlify.com/):
![register](https://i.imgur.com/ttDpo7p.png)
On clicking submit, the email ID along with the public keys (addresses) are stored into our database and are later used by the skill to fetch the account details such as:

1. **Portfolio value:**

The core of blockchain technology is a public ledger. This ledger can be viewed by anyone. Given the public key, we use bitcoin's API to fetch the amount of coins held in the address stored in our database. 
![holdings](https://i.imgur.com/9DB5vGH.jpg)
This public API can be viewed here: https://www.blockchain.com/btc/address/1BPyXemrs6Rb2kQdJynnxzxEVv5M2qLfa2

Similarly, other crypto details can be fetched.


2. **Unconfirmed transcations:** 

Unconfirmed transaction means that the transaction has not been included in a block and thus has not been completed. This too can be fetched from the bitcoin and other crypto API's provided we have the public key.
![txns](https://i.imgur.com/XVPa17D.jpg)

This public API can be viewed here: https://www.blockchain.com/btc/address/1BPyXemrs6Rb2kQdJynnxzxEVv5M2qLfa2

Our API also performs several other features:

1. **Fetch news:** 

Top new articles are fetched from the google news crypto section. This is done using webscraping with bs4 python module.
(https://news.google.com/topics/CAAqBwgKMIjl9gowp9zVAg?hl=en-IN&gl=IN&ceid=IN:en)


2. **Price prediction:**

This is done using our machine learning algorithm which uses the data set regularly updated at https://coinmetrics.io/data-downloads/ 

## Machine learning model
Description of Prediction Model: A recent news item went as follows: “Apple buys machine learning firm Perceptio Inc., a startup, in an attempt to bring advanced image-classifying artificial intelligence to smartphones by reducing data overhead which is typically required of conventional methods.” Another recent development was that MIT researchers were working on object recognition through flexible machine learning. Machine learning is starting to reshape how we live, and it’s time we understood what it is and why it matters.
In our Alexa skill, we have applied Machine Learning in predicting the price of crypto-currencies for the user in order to assist him to manage his crypto-currency transactions. The model learns the pattern followed by the prices of the respective crypto-currency from its beginning to date and makes predictions for the next 30 days for the user. However, these are simply prices predicted by an algorithm and may vary with the actual prices. We, on our part, have tried our level best to provide the user with prices predicted as close as possible to the real prices.

## Several other features using external API:
API endpoint: https://www.coindesk.com/api/ 

We use the coindesk free API according it's TOC we are allowed to use this API with our skill until we start monetizing it which is when we need to buy the API.

We can peform various functions with this such as:

1. **Fetch price of 50+ cryptocurrencies:**

We can fetch price of all cryptos listed on our website support (https://mycryptoportfolio.netlify.com/support.html)

Our skill not only reads the price but also present the net gain/loss in the price

2. **Fetch market cap:**
Fetch net market cap of 50+ cryptocurrencies:

We can fetch current market cap of all cryptos listed on our website support (https://mycryptoportfolio.netlify.com/support.html)

# Target Audience
The generation of millenials is a strong community
who support the use of cryptocurrencies and this is
just the right platform for simplifying their daily
management and use of cryptocurrencies.
My Crypto Portfolio offers all the needed features
that a crypto savvy person might need in order to
stay updated with the market.


