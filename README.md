# Basic Image Processing Projects
---
## Basic Motion Detector
This program detects any motion in the frame; thus, it can be used to detect any intruders in the building. The program works on the assumption that the first frame is always the motionless background. 
#### File Structure
There are three files included in this project:
1. To detect motion from a live camera stream and to output it the display. 
2. To detect motion from an existing video file and to output it the display.
3. To detect motion from a file or live camera and to store the output frames into a video file.
#### Requirements
   Python3, OpenCV, numpy, imutils, argparse
#### Example
![sample](https://github.com/Fais-K/Basic_Image_Processing_Projects/blob/master/Motion%20Detector%20-%20Basic/output.gif)

## Block Counter
This program essentially finds and counts the number of blocks or shapes in an image. As an example, i have provided a tetris block image here, on which this program was able to successfully execute, identify and display the number of tetris blocks present in the image.
#### Requirements
   Python3, OpenCV, imutils, argparse
#### Example
![sample](https://github.com/Fais-K/Basic_Image_Processing_Projects/blob/master/Blocks%20Counter/Screenshot.png)
   
## Color Blocks Finder
This program identifies blocks or shapes in the image based on their color and marks a red rectangular box around the same. As an exapmle, i have provided a lego block image here, on which this program was able to successfully execute, identify and mark the chosen colored lego blocks in the image.
#### Requirements
   Python3, OpenCV, numpy, imutils, argparse
#### Example
![sample](https://github.com/Fais-K/Basic_Image_Processing_Projects/blob/master/Color%20Blocks%20Finder/Screenshot.png)

## Proximate Objects Detector
The main motive behind this project is to find the objects which are within a certain proximity limit (pixel distance). The objects which are in the close proximity, themselves and the link between them are marked red (indicating danger). The objects which are in a safe distance away from other objects are marked green (indicating safe). As an example, i have provided an image with many circles in it, which is essentially a bird eye view of a street and the circles indicates people in the street. Thus on that image this program was able to successfully execute, identify and mark the people who are social distancing and not.
#### Requirements
   Python3, OpenCV, numpy, imutils, scipy, argparse
#### Example
![sample](https://github.com/Fais-K/Basic_Image_Processing_Projects/blob/master/Proximate%20Objects%20Detector/Screenshot.png)

## Shapes Identifier
This program identifies shapes in the image, draws outline around it and displays what shape it is. 
#### Requirements
   Python3, OpenCV, numpy, imutils, argparse
#### Example
![sample](https://github.com/Fais-K/Basic_Image_Processing_Projects/blob/master/Shapes%20Identifier/Screenshot.png)


