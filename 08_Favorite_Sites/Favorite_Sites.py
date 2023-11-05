#!/usr/bin/python3

favorite_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com/OmarSaudiy?tab=repositories",
    "linkedin": "https://www.linkedin.com/in/omarsaudiy",
    # Add more websites here
}


import webbrowser

def open_website(website_name):
    if website_name in favorite_websites:
        url = favorite_websites[website_name]
        webbrowser.open(url, new=2)  # 'new=2' opens the URL in a new tab
    else:
        print(f"Sorry, '{website_name}' is not in your list of favorite websites.")