# Video Voice Recognition and Editing

This is a Python script that uses Jumpcutter and Speech Recognition to edit a video and cut out the parts where a target person is not speaking. The script transcribes the audio of the input video using Speech Recognition, identifies the parts of the audio where the target person is speaking, cuts out the silent parts using Jumpcutter, and creates an output video that contains only the speech parts of the target person.

## Requirements

- Python 3.6 or later
- Jumpcutter
- Speech Recognition

## Usage

1. Clone the repository and navigate to the project directory:

git clone git@github.com:JWSaye/Bootleg-Youtube-LTR.git
cd video-voice-recognition

2. Install the required libraries:

pip install jumpcutter SpeechRecognition

3. Copy your input video file to the project directory and set its path in the script:

input_file = 'input_video.mp4'

4. Set the name of the target person in the script:

target_person = 'John Doe'

5. Run the script:

python voice_recognition.py

6. The output



YouTube Channel Video Downloader

This Python script uses the pytube library to download all the videos from a YouTube channel.
Getting Started
Prerequisites

Before running the script, you'll need to install the pytube library. You can install it using pip:

pip install pytube

Usage

To use the script, simply replace the channel_url variable with the URL of the YouTube channel you want to download, and run the script:

python download_videos.py

The script will create a directory called videos in the current working directory, and download all the videos from the specified channel into that directory.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

This script uses the pytube library, which is an open-source project developed by Nick Ficano. You can find the pytube project on GitHub at https://github.com/nficano/pytube.
