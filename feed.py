posts = [
    "New campus coffee shop opens",
    "Python workshop this Friday",
    "Robotics club builds a drone",
    "Students launch a weather app",
    "Hackathon registration is open",
    "New library study spaces",
    "Campus Wi-Fi gets upgraded",
    "CS students build a game",
]

PAGE_SIZE = 3


def fetch_page(page):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    return posts[start:end]

def is_valid(action):
    if (action.strip().lower() == "y" 
        or action.strip().lower() == "n"):
        return True
    else:
        return False


page = 0
feed = []

while True:

    if (len(feed) >= len(posts)):
        print("\nNo more posts.")
        break

    new_posts = fetch_page(page)

    for post in new_posts:
        feed.append(post)

    print("\nYour Feed:")
    for post in feed:
        print("-", post)

    print(f"\nLoaded {len(feed)} posts")

    while not is_valid(action := input("\nScroll? (y/n): ")):
        print("Please enter y or n.")
    
    if action == "n":
        break
    elif action.strip().lower() == "y":
        page += 1
        


print("Session ended.")
