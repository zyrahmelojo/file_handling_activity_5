def defining_my_life():
    with open("my_life.txt", "w") as file:
        while True:
            line = input("Enter line: ")
            file.write(line + "\n")

            more = input("Are there more lines y/n? ").lower()
            if more != 'y':
                break

    print("Your text has been saved to my_life.txt")

# Run the function
defining_my_life()