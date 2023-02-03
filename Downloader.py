import os
import time
import subprocess

# This requires: yt-dlp (Recommended) or youtube-dl(simply change all "yt-dlp" arugments and variables to "youtube-dl" or whatever alias you may use).
# This script creates a subprocess in terminator, you may need to change "terminator" to your terminal name e.g "gnome-terminal" for gnome or "konsole" for KDE etc...  
while True:  # infinite loop

    # check if yt-dlp is running
    process_name = "yt-dlp"
    tmp = os.popen("ps -Af").read()

    if process_name in tmp[:]:
        print(f"{process_name} is running")
        time.sleep(30)  # sleep for 30 seconds
    else:
        subprocess.run(["terminator", "-e", "yt-dlp URL"]) # runs yt-dlp with arg, under a subprocess in terminator
        time.sleep(30) #sleep for 30 seconds
