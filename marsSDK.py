import json
import random
import requests
import webbrowser

from config import my_api_key


class MarsSDK():

    api_key = my_api_key

    base = "https://api.nasa.gov/mars-photos/api/v1/"

    #Generate a random number to be used for choosing a photo.
    def randomNumber(self):
      #for x in range(1):
      photo_num = random.randint(1,5)
      return photo_num

    #Returns the most recent image from the Curiousity Rover with the front camera
    def mostRecentSolDateImage(self, rover_name, camera):
        url = self.base + "rovers/{}/photos?sol=max_sol&camera={}&api_key={}".format(rover_name, camera, self.api_key)
        my_data = requests.get(url).json()
        rover_image = my_data.get("photos")[self.randomNumber()].get("img_src")
        return webbrowser.open_new_tab(rover_image)

    # Choose Rover, Sol, Camera to get the image results
    def customSearch(self,rover_name, solNum, camera):
        url = self.base + "rovers/{}/photos?sol={}&camera={}&api_key={}".format(rover_name, solNum, camera, self.api_key)
        my_data = requests.get(url).json()
        custom_search_result = my_data.get("photos")[self.randomNumber()].get("img_src")
        #add if image not available print"No image can be found"
        return webbrowser.open_new_tab(custom_search_result)

    #Returns the Rovers Status
    def roverMissionStatus(self, rover_name):
        url = self.base + "manifests/{}?api_key={}".format(rover_name, self.api_key)
        my_data = requests.get(url).json()
        rover_status= my_data.get("photo_manifest").get("status")
        return("The {} mission status is: {}".format(rover_name, rover_status))

    #Getting the Mission Manifest from the chosen Rover
    def missionManifest(self, rover_name):
        url = self.base + "manifests/{}?api_key={}".format(rover_name, self.api_key)
        my_data = requests.get(url).json()
        manifest = my_data.get("photo_manifest")
        return(manifest)

    #Getting the Most Recent Sol from chosen Rover
    def mostRecentSol(self, rover_name):
        url = self.base + "manifests/{}?api_key={}".format(rover_name, self.api_key)
        my_data = requests.get(url).json()
        recent_sol = my_data.get("photo_manifest").get("max_sol")
        return("The most recent Mars sol is: {}".format(recent_sol))

    # Return a list of Sols
    def missionSol(self, rover_name):
        url = self.base + "manifests/{}?api_key={}".format(rover_name, self.api_key)
        my_data = requests.get(url).json()
        sol_num = []
        for i in my_data.get("photo_manifest").get("photos"):
            sol_num.append(i[u"sol"])
        return("List of Mission Sols: {}".format(sol_num))

    #If totalPhotos is greater than X, print list of sol mission numbers
    def totalPhotosGreaterThan(self, rover_name, total_photos):
        url = self.base + "manifests/{}?api_key={}".format(rover_name, self.api_key)
        my_data = requests.get(url).json()
        sol_num = []
        for i in my_data.get("photo_manifest").get("photos"):
            if int(i[u"total_photos"]) > total_photos:
                sol_num.append(i[u"sol"])
        return(sol_num)
