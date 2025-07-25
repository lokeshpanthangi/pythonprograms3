from collections import Counter, defaultdict

posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]},
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120},
}

# Most Popular Tags
tag_counter = Counter(tag for post in posts for tag in post["tags"])
print("Most Popular Tags:", tag_counter.most_common())

# User Engagement Analysis
user_likes = defaultdict(int)
for post in posts:
    user_likes[post["user"]] += post["likes"]
print("User Engagement Analysis:", dict(user_likes))

# Top Posts by Likes
top_posts = sorted(posts, key=lambda x: x["likes"], reverse=True)
print("Top Posts by Likes:", top_posts)

# User Activity Summary
user_summary = {}
for user, data in users.items():
    user_posts = [post for post in posts if post["user"] == user]
    user_summary[user] = {
        "posts_count": len(user_posts),
        "total_likes": sum(post["likes"] for post in user_posts),
        "followers": data["followers"],
        "following": data["following"],
    }
print("User Activity Summary:", user_summary)



