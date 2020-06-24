from django.shortcuts import render
import requests,json


# Create your views here.
def index(request):
    if request.method=='POST':
     firstname=request.POST.get('fname')
     lastname=request.POST.get('lname')
     r=requests.get('http://api.icndb.com/jokes/random?firstName='+ firstname + '&lastName=' + lastname)
     json_data=json.loads(r.text)
     joke=json_data.get('value').get('joke')
     context={'joker':joke}
     return render(request, 'mysite/index.html',context)
    else:
        firstname ='Ravia'
        lastname = 'lodu'
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)



def contact(request):
    if request.method=='POST':
        return render(request, 'mysite/thank.html')
    else:
     return render(request, 'mysite/contact.html')


def portfolio(request):
    return render(request, 'mysite/portfolio.html')
