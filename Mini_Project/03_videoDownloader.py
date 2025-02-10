from pytube import YouTube

# Videolink = YouTube("https://www.youtube.com/watch?v=NTHVTY6w2Co&list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop&index=10")
# print(Videolink.title)
# # video = Videolink.streams.get_lowest_resolution()
# # video.download("C:/Users/PC/Downloads")


'''
# from pytube import YouTube

# URL of the YouTube video you want to download
url = 'https://www.youtube.com/watch?v=NTHVTY6w2Co&list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop&index=10'

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution stream available
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print("Download complete!")

'''

import yt_dlp

url = 'https://youtu.be/Kj2peHnI8kg?si=19z0i3A2hVVMB13Z'

# Create a YDL options dictionary
ydl_opts = {
    'format': 'best',  # download the best available quality
    'outtmpl': '%(title)s.%(ext)s'  # save the video with its title
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")

