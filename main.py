from pytube import YouTube

print("Welcome to the YouTube CLI Downloader.")
link = input("Enter the link:")
yt = YouTube(link)
answer =  input("Download this video? (Y/N) ")
ys = yt.streams.get_highest_resolution()
if answer == "y":
    ys = yt.streams.get_highest_resolution()
    print("Downloading...")
    ys.download("$HOME/Downloads")
    print("Download complete!")
elif answer == "n":
    exit
