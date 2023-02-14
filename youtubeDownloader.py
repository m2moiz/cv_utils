import os
import yt_dlp as youtube_dl
from typing import Optional

class YoutubeDownloader:
    def video_download(self, link: str, filename: Optional[str] = None, location: Optional[str] = None):
        """
        Downloads a YouTube video in the best quality available and converts it to MP4 format.

        :param link: The YouTube video link.
        :param filename: The name to save the video as. If not provided, the video title will be used.
        :param location: The location to save the video. If not provided, the current working directory will be used.
        """

        if not os.path.exists(location):
            os.makedirs(location)
        
        if "playlist" in link:
            file_path = os.path.join(location, '%(playlist_index)s-' + filename + '.mp4') if filename else os.path.join(location, '%(playlist_index)s-%(title)s.%(ext)s')
        else:
            file_path = os.path.join(location, filename + '.mp4') if filename else os.path.join(location, '%(title)s.%(ext)s')

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'outtmpl': file_path,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

    def audio_download(self, link: str, filename: Optional[str] = None, location: Optional[str] = None):
        """
        Downloads the audio of a YouTube video in MP3 format.

        :param link: The YouTube video link.
        :param filename: The name to save the audio as. If not provided, the video title will be used.
        :param location: The location to save the audio. If not provided, the current working directory will be used.
        """

        if not os.path.exists(location):
            os.makedirs(location)

        if "playlist" in link:
            file_path = os.path.join(location, '%(playlist_index)s-' + filename + '.mp3') if filename else os.path.join(location, '%(playlist_index)s-%(title)s.mp3')
        else:
            file_path = os.path.join(location, filename + '.mp3') if filename else os.path.join(location, '%(title)s.mp3')

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': file_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])