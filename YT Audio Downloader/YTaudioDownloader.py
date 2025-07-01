import os

VIDEO_URL = input("Input video URL:")

index = VIDEO_URL.find('&') #truncating the url when it reaches '&' in case the user is stupid ass and puts the link as part of a playlist
if index != -1:
    VIDEO_URL = VIDEO_URL[:index]

print()    
specifiedFormat = input("Input which format you'd like to have the audio in (ex.: mp3, wav, flac) (if not set, will default to best audio):")
if (specifiedFormat != 'mp3' and
specifiedFormat != 'aac' and
specifiedFormat != 'm4a' and
specifiedFormat != 'opus' and
specifiedFormat != 'vorbis' and
specifiedFormat != 'wav' and
specifiedFormat != 'flac' and
specifiedFormat != 'alac' and
specifiedFormat != 'best'):
    specifiedFormat = "best"
    
try:
    os.system(f"yt-dlp -x --audio-format {specifiedFormat} -o \"%(title)s.%(ext)s\" {VIDEO_URL}")
    print("All Done!")
except:
    print("Stupid ass program... can't even do anything right (smth went wrong)")
os.system('pause')