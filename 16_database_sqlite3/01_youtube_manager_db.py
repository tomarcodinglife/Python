import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY
               name TEXT NOT NULL
               time TEXT NOT NULL
               )

''')

def list_video():
    pass

def add_video():
    pass

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List Video")
        print("2. Add Video")
        print("3. Update Video")
        print("5. Delete Video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Enter the video Name: ")
            duration = input("Enter the video Duration: ")
            add_video(name, duration)
        elif choice == "3":
            input("Enter video ID to updated ")
            name = input("Enter the video Name: ")
            duration = input("Enter the video Duration: ")
            add_video(name, duration)

if __name__ == "__main__":
    main()