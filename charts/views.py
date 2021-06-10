from django.shortcuts import render
import requests


# Create your views here.

def charts(request):

    # Under Development

    '''url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name":"India"}

    headers = {
        'x-rapidapi-key': "b0166b2bfemsh17c840521658b71p1ee3dajsne5c3d1f64c08",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)'''

    '''url = "https://covid-19-tracking.p.rapidapi.com/v1/India"

    headers = {
        'x-rapidapi-key': "b0166b2bfemsh17c840521658b71p1ee3dajsne5c3d1f64c08",
        'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)'''


    return render(request, 'Charts.html')
