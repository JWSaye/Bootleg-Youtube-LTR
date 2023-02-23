import os
import re
import pytube

# Set the base directory for downloaded videos
#base_dir = 'Raw Videos'

# Set the channel URL
channel_url = 'https://www.youtube.com/channel/UCOuGATIAbd2DvzJmUgXn2IQ'

def download_channel_videos(channel_url):
    # Extract the channel ID from the channel URL
    channel_id = channel_url.split("/")[-1]
    print(f"Channel ID: {channel_id}")
    # Get the playlist ID for the channel uploads
    playlist_url = f"https://www.youtube.com/playlist?list=UU{channel_id}A"
    print(f"Downloading videos from channel {channel_id} to playlist {playlist_url}...")
    playlist = pytube.Playlist(playlist_url)
    # Get the title of the channel for folder naming
    channel_title = pytube.YouTube(channel_url).author
    print(f"Channel title: {channel_title}")
    # Download each video in the playlist to the specified folder
    for video in playlist.videos:
        print(f"Downloading {video.title}...")
        video.streams.get_highest_resolution().download(output_path=f"Raw Videos/{channel_title}", filename=video.title + ".mp4")
        print(f"Downloaded {video.title}.")

# Get the channel's ID from the URL
#channel_id = channel_url.split('/')[-1]

# Set the URL of the playlist you want to download
playlist_url = 'https://www.youtube.com/playlist?list=PLqK20s6leKws09Fvd_OQnAOjN2Tb0f7zV'

# Set up the YouTube video URL and download location
video_url = 'https://www.youtube.com/watch?v=SXipG3B-t9I'
download_folder = 'Raw Videos/'

# Create the channel directory
#channel_dir = os.path.join(base_dir, channel_id)
#os.makedirs(channel_dir, exist_ok=True)

# Create the download folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Search for the uploads playlist of the channel
#channel = pytube.Channel(channel_url)
#uploads_playlist_id = channel.playlists[0].playlist_id

# Create a Playlist object
playlist = pytube.Playlist(playlist_url)

# Create a YouTube object and get the video
yt = pytube.YouTube(video_url)
video = yt.streams.get_highest_resolution()

# Get the videos from the uploads playlist
#playlist = pytube.Playlist(f'https://www.youtube.com/playlist?list={uploads_playlist_id}')
#playlist._video_regex = re.compile(r"\"videoId\":\"(\S{11})\"")
#videos = playlist.video_urls

# Get the title of the playlist
playlist_title = playlist.title.replace('/', '')  # Remove any slashes in the title

# Get the file name and save path
file_name = f"{yt.title}.mp4"
save_path = os.path.join(download_folder, file_name)

# Create a subfolder for the playlist if it doesn't exist
if not os.path.exists(f'Raw Videos/{playlist_title}'):
    os.makedirs(f'Raw Videos/{playlist_title}')

# Download the video
print(f"Downloading {yt.title}...")
video.download(download_folder, filename=file_name)
print(f"Video saved to {save_path}")

# Loop through each video in the playlist and download it
for video in playlist.videos:
    # Get the title of the video and remove any slashes
    video_title = video.title.replace('/', '')

    # Set the filename of the video
    file_name_playlist = f'{video_title}.mp4'

    # Download the video if it doesn't already exist
    if not os.path.exists(file_name_playlist):
        print(f'Downloading {video_title}...')
        video.streams.get_highest_resolution().download(output_path=f'Raw Videos/{playlist_title}', filename=file_name_playlist)
    else:
        print(f'{video_title} already exists, skipping...')
"""
# Download each video
for video_url in videos:
    video = pytube.YouTube(video_url)
    video_title = video.title.replace('/', '-')  # Replace / in title with -
    video_file_path = os.path.join(channel_dir, f'{video_title}.mp4')
    if not os.path.exists(video_file_path):
        print(f'Downloading {video_file_path}')
        video.streams.get_highest_resolution().download(output_path=channel_dir, filename='{video_title}.mp4')
    else:
        print(f'Skipping {video_file_path}, already downloaded')
"""
download_channel_videos(channel_url)