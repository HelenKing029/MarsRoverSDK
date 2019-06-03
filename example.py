import requests
import webbrowser
import json
import config
import random
import marsSDK

my_marsSDK_object = marsSDK.marsSDK()

#Testing the RandomPhoto/Number generator: 
#print(randomPhoto())

## Example Functions:
my_marsSDK_object.mostRecentSolDateImage("curiosity", "fhaz")
#print(my_marsSDK_object.roverMissionStatus("opportunity"))
#print(my_marsSDK_object.missionManifest("curiosity"))
#print(my_marsSDK_object.mostRecentSol("curiosity"))
#my_marsSDK_object.customSearch("curiosity", 1000, "rhaz")
#print(my_marsSDK_object.missionSol("curiosity"))
#print(my_marsSDK_object.totalPhotosGreaterThan("curiosity", 1500))
