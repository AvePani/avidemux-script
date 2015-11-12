#!/usr/bin/env python3

'''
This script converts videos (of the most common formats) to .mp4 format (with x264 video codecs and mp3 audio codecs) using avidemux CLI utility.
Note that it looks for videos in the directory of the user's choosing and converts any video within every recursive directory.
Depends on avidemux2_cli package.
'''
import os, subprocess, sys

types_of_video_formats_to_convert = ['avi', 'wmv', 'm4v', 'mkv', 'mov', 'mpeg', 'mpg', 'mpv', 'webm', 'flv', 'ogv', 'qt', 'asf', 'rmvb']

### Convert video function ###
def convertVideo(video_file, video_file_format):
  new_video_file_name = video_file.replace('.' + video_file_format, '.mp4')
  avidemux_file_conversion_command = 'avidemux2_cli --nogui --audio-codec mp3 --video-codec x264 --output-format mp4 --load "' + video_file  + '" --save "' + new_video_file_name + '" --quit'
  subprocess.Popen(avidemux_file_conversion_command, shell=True)

### Get list of videos to convert and return value ###
def videoFilesToConvert(working_directory, video_file_format):
  list_of_video_files_to_convert = []
  video_file_extension = '.' + video_file_format
  for root, dirs, files in os.walk(working_directory):
    for video_file in files:
      if video_file_extension in video_file:
        list_of_video_files_to_convert.append(os.path.join(root, video_file))
  return list_of_video_files_to_convert

### Get video formats to convert from user input and return value ###
def fileTypesToConvert():
  while True:
    type_of_video = input("What type of video file formats would you like to convert?\n(e.g. avi, wmv, mkv, mpg, etc.)\n")
    video_file_type = type_of_video.lower()
    if video_file_type in types_of_video_formats_to_convert:
      return video_file_type
      break
    elif video_file_type.lower() == 'stop' or video_file_type.lower() == 'exit' or video_file_type.lower() == 'quit':
      sys.exit("Thank you for (not) using my script.")
    else:
      print("Sorry, I don't work with those types of files.  Please enter a different file format.\n")

### Get directory to find video files from user input and return value ###
def directoryToLookForVideoFiles():
  count = 1
  while count <=5:
    try:
      videos_root_directory = input("Inside which directory should I look to find video files to convert?\n")
      if videos_root_directory.lower() == 'stop' or videos_root_directory.lower() == 'exit' or videos_root_directory.lower() == 'quit':
        sys.exit()
      else:
        return videos_root_directory
        break
    except OSError:
      if count < 5:
        print("Sorry, I couldn't find that directory.  Please try entering another diretory.\n")
        count += 1
        pass
      else:
        sys.exit("Sorry, we've been at this for a while.  Please make sure you get the right directory first, then try running me again.")

##########

directory = directoryToLookForVideoFiles()
file_format = fileTypesToConvert()

videos_to_convert = videoFilesToConvert(directory, file_format)
print("These are the files to be converted:")
for video in videos_to_convert:
  print(videos_to_convert)
input("\nPlease press enter to continue.")

for video in videos_to_convert:
  print("Converting " + video + ' ...')
  convertVideo(video, file_format)

print('All done!')
