import requests
import webbrowser
import json
import random

#api_key = "wTdsNpFtovzuN4I2Vo4xGU3SQLf8e5robl4oj9c6"

from configparser import ConfigParser
config = ConfigParser()
config.read('config.py')
api_key = config.get('auth','api_key')


base = "https://api.nasa.gov/mars-photos/api/v1/"

#Mars Rovers: Curiousity Opportunity Spirit

#Generate a random number to be used for choosing a photo.
def randomPhoto():
  for x in range(1):
    photoNum = random.randint(1,5)
    return photoNum

#Returns the most recent image from the Curiousity Rover with the front camera
def mostRecentSolDateImage(rover_name, camera):
    url = base + "rovers/{}/photos?sol=max_sol&camera={}&api_key={}".format(rover_name, camera, api_key)
    myData = requests.get(url).json()
    roverImage = myData.get("photos")[randomPhoto()].get("img_src")
    return webbrowser.open_new_tab(roverImage)

# Choose Rover, Sol, Camera to get the image results
def customSearch(rover_name, solNum, camera):
    url = base + "rovers/{}/photos?sol={}&camera={}&api_key={}".format(rover_name, solNum, camera, api_key)
    myData = requests.get(url).json()
    customSearchResult = myData.get("photos")[randomPhoto()].get("img_src")
    return webbrowser.open_new_tab(customSearchResult)

#Returns the Rovers Status
def roverMissionStatus(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    roverStatus= myData.get("photo_manifest") or {}.get("status")
    return("The {} mission status is: {}".format(rover_name, roverStatus))

#Getting the Mission Manifest from the chosen Rover
def missionManifest(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    manifest = myData.get("photo_manifest")
    return(manifest)

#Getting the Most Recent Sol from chosen Rover
def mostRecentSol(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    recentSol = myData.get("photo_manifest").get("max_sol")
    return("The most recent Mars sol is: {}".format(recentSol))

# Return a list of Sols
def missionSol(rover_name):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    solNum = []
    for i in myData.get("photo_manifest").get("photos"):
        solNum.append(i[u"sol"])
    return("List of Mission Sols: {}".format(solNum))

#If totalPhotos is greater than X, print list of sol mission numbers
def totalPhotosGreaterThan(rover_name, total_photos):
    url = base + "manifests/{}?api_key={}".format(rover_name, api_key)
    myData = requests.get(url).json()
    solNum = []
    for i in myData.get("photo_manifest").get("photos"):
        if int(i[u"total_photos"]) > total_photos:
            solNum.append(i[u"sol"])
    return(solNum)

## Functions Tested:
#mostRecentSolDateImage("curiosity", "fhaz") #working
#roverMissionStatus("opportunity") #working
#missionManifest("curiosity") #working
print(mostRecentSol("curiosity")) #working
#customSearch("curiosity", 797, "navcam") #working
#missionSol("curiosity") #working
#totalPhotosGreaterThan("curiosity", 800) #working
