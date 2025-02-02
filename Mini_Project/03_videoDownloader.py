from pytube import YouTube

Videolink = YouTube("https://www.youtube.com/watch?v=NTHVTY6w2Co&list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop&index=10")
video = Videolink.streams.get_lowest_resolution()
video.download("C:/Users/PC/Downloads")