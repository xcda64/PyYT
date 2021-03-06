#Modules
from pytube import YouTube
import sys
import time

#Main Code (Wrapped with try function (sys module))
try:
    print("Welcome to PyYT.")
    link = input("Enter the link:")
    yt = YouTube(link) 
    answer =  input("Download this video? (Y/N) ")
    if answer == "y":
        ys = yt.streams.get_highest_resolution()
        print("Downloading...")
        ys.download()
        print("Download complete!")
    elif answer == "n":
        exit
#If you input an interrupt, it will wait for 3 seconds, then exit.
except KeyboardInterrupt:
    time.sleep(3)
    sys.exit()
