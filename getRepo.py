import requests
import json

def GithubApi(username):
    userData = requests.get("https://api.github.com/users/"+ username +"/repos")
    userData = userData.json()
    print(userData)



if __name__ == "__main__":
    userInput = input("Enter Github Username: ")
    GithubApi(userInput)