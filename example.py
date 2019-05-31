import requests
import webbrowser
import json
import random
import marsSDK
import config

my_marsSDK_object = marsSDK.marsSDK()

#print(randomPhoto())
## Functions Tested:
#mostRecentSolDateImage("curiosity", "fhaz") #working
print(my_marsSDK_object.roverMissionStatus("opportunity")) #working
#missionManifest("curiosity") #working
#mostRecentSol("curiosity") #working
#customSearch("curiosity", 797, "navcam") #working
#missionSol("curiosity") #working
#print(totalPhotosGreaterThan("curiosity", 1000)) #working
