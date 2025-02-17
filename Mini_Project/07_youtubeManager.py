import json

yt_file = 'Mini_Project\youtube.txt'

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
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, - Duration: {video['time']} ")
    print("\n")

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Timme: " )
    videos.append ({"name" : name, "time" : time})
    save_data_helper(videos)
    

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the New Video Name ")
        time = input ("Enter the new video time: ")
        videos[index-1] = {'name' : name, 'time' : time}
        save_data_helper(videos)
    else:
        print("Invalid Video index Selected")
        
def delete_video(videos):
    list_all_video(videos)
    index = int(input("which videos index want to delete: "))
    if 1 <= index <= len(videos):
        del videos(index-1)
    else:
        print("Invalid Video index Selected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
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