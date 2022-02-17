import cv2
import os
import argparse

def video_to_frames(file, output, num):
    file_name = os.path.basename(file)
    fps = int(num)
    vidcap = cv2.VideoCapture(file)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            if(count % fps == 0):
                path = os.path.join(output, '%s%d.png') % (file_name, count)
                cv2.imwrite(path,image)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Description for my parser")
    parser.add_argument("-f", "--file", help = "location of video that will be split.", required = False, default = "")
    parser.add_argument("-d", "--directory", help = "location of directory of videos that will be split", required = False, default = "input")
    parser.add_argument("-o", "--output", help = "directory images will go to", required = False, default = "output")
    parser.add_argument("-n", "--frames", help = "for n frames, 1 out of every n frames will be saved", required = False, default = "32")
        
    argument = parser.parse_args()

    if((argument.file and argument.directory) and argument.directory != "input"):
        print("Cannot have both an input file and directory.\n")
        exit()

    if(argument.file):
        #read in file
        print("processing ",argument.file, "...")
        video_to_frames(argument.file, argument.output, argument.frames)
    else:
        #read in from directory
        for filename in os.listdir(argument.directory):
            print("processing ",filename, "...")
            file = os.path.abspath(os.path.join(argument.directory,filename))
            video_to_frames(file, argument.output, argument.frames)
        print("Done!\n")
