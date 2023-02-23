from pytube import Channel

c = Channel("https://www.youtube.com/channel/UCOuGATIAbd2DvzJmUgXn2IQ")

print(f"Channel ID: {c.channel_id}")
print(f"Channel Name: {c.channel_name}")

print(f"Channel Title: {c.length}")

'''
# Set the channel URL
channel_url = 'https://www.youtube.com/channel/UCOuGATIAbd2DvzJmUgXn2IQ'

# Extract the channel ID from the channel URL
channel_id = channel_url.split("/")[-1]

# Get the channel object
channel = pytube.Channel(channel_url)
print(f"Channel ID: {channel_id}")
#print(f"Channel title: {channel.title}")
#print(f"Channel video count: {channel.video_count}")
# Loop through each video URL in the channel and download it
for video_url in channel.video_urls:
     print(f"Downloading {video_url}...")
     video = pytube.YouTube(video_url)
     video.streams.first().download()
     print(f"Downloaded {video_url}.")


# Get the playlist ID for the channel uploads
uploads_playlist_id = None
for playlist in channel.playlists:
    if playlist.title == "Uploads":
        uploads_playlist_id = playlist.playlist_id
        break

# Construct the playlist URL
if uploads_playlist_id:
    playlist_url = f"https://www.youtube.com/playlist?list={uploads_playlist_id}"
    print(f"Downloading videos from channel {channel_id} to playlist {playlist_url}...")
    # Download videos from the playlist here...
else:
    print(f"No uploads playlist found for channel {channel_id}.")
'''