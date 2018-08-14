# Overview
Used YOLO to recognize original object (Eggplant)

# Difficulty
Eggplant is difficult to detect using OpenCV,
due to its darkness that cannot be classified between shadow and the object itself.

# How to make YOLO learn the original object
1. Collect Images (from ImageNet) 
2. Annotate By Yourself by using [BBox-Label-Tool](https://github.com/puzzledqs/BBox-Label-Tool)
3. Divide into Training Sets and Testing Sets
4. Preparing Some Config Files needed for YOLO

5. Install YOLO V3 from [darknet](https://pjreddie.com/darknet/yolo/)
6. Make it Learn
