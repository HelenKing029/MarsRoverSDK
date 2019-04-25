import requests
import webbrowser

api_key = "ENTER-KEY"


def mostRecentSolDate():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=max_sol&camera=fhaz&api_key={}".format(api_key)
    myData = requests.get(url)
    print(myData)
    json_dict = myData.json()
    print(json_dict)
    roverImage = json_dict["photos"][0]["img_src"]
    return webbrowser.open_new_tab(roverImage)

def roverMissionStatus():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?status&api_key={}".format(api_key)
    myData = requests.get(url)
    roverStatus = myData.json()
    print(roverStatus)

def missionManifest(rover_name):
    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    manifest = myData['photo_manifest'] ## need to confirm if this is correct?
    print(manifest)

missionManifest(curiosity)
myrequest()
#"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=ENTER_YOUR_KEY"
