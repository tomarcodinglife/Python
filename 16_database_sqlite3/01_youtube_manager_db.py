import sqlite3


con = sqlite3.connect(r"C:/Users/PC/OneDrive/Documents/Python Code\Python/16_database_sqlite3/youtube_videos.db")

cursor = con.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )

''')

def list_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, duration):
    cursor.execute("INSERT INTO  videos (name, time) VALUES (?, ?)", (name, duration))
    con.commit()

def update_video(video_id, name, duration):
    cursor.execute("UPDATE video SET name = ?, time = ?, WHERE id = ?", (name, duration, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    con.commit()

def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List Video")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Enter the video Name: ")
            duration = input("Enter the video Duration: ")
            add_video(name, duration)
        elif choice == "3":
            video_id = input("Enter video ID to updated: ")
            name = input("Enter the video Name: ")
            duration = input("Enter the video Duration: ")
            update_video(video_id, name, duration)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice ")
    con.close()
if __name__ == "__main__":
    main() 