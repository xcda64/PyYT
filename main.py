from pytube import YouTube
import sys
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
except KeyboardInterrupt:
    sys.exit()