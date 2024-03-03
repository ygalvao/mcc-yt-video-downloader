#!/usr/bin/env Python3

### Written on 2023-12-03 for the Maranatha Christian Church of Winnipeg

### Contact: Yuri Henrique Galvao, yuri@galvao.ca

import pytubefix as pt
import time

print('WARNING: This Python script will try to download the desired video\
 in 720p along with its corresponding audio.\n')

print('Run this script inside the desired folder!\n')

print('If this is not the folder you want your video saved, either\
 close the cript, copy it and paste it inside the desired folder\
 or cut and paste the video in the desired folder after the download\n''')

input('''Press "Enter" to continue.\n''')

video_url = input('Enter the URL for the video: ')

def instantiate_video_obj(
        mode:str,
        progress_func:object,
        video_url:str=None,
        video_obj:object=None,
        )->object:
    """"""

    def youtube(
            video_url=video_url,
            on_progress_callback=progress_func,
            #use_oauth=True,
            #allow_oauth_cache=True,
            )->object:
        """"""

        video = pt.YouTube(
                    video_url,
                    on_progress_callback,
                    #use_oauth,
                    #allow_oauth_cache,
                    )

        return video

    maranatha = ('maranatha', 'maranata')
    mode = maranatha if mode in maranatha else mode

    if video_url:
        while mode in video_url:
            print('''Sorry, this script can't download lives!''')
            print('''Please, try again (don't use a URL that has "live" in it).''')
            time.sleep(1)
            video_url = input('Enter the URL for the video: ')

        video = youtube()
    elif video_obj:
        video_title = video_obj.title.lower()
        video_author = video_obj.author.lower()
        while mode[0] not in video_title and mode[0] not in video_author:
            if mode[1] in video_title or mode[1] in video_author:
                break
            while mode[1] not in video_title and mode[1] not in video_author:
                if mode[0] in video_title or mode[0] in video_author:
                    break
                print('''Sorry, this script was designed to only download videos from the Maranatha Christian Church!''')
                print('''Please, try again (only use videos from channels of the Maranatha Christian Church).''')
                time.sleep(1)
                video_url = input('Enter the URL for the video: ')
                video = youtube()
                video_title = video.title

        video = video_obj if video_obj else youtube()

    return video

def check_url(video_url:str, progress_func:object)->object:
    """"""

    video_obj = instantiate_video_obj('live', progress_func=progress_func, video_url=video_url)
    video_obj = instantiate_video_obj('maranatha', progress_func=progress_func, video_obj=video_obj)

    return video_obj

def on_progress(stream:object, chunk:bytes, bytes_remaining:int)->None:
    """"""

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = round((bytes_downloaded / total_size) * 100, 2)
    print(f'''{percentage_of_completion}% complete  ''', end='\r')

if __name__ == '__main__':
    yt_video = check_url(video_url, on_progress)

    try:
        stream = yt_video.streams.get_by_itag(22)
        print(f'\nThe download of "{yt_video.title}" has started! The download can take a few minutes.\n')
        stream.download()
    except Exception as e:
        print(f'Error! Exception: {e}')
    else:
        print('\n\nVideo downloaded successfully!')
        time.sleep(5)
