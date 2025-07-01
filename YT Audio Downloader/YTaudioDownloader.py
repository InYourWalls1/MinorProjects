import os

if os.path.isfile('new.flag'):
    print("First time using the program!")
    startChoice = input("Would you like to download yt dlp? (required for the program to run) (Y/N)")
    while (startChoice.lower() != y or startChoice.lower() != n):
        os.system('cls')
        startChoice = input("Would you like to download yt dlp? (required for the program to run) (Y/N)")
    if startChoice.lower() == y:
        os.system('python -m ensurepip --upgrade')
        os.system('pip install yt-dlp')
    print("Setup done! You may now use the program")
    os.system('del new.flag')
    
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
    print("Something went wrong, ensure yt-dlp is installed correctly")
os.system('pause')
