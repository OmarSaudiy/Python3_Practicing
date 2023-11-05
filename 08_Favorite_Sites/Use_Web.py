#!/usr/bin/python3

import Favorite_Sites as fs
def print_menu():
    print("Your Favorite Websites:")
    for website_name in fs.favorite_websites:
        print(f"- {website_name}")
    print("Enter the name of the website you want to open, or type 'exit' to quit.")

if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            fs.open_website(choice)