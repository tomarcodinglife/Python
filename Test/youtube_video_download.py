from pytube import YouTube
link = input("Enter YT Link ")
yt= YouTube(link)
print(yt.title())
print(yt.title)