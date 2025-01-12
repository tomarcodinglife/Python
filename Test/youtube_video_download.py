from pytube import YouTube
link = input("Enter the video link here --> ")
y_tube= YouTube(link)

print(f'Video Title-->{y_tube.title}')