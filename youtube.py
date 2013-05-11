import shutil
import os
import sys
import subprocess
# Settings
root_folder = './'

def download(link):

        # Create the directory for the playlist if it does not exist yet

        # Download every single video from the given playlist
        download_videos = subprocess.call(['youtube-dl', '-f', '85/84/83/82/38/37/22/18/120/35/34', 
        									'-o',' uploads/test.\%(ext)s', link])

        #download_videos.wait()
