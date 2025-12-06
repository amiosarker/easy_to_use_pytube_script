from pytubefix import YouTube
from pytubefix.cli import on_progress

# Ask the user for the file path
download_path = input("Enter download path (leave blank for current directory): ").strip()
if not download_path:
    download_path = "."  # current directory

# YouTube video URL
video_url = input("Enter url: ").strip()

# Initialize YouTube object
yt = YouTube(video_url, on_progress_callback=on_progress)
print(f"Title: {yt.title}")

# Get highest resolution stream
ys = yt.streams.get_highest_resolution()

# Download to the specified path
ys.download(output_path=download_path)

print("Download complete!")