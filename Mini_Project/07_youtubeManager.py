import json

yt_file = 'youtube.txt'

def load_data():
    try:
        with open(yt_file) as file:
            return json.load(file)
    except FileNotFoundError:
            return []
    
def save_data_helper(videos):
    with open (yt_file, 'w') as file:
        json.dump(videos, file) # two parameter What Write and Where Write

def list_all_video(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Timme: " )
    videos.append ({"name" : name, "time" : time})
    save_data_helper(videos)
    

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app ")
        choice = input("Enter you choice ")

        match choice:
            case "1":
                list_all_video(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()