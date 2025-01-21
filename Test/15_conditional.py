filter_textFrist = "Suicide"
filter_textSecond = "Death"
filter_textThird = "suicide"
filter_textForth = "death"
filter_textFifth = "Kill"
filter_textSixth = "kill"

message = input("Enter Your Message: ")

if(filter_textFrist in message or filter_textSecond in message or filter_textThird in message or filter_textThird in message or filter_textForth in message or filter_textFifth in message or filter_textSixth in message):
    print("Please use only valid keyword in message")
else:
    print("You are welcome. Your Message is :- ", message)

if(filter_textFrist in message):
    print(filter_textFrist, "is not valid in message")
elif(filter_textThird in message):
    print(filter_textThird, "is not valid in message")
elif(filter_textForth in message):
    print(filter_textForth, "is not valid in message")
elif(filter_textFifth in message):
    print(filter_textFifth, "is not valid in message")
elif(filter_textSixth in message):
    print(filter_textSixth, "is not valid in message")
