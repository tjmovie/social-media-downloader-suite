import os

def banner():
    print("="*60)
    print("   ALL MEDIA DOWNLOADER PRO")
    print("   Video | Audio | Shorts | Reels | Channels")
    print("="*60)

def menu():
    print("\nChoose option:")
    print("1. Download Video")
    print("2. Download Audio (MP3)")
    print("3. Download Shorts/Reels")
    print("4. Download From Channel/Playlist")
    print("5. Exit")

def run(cmd):
    os.system(cmd)

def choose_quality():
    print("\nSelect Quality:")
    print("1. Best")
    print("2. 1080p")
    print("3. 720p")
    print("4. 480p")
    q = input("Choose: ")

    if q == "2": return "bestvideo[height<=1080]+bestaudio/best"
    if q == "3": return "bestvideo[height<=720]+bestaudio/best"
    if q == "4": return "bestvideo[height<=480]+bestaudio/best"
    return "best"

while True:
    banner()
    menu()
    choice = input("\nEnter choice: ")

    if choice == "1":
        url = input("Enter video link: ")
        quality = choose_quality()
        cmd = f'yt-dlp -f "{quality}" -o "downloads/videos/%(title)s.%(ext)s" {url}'
        run(cmd)

    elif choice == "2":
        url = input("Enter video link: ")
        cmd = f'yt-dlp -x --audio-format mp3 -o "downloads/audio/%(title)s.%(ext)s" {url}'
        run(cmd)

    elif choice == "3":
        url = input("Enter Shorts/Reels link: ")
        quality = choose_quality()
        cmd = f'yt-dlp -f "{quality}" -o "downloads/videos/%(title)s.%(ext)s" {url}'
        run(cmd)

    elif choice == "4":
        url = input("Enter channel/playlist link: ")
        num = input("How many videos to download? (0 = all): ")

        limit = ""
        if num != "0":
            limit = f"--playlist-end {num}"

        quality = choose_quality()
        cmd = f'yt-dlp {limit} -f "{quality}" -o "downloads/videos/%(playlist)s/%(title)s.%(ext)s" {url}'
        run(cmd)

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option!")
