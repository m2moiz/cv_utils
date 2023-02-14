# cv_utils

A set of utility functions that aid in working with computer vision projects

## Youtube Downloader

A Python class for downloading YouTube videos and audio.

### Overview

The `YoutubeDownloader` class allows you to download YouTube videos and audio with just a few lines of code. It is a simple and convenient way to save your favorite videos and audio from YouTube to your local storage.

### Requirements

Before you can use the `YoutubeDownloader` class, you will need to install the following libraries:

- yt_dlp

You can install these libraries using `pip`: pip install yt-dlp

### Usage

The `YoutubeDownloader` class has two methods: `video_download` and `audio_download`. The `video_download` method downloads the best quality video available and converts it to MP4 format. The `audio_download` method downloads the audio in MP3 format.

Here's an example of how to use the `YoutubeDownloader` class:

```python
# Import the class
from youtube_downloader import YoutubeDownloader

# Creating the object
yt = YoutubeDownloader()

# Download a video
yt.video_download('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Never_Gonna_Give_You_Up.mp4', '/path/to/downloads')

# Download audio
yt.audio_download('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'Never_Gonna_Give_You_Up.mp3', '/path/to/downloads')

```

### Parameters

- link: The YouTube video link to download.

- filename (optional): The name to save the video/audio as. If not provided, the video/audio title will be used.

- location (optional): The location to save the video/audio. If not provided, the current working directory will be used.

### Limitations

- The YoutubeDownloader class depends on the yt-dlp library, which is not always up-to-date with the latest changes to the YouTube website. If you encounter any issues with downloading videos or audio, you may need to update the yt-dlp library.

- The YoutubeDownloader class downloads the best quality video or audio available. However, the actual quality of the video or audio may vary depending on the source.

- The YoutubeDownloader class does not support downloading playlists or multiple videos at once.

### Support

If you need help or have any questions, feel free to open an issue on the GitHub repository for this project.
