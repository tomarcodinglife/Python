import pymongo
import pymongo.mongo_client
from bson import ObjectId

# please not push this type because it have data base id password
client = pymongo.MongoClient("mongodb+srv://Python:Python@cluster0.12fjp.mongodb.net/", tlsAllowInvalidCertificates = True) # this not valid idea

db = client["Python"]

video_collection = db["PythonDBFirst"]

print(video_collection)


def list_video():
    for video in video_collection.find():
        print(f"ID = {video ["_id"]}, Name = {video["name"]}, duration = {video["duration"]}")

def add_video(name, duration):
    video_collection.insert_one({"name" : name, "duration" : duration})

def update_video(video_id, new_name, new_duration):
    # video id pass with object because it is pass string and mongo db accept bson 
    video_collection.update_one({"_id" : ObjectId(video_id)}, {"$set": {"name" : new_name, "duration" : new_duration}})

def delete_video(video_id):
    video_collection.delete_one({"_id": video_id})
    


def main():
    while True:
        print("\n Welcome to the Youtube Manager App")
        print("1. List all videos")
        print("2. Add new videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_video()
        elif choice == "2":
            name = input("Please Enter Video Name: ")
            duration = input("Please Enter Video duration: ")
            add_video(name, duration)
        elif choice == "3":
            video_id = input("Please Enter Video ID to update : ")
            new_name = input("Please Enter Updated Video Name: ")
            new_duration = input("Please Enter Updated Video duration: ")
            update_video(video_id, new_name, new_duration)
        elif choice == "4":
            video_id = input("Please Enter Video ID to update : ")
            delete_video(video_id,)
        elif choice == "5":
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()