# Mars Rover SDK
In this SDK you can choose from different Rovers, Cameras and Sol numbers to return different images and information from the Rovers.

## Getting Started

This is a Python implementation of the NASA Mars Rover API.

### Install Python

Download Python for your system 
https://www.python.org/downloads/

### Get an API Key

Apply for your key here: https://api.nasa.gov/index.html#apply-for-an-api-key

Mars Rover Documenation: https://api.nasa.gov/api.html#MarsPhotos

### Using the Functions

**mostRecentSolDateImage** - Returns the most recent image from the Rover selected with the camera of choice. 
(For best results Curiosity has the most image returns.) You will need to pass the parameters for the Rover name and the Camera you wish to use.

Call Example:
```   
mostRecentSolDateImage("curiosity", "rhaz")
```
In the example above you can see the Curiosity Rover has been selected with the Rear Hazard Avoidance Camera selected. 

**customSearch** - Choose Rover, Sol, Camera to get the image results

**roverMissionStatus** - Returns the Rovers Status

**missionManifest** - Returns the Mission Manifest from the chosen Rover

**mostRecentSol** - Returns the Most Recent Sol from chosen Rover

**missionSol** - Returns every mission Sol number

**totalPhotosGreaterThan** - If totalPhotos is greater than X, print list of sol mission numbers

### Mars Rovers
These are the Rovers you can choose from:
- Curiousity
- Opportunity
- Spirit

### Mars Cameras
The following is a list of cameras you can use in your search. 
(Sourced from the Mars Rover Documenation linked above)

Cameras are available for Rovers listed based on: C - Curiosity O - Opportunity S - Spirit

 - FHAZ (Front Hazard Avoidance Camera) - Available for: C, O, S
 - RHAZ (Rear Hazard Avoidance Camera) - Available for: C, O, S
 - MAST (Mast Camera) - Available for: C
 - CHEMCAM (Chemistry and Camera Complex) - Available for: C
 - MAHLI (Mars Hand Lens Imager) - Available for: C
 - MARDI (Mars Descent Imager) - Available for: C
 - NAVCAM (Navigation Camera) - Available for: C, O, S
 - PANCAM (Panoramic Camera) - Available for: O, S
 - MINITES (Miniature Thermal Emission Spectrometer (Mini-TES) - Available for: O, S

