import requests
import webbrowser
import json
import config
import random
import marsSDK


my_marsSDK_object = marsSDK.marsSDK()

#print(randomPhoto())
## Functions Tested:
#my_marsSDK_object.mostRecentSolDateImage("curiosity", "fhaz")
#print(my_marsSDK_object.roverMissionStatus("opportunity"))
#my_marsSDK_object.missionManifest("curiosity")
#my_marsSDK_object.mostRecentSol("curiosity")
my_marsSDK_object.customSearch("curiosity", 780, "rhaz")
#my_marsSDK_object.missionSol("curiosity")
#print(my_marsSDK_object.totalPhotosGreaterThan("curiosity", 1000))
