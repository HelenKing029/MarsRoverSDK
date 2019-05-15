import requests
import webbrowser
import json

api_key = "ENTER_YOUR_KEY"

base = "https://api.nasa.gov/mars-photos/api/v1/"

#Mars Rovers: Curiousity Opportunity Spirit

#Returns the most recent image from the Curiousity Rover with the front camera
def mostRecentSolDateImage():
    url = base + "rovers/curiosity/photos?sol=max_sol&camera=fhaz&api_key={}".format(api_key)
    myData = requests.get(url).json()
    roverImage = myData["photos"][5]["img_src"]
    print("Opening Image...")
    return webbrowser.open_new_tab(roverImage)

# Choose Rover, Sol, Camera to get the image results
def customSearch(rover_name, solNum, camera):
    url = base + "rovers/{}/photos?sol={}&camera={}&api_key={}".format(rover_name, solNum, camera, api_key)
    myData = requests.get(url).json()
    customSearchResult = myData["photos"][5]["img_src"]
    print("Opening Image...")
    return webbrowser.open_new_tab(customSearchResult)

#Returns the Rovers Status
def roverMissionStatus(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    roverStatus= myData["photo_manifest"]["status"]
    print("The {} mission status is: {}".format(rover_name, roverStatus))

#Getting the Mission Manifest from the chosen Rover
def missionManifest(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    manifest = myData["photo_manifest"]
    print(manifest)

#Getting the Most Recent Sol from chosen Rover
def mostRecentSol(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    recentSol = myData["photo_manifest"]["max_sol"]
    print("The most recent Mars sol is: {}".format(recentSol))

# Return a list of Sols
def missionSol(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    solNum = []
    for i in myData["photo_manifest"]["photos"]:
        solNum.append(i[u"sol"])
    print("List of Mission Sols:")
    print(solNum)

#If totalPhotos is greater than X, print list of sol mission numbers
def totalPhotosGreaterThan(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    solNum = []
    for i in myData["photo_manifest"]["photos"]:
        if int(i[u"total_photos"]) > 800:
            solNum.append(i[u"sol"])
    print(solNum)


## Functions Tested:
#mostRecentSolDateImage() #working
#roverMissionStatus("opportunity") #working
#missionManifest("curiosity") #working
#mostRecentSol("curiosity") #working
#customSearch("curiosity", 797, "navcam") #working
#missionSol("curiosity") #working
totalPhotosGreaterThan("curiosity") #working
