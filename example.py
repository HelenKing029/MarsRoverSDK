import requests
import webbrowser
import json
import random
from marsSDK import mostRecentSolDateImage

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
api_key = config.get('auth','api_key')

## Functions Tested:
mostRecentSolDateImage("curiosity", "fhaz") #working
#roverMissionStatus("opportunity") #working
#missionManifest("curiosity") #working
#mostRecentSol("curiosity") #working
#customSearch("curiosity", 797, "navcam") #working
#missionSol("curiosity") #working
#totalPhotosGreaterThan("curiosity", 800) #working
