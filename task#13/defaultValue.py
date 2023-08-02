def print_message(message, repeat_count=1):
    for x in range(repeat_count):
        print(message)

user = input("Enter a message")
user_count = input("inter a repeat count (optional):")

print_message(user, int(user_count))