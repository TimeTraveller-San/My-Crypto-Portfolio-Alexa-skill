![LOGO](https://i.imgur.com/8q5pYLJ.png)
# My Crypto Portfolio : Alexa skill
1. Flask ask endpoint : Our skill endpoint is constructed in the powerful flask-ask endpoint
2. Alexa skill data API : We created from the scratch a seperate API specially designed for the versatile requirements of our skill
3. Skill user registration website: This is where our users register their crypto addresses with us to get dynamic lightning fast updates.
4. Docs: These are the docs explaining everything


# Description
My Crypto Currency is a one-stop skill for all crypto related queries and personal portfolio details. It supports a wide range of commands which can mainly be divided into two parts:-

a. Registration independent commands : (For these commands users need not register his/her email with our services)

	1. What is the price of [crypto]: Alexa will speak out the price of the [crypto] currently we support a range of 52 cryptocurrencies which can be found here (https://mycryptoportfolio.netlify.com/support.html). Along with the price, Alexa will speak the percentage increase/decrease in past 24 hours which is very handy
	2. What is the market cap of [crypto]
	3. Alexa fetch me some crypto news
	4. Alexa, predict the price of [crypto] on 1 June: Through state of the art machine learning techniques, our skill's machine learning algorithm can predict the price of btc/eth/ltc/doge upto 30 days from the current date. Note: Market is subjected to unforseeable sudden changes, these predictions are only based upon past data and can not be trusted with confidence.

b. Registration dependent commands: These commands require special information namely bitcoin/ ether/ litecoin and dogecoin address from the user and requires registration at our platform https://mycryptoportfolio.netlify.com/ 

	1. Give me an update on my portfolio?: tells you the changes in your portfolio since last 24 hours
        2. Summarize my portfolio
	3. How many [CRYPTO] am I holding? : we support 4 cryptos for this namely btc/doge/ltc/eth. Alexa will speak the crypto amount and it's equivalent in USD
	4. How many unconfirmed transactions do i have?
