def print_message(message, repeat_count=1):
    for x in range(repeat_count):
        print(message)

    user = input("Enter a message")
    user_count = input("inter a repeat count (optional):")

    if user and user_count:
        print_message(user, int(user_count))
    else:
        print_message(user)


print_message("Enter a message")