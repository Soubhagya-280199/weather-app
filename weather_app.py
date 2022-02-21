import requests

api_key = '4404d77a15c8378705d8190f42c72fe0'
val = True
while(True):
    user_input = input("Enter your city : ")

    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    '''to fetch status code of the respose '''
    #print(weather_data.status_code)
    '''to fetch all the details '''
    #print(weather_data.json())

    if weather_data.json()['cod'] == '404':
        print(f"Your city {user_input} not found in our database!!")
    
    else:
        #weather = weather_data.json()['weather'][0]['main']
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        country = weather_data.json()['sys']['country']

        print(f"The weather at {user_input},{country} \n is having temprature {temp} \n weather {weather}")

    complete = input("Do you want to check another (y/n) :")

    
    if complete == "y":
        pass
    else:
        break
