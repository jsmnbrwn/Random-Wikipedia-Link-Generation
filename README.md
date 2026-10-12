A command-line tool for exploring Wikipedia at random. Pick a broad topic, get a random article link from it, then keep rolling for new links or dive deeper into whatever catches your eye.

How it works
1. Choose one of Wikipedia's 12 main topic areas from the menu.
2. The program scrapes that topic's contents page and picks a random article link.
3. From there you can:
    - Enter – get another random link from the same page
    - D – go deeper: jump into the link you just got and pick a random link from that page
    - X – go back to the topic menu


  ### Requirements
  - Python3
  - Requests and BeautifulSoup4

```bash
git clone https://github.com/jsmnbrwn/Random-Wikipedia-Link-Generation
cd Random-Wikipedia-Link-Generation
pip install requests beautifulsoup4
python wikipediagen.py
```
