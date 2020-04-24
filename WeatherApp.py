import tkinter as tk
from tkinter import font
import requests




HEIGHT=500
WIDTH=600

def test_function(entry):
    print("This is the entry:", entry)

    
   


   
def format_response(weather):
    try: 
       
       name = weather['name']
       country = weather['sys'] ['country']
       desc = weather['weather'][0]['description']
       temp = weather['main']['temp']


       final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature: %s%s' %(name, country, desc, temp,'°C')    
    except:
       final_str = 'There was a problem retrieving data!\n Enter a valid name of city!'

    return final_str



def get_weather(city):
    weather_key ='3c0ea3b30ed2bda5f524e44631d65f1a'
    url='https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q':city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


   
  
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
background_image = tk.PhotoImage(file='ios_weather_icons.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='black',bd=5)
frame.place(relx=0.5,rely=0.22,relwidth=0.7,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=('Courier',12))
entry.place(relwidth=0.53,relheight=0.6)

button = tk.Button(frame, bg='#262d43', fg='white',text="Get Weather",font=('Arial bold',14), command=lambda: get_weather(entry.get()))
button.place(relx=0.6,relwidth=0.4,relheight=0.7)

lower_frame = tk.Frame(root, bg='black', bd=8)
lower_frame.place(relx=0.5,rely=0.28,relwidth=0.7,relheight=0.5,anchor='n')

label = tk.Label(lower_frame,bg='#262d43',fg='white',font=('Courier', 14))
label.place(relwidth=1,relheight=1)



root.mainloop()
