#!/usr/bin/env python3
"""
GitHub Profile Stats Updater
This script can be used to update dynamic content in your profile README
"""

import requests
import json
from datetime import datetime

def get_github_stats(username="nazmur96"):
    """Fetch GitHub stats using GitHub API"""
    url = f"https://api.github.com/users/{username}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        stats = {
            "public_repos": data.get("public_repos", 0),
            "followers": data.get("followers", 0),
            "following": data.get("following", 0),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return stats
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return None

if __name__ == "__main__":
    stats = get_github_stats()
    if stats:
        print(f"📊 GitHub Stats for nazmur96:")
        print(f"📁 Public Repositories: {stats['public_repos']}")
        print(f"👥 Followers: {stats['followers']}")
        print(f"👤 Following: {stats['following']}")
        print(f"🕒 Last Updated: {stats['updated_at']}")

