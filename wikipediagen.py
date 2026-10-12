import wikipedia 
import requests 
from bs4 import BeautifulSoup 
import webbrowser
import random

CONTENTS = ["Culture_and_the_arts","Geography_and_places","Health_and_fitness","History_and_events","Human_activities","Mathematics_and_logic","Natural_and_physical_sciences",
            "People_and_self","Philosophy_and_thinking","Religion_and_belief_systems","Society_and_social_sciences","Technology_and_applied_sciences"]

HEADERS= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def getLinksFromPage(url):
    
    response = requests.get(url,headers=HEADERS)

    if response.status_code != 200:
        print("Topic page not found: ", url)
        return []

    soup = BeautifulSoup(response.content,'html.parser')
    links = soup.find_all("a")

    clean = []
    for link in links:
        href = link.get("href")
        # Only collect REAL article links
        if href and href.startswith("/wiki/") and ":" not in href:
            clean.append("https://en.wikipedia.org" + href)

    return clean


def validateChoice(choice): 
    if choice > 13:
        print("Integer too big. Quitting.")
        choice = 13
    if choice < 0:
        print("Integer too small. Quitting.")
        choice = 13

    return choice 


def askTopic():
    choice = None 

    print("\n\n")
    print("What topic would you like to view? (Type the number)\n")
    print("1.\tCulture\t\t\t 2.\tGeorgraphy\n" \
    "3.\tHealth\t\t\t 4.\tHistory\n" \
    "5.\tHuman Activities\t 6.\tMathematics\n" \
    "7.\tSciences\t\t 8.\tPeople\n" \
    "9.\tPhilosophy\t\t 10.\tReligion\n" \
    "11.\tSociety\t\t\t 12.\tTechnology\n" \
    "\n" \
    "13. QUIT ")

    while choice is None:
        try:
            choice = int(input())
        except ValueError:
            print("You need to type an integer")

    choice = validateChoice(choice)

    return choice
    
def getNewChoice():
    print("\nPress ENTER for a new link"
          "\ntype X to pick a new topic" \
          "\ntype D to go deeper on this topic")
    
    userInput = str(input())

    if userInput.lower() == "x":
        print("X")
        return True 
    elif userInput.lower()== "d":
        print("D")
        return "Deeper"
    elif userInput == "":
        print("Generating new link....")
        return False
    else:
        print("Incorrect entry, taking you to menu.")
        return True 

    
def program():
    newChoice = False
    
    choice = askTopic()

    if choice == 13:
        print("Quitting..")
        return True 

    url = "https://en.wikipedia.org/wiki/Portal:Contents/"+CONTENTS[choice-1] 

    while not newChoice:
        
        links = getLinksFromPage(url)

        if not links:
            print("No links found for that topic.")
            return 
        
        print("========================================")
        print("\nYour randomly selected topic is.....\n")

        genLink = random.choice(links)
        print(genLink)

        nextChoice = getNewChoice()
        if nextChoice == "Deeper":
            url = genLink
            continue
        else:
            newChoice = nextChoice
    

def main():
    end = False 
    while not end:
        end = program()



main()