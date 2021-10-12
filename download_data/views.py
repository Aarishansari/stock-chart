from django.shortcuts import render
from .forms import TickerForm
from django.http import HttpResponseRedirect
from .y_finance import get_meta_data
from .models import StocksData
def index(request):
	if request.method == 'POST':
		form = TickerForm(request.POST)
		if form.is_valid():
			ticker = request.POST['ticker']
			return HttpResponseRedirect(ticker)
	else:	
		form = TickerForm()
	return render(request,'index.html',{'form':form})
	
	
def ticker(request,tid):
	stockdata = StocksData()
	context = {}
	stockdata.ticker = get_meta_data(tid)['ticker']
	stockdata.description = get_meta_data(tid)['description']
	stockdata.exchange = get_meta_data(tid)['exchangeCode']
	stockdata.name = get_meta_data(tid)['name']
	
	stockdata.save()
	stocks_info = StocksData.objects.latest()
	context['ticker'] = stocks_info.ticker
	print(context['ticker'])
	context['description'] = stocks_info.description
	context['exchange'] = stocks_info.exchange
	context['name'] = stocks_info.name
	return render(request,'ticker.html',context )
