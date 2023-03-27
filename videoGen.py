import random
from time import time
import time
import numpy
import moviepy
from moviepy.editor import *
import pygame
from datetime import datetime
import schedule
import os
import upload
import pandas as pd

def generate():
    #setting up nessisary variables
    path = ""
    desired_durration_min = 10

    with open('durration_base.txt','r') as f:
        durr_temp = f.read()
        try:
            desired_durration_min = float(durr_temp)
        except:
            print("Failed to cast desired durr base to float")

    #determining the day of the week and setting desired durrations and filepaths to match the path that goes with that day
    day = datetime.today().weekday()
    pathList = pd.read_csv('paths.csv')

    for ind, row in pathList.iterrows():
        if day == int(row['day']):
            path = row['path']
            try:
                desired_durration_min = float(row['durration'])
            except:
                print('failed to cast durration to a float for day '+day)

    #setting durration to a seconds representaion in order to match the length representaion of moviepy
    desired_durr = float(desired_durration_min * 60)

    #getting audio and video files
    files = get_files(path=path)
    vid_clip = VideoFileClip(files[0])
    aud_clip = AudioFileClip(files[1])

    #if path was random we need to set it to the folder from the first file pull so the compositions will flow well
    if path == "":
        path = files[2]

    #filling audio clip list until desired durration is met
    aud_list = [aud_clip]
    aud_durr = float(aud_clip.duration)

    while aud_durr < desired_durr:
        files = get_files(path=path)
        aud_clip = AudioFileClip(files[1])
        aud_list.append(aud_clip)
        aud_durr += float(aud_clip.duration)
  
    #filling video clip list until current audio durration is met
    vid_list = [vid_clip]
    vid_durr = float(vid_clip.duration)


    while vid_durr < aud_durr:
        files = get_files(path=path)
        vid_clip = VideoFileClip(files[0])
        vid_list.append(vid_clip)
        vid_durr += float(vid_clip.duration)

    # #setting up the final compositions
    vid_comp = concatenate_videoclips(vid_list)
    aud_comp = concatenate_audioclips(aud_list)

    #both audio and video need to end at the same time
    vid_comp = vid_comp.set_duration(aud_comp.duration)

    #writing final video
    vid_comp.audio = aud_comp

    file_name = "Mount/Done/"+datetime.today().strftime("%a-%m-%y-%H%M")+'-video.mp4'

    vid_comp.write_videofile(file_name)

    upload.upload(file_name,path)



def get_files(path = "") -> list:
    """
        If provided a path this function will fetch a random file in that filepath, if not this function will 
        fetch a random path and a random file in that path

        This function returns a list of filepaths

    """
    #If no path is provided this will select a random folder & random audio & video file for that random folder
    if path == "":
        #getting video file path
        vidFilePaths = os.listdir('Mount/Video')
        rand = random.randint(0,(len(vidFilePaths)-1))
        rand = rand-1
        vidFilePath = os.listdir('Mount/Video/'+vidFilePaths[rand])

        #getting audio file that matches video category
        audioFilePath =  os.listdir('Mount/Audio/'+vidFilePaths[rand])

        #selecting random audio and video in filepath
        vidRand = random.randint(0,(len(vidFilePath)-1))
        audrand = random.randint(0,(len(audioFilePath)-1))

        return ['Mount/Video/'+vidFilePaths[rand]+'/'+vidFilePath[vidRand] , 'Mount/Audio/'+vidFilePaths[rand]+'/'+audioFilePath[audrand],vidFilePaths[rand]]

    #If a path is provided this will return a random audio & video for that folder    
    else:
        vidFilePath = os.listdir('Mount/Video/'+path)

        #getting audio file that matches video category
        audioFilePath =  os.listdir('Mount/Audio/'+path)

        #selecting random audio and video in filepath
        vidRand = random.randint(0,(len(vidFilePath)-1))
        audrand = random.randint(0,(len(audioFilePath)-1))

        return ['Mount/Video/'+path+'/'+vidFilePath[vidRand] , 'Mount/Audio/'+path+'/'+audioFilePath[audrand]]


##########################    Job Scheduling     ################################ 

schedule.every(2).hours.do(generate)

while True:
    schedule.run_pending()
    time.sleep(1)