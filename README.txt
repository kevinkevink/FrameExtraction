#Frame Extraction (Created in 2020 for Wisconsin Autonomous)

This was a simple frame extraction program that was designed to save a select number of frames from a series of videos, in order to create training data for the autonomous AI.

Command: python FrameExtraction.py 
Looks for folder named input that contains ONLY videos to be parsed
Places images in an already-created directory named output

-	If only reading through one video, use argument -f *file location* to read in that file.
-	If reading in a separate directory, use argument -d *directory location* to read all files in that directory.
-	If output should be somewhere else, use -o *directory location* to input images to that directory.

Default is saving one of every 32 frames, if a number other than 32 is desired use argument -n *# of frames*
