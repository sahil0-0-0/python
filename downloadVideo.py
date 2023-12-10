import yt_dlp

url = input("Enter video link here : ")

video = {}

with yt_dlp.YoutubeDL(video) as vdo :
    vdo.download([url])

print("Video download successfully .")