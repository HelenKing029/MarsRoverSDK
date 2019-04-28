import requests
import webbrowser
import json

api_key = "ENTER-KEY"
api_key = "ENTER_YOUR_KEY"
#Mars Rovers: Curiousity Opportunity Spirit



#Returns the most recent image from the Curiousity Rover with the front camera
def mostRecentSolDateImage():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=max_sol&camera=fhaz&api_key={}".format(api_key)
    myData = requests.get(url)
    json_dict = myData.json()
    roverImage = json_dict["photos"][4]["img_src"]
    return webbrowser.open_new_tab(roverImage)

#Returns the Rovers Status
def roverMissionStatus(rover_name):
    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    roverStatus= myData["photo_manifest"]["status"]
    print(roverStatus)

#Getting the Mission Manifest from the chosen Rover
def missionManifest(rover_name):
    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    manifest = myData["photo_manifest"]
    print(manifest)

#Getting the Most Recent Sol from chosen Rover
def mostRecentSol(rover_name):
    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    recentSol = myData["photo_manifest"]["max_sol"]
    print("The most recent Mars sol is: {}".format(recentSol))

# Choose Rover, Sol, Camera to get the image results
def customSearch(rover_name, solNum, camera):
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/{}/photos?sol={}&camera={}&api_key={}".format(rover_name, solNum, camera, api_key)
    myData = requests.get(url)
    json_dict = myData.json()
    customSearchResult = json_dict["photos"][0]["img_src"]
    print("Opening Image...")
    return webbrowser.open_new_tab(customSearchResult)

# Return a list of Sols
def missionSol(rover_name):
    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    solNum = []
    for i in myData["photo_manifest"]["photos"]:
        solNum.append(i[u"sol"])
    print(solNum)

#If totalPhotos is greater than X, print list of sol mission numbers
def totalPhotosGreaterThan1000(rover_name):
    url = "https://api.nasa.gov/mars-photos/api/v1/manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    solNum = []
    for i in myData["photo_manifest"]["photos"]:
        if int(i[u"total_photos"]) > 500:
            solNum.append(i[u"sol"])
    print(solNum)

totalPhotosGreaterThan1000("curiosity")
#missionSol("curiosity")
#totalPhotosGreaterThan1000("curiosity")
#mostRecentSol("curiosity")
#roverMissionStatus("opportunity")
#mostRecentSolDateImage()
#"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=ENTER_YOUR_KEY"
