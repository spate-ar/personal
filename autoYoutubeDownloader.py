# youtube to mp4
from pytube import YouTube
from pytube import Playlist
import datetime
import time
import os



def downloader(link, SAVE_PATH):
    try: 
          
        # object creation using YouTube
        yt = YouTube(link)
    except: 
          
        #to handle exception 
        print("Connection Error") 
    try: 
        # downloading the video
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
        
    except: 
        print("Some Error!") 

SAVE_PATH = "C:/autoDownloader" #change to destination file location
dynamo= Playlist('https://www.youtube.com/watch?v=HxigGkgWeuw&list=UUUavkI6ArT44SRiAtnoN45Q') #change to desired playlist
link=dynamo.video_urls
#set up never ending loop that tries to download every hour
while True:
    for i in link: #scans all videos in playlist
        if not os.path.isfile(SAVE_PATH+"/"+YouTube(i).title+".mp4"): #if video is not in playlist, then add it
            downloader(i, SAVE_PATH)
    print('sleep')
    time.sleep(3600) #wait an hour and check again
    
print('Task Completed!') 
