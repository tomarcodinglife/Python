from pytube import YouTube

savePath = 0
link = input("Enter YT Link ")
yt= YouTube(link)
print(yt.title())
print(yt.title)