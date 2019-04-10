import requests
import webbrowser

api_key = "wTdsNpFtovzuN4I2Vo4xGU3SQLf8e5robl4oj9c6"

def myrequest():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key={api_key}"
    myData = requests.get(url)
    print(myData)
    json_dict = myData.json()
    print(json_dict)
    roverImage = json_dict["photos"][0]["img_src"]
    webbrowser.open_new_tab(roverImage)

myrequest()
#"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=ENTER_YOUR_KEY"
