from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import statsmodels.api as sm
from django.shortcuts import render
import requests
import json
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from plotly.offline import plot

# Create your views here.
def home(request):
	#Crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	#Crypto Price
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTS,LINK,BNB,TRX,ETC&tsyms=USD")
	price = json.loads(price_request.content)

	context={
	'api':api,
	'price':price
	}
	return render(request,'dashboard/home.html',context)

def prices(request):
	quote=''
	pred=["0"]
	crypto=''
	history=''
	data=''
	plot_div=''
	count=0
	high=[] #The list that contains the average price of the crypto for the past 60 days
	if request.method=="POST":
		quote = request.POST['quote']
		quote = quote.upper()
		#Crypto Price
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		#Crypto Historical Data
		history_request = requests.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=" + quote + "&tsym=USD&limit=2000")
		history = json.loads(history_request.content)
		try:
			data = history['Data']['Data']

			for i in data:
				high.append((int(i['high']) + int(i['low']))/2)
				high = high[-60:]
			pred = train(high)
			x = np.linspace(0, 60,60)
			fig = go.Figure(data=go.Scatter(x=x, y=high))
			plot_div = plot(fig, output_type='div', include_plotlyjs=False)
		except:
			pass
	context={
	'quote':quote,
	'crypto':crypto,
	'history':history,
	'data':high,
	'plot':plot_div,
	'pred':int(pred[0]),
	}
	return render(request,'dashboard/prices.html',context)





def train(data):
	model = ExponentialSmoothing(np.asarray(data) ,seasonal_periods=7 ,trend='add', seasonal='add').fit()
	pred = model.forecast(1)
	return pred