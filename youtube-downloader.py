# unfortunately it does'nt work without vpn in Iran ,but i will find another way to download videos -_-

from pytube import YouTube

# get url
url=YouTube(input('enter your link video: '))

# get audio or video
x=input('video or audio(v for video,a for audio: ')
if x=='v':
    video=url.streams.get_highest_resolution()
elif x=='a':
    video=url.streams.get_audio_only()

# get path for download
path=input('enter your path;if you want to same path enter 0: ')
if path==0:
    video.download() if x=='v' else video.download(filename=str(video.title)+".mp3")
else:
    video.download(path) if x=='v' else video.download(path,filename=str(video.title)+".mp3")



