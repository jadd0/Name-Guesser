import requests, bs4, threading, math

word = ["E","M"," "," "," ","E"]
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]   

def req():
    for i in range(len(words)):
        response = requests.get(f"https://www.scb.se/en/finding-statistics/sverige-i-siffror/namesearch/Search/?nameSearchInput={words[i]}")
        response = response.content
        soup = bs4.BeautifulSoup(response,'html.parser')
        head = soup.find_all("h2")[1]

        if "No results" in soup.get_text():
            pass
        else:
            print(words[i])

def start():
    words = []
    for i in range(26):
        word[2] = alphabet[i]
        for l in range(26):
            word[3] = alphabet[l]
            
            for l in range(26):
                word[4] = alphabet[l]
                if ("Y" not in word) and (word[4] != "I") and ("P" not in word) and ("Z" not in word) and ("X" not in word) and ("W" not in word) and ("K" not in word) and (word[2] != "F") and (word[2] != "M") and ("Q" not in word) and ("V" not in word) and (word[2] != "H") and ((word[2] != word[3]) and (word[3] != word[4]) and (word[4] != word[5])) and (word[2] != "T") and (word[2] != "J"):
                    with open("words.txt","a") as g:
                        g.write(f"{str(word)}\n")
                    # print(word)
                    words.append(''.join(word))
    return words

words = start()
req()
