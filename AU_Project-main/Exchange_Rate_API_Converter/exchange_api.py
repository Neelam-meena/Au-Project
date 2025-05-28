import requests

Base_url = "https://api.exchangerate-api.com/v4/latest/"


def exchange_rate(currency_code):

    comp_url = Base_url + currency_code

    try:
        response = requests.get(comp_url)
        data = response.json()
        value = data['rates']['INR']
        return(value)

    
    except: 
        return None
    
ans= exchange_rate('USD')
print(ans)
