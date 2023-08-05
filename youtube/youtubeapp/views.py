from django.shortcuts import render

from django.shortcuts import render
from pytube import YouTube
import os




def download_audio_from_video(video_url, output_file, download_path='.'):
    try:
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            print(f"Downloading audio from '{yt.title}'...")
            output_path = os.path.join(download_path, output_file)
            audio_stream.download(output_path=output_path)
            print(f"Download complete. Audio saved as '{output_file}' in '{download_path}'")
        else:
            print("No audio stream found for the provided URL.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")
    output_file = input("Enter the output filename (without extension): ") + ".mp3"
    download_path = input("Enter the download path (leave blank for current directory): ") or '.'
    download_audio_from_video(video_url, output_file, download_path)


def home(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        output_file = request.POST.get('output_file') + ".mp3"
        download_path = '.'  # Default to the current directory

        download_audio_from_video(video_url, output_file, download_path)

    return render(request, 'home.html')


# Create your views here.
