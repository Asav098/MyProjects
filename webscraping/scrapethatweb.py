import requests
from bs4 import BeautifulSoup
import json
import os

booklist = []
if os.path.exists("books.json"):
    with open("books.json", "r") as f:
        booklist = json.load(f)
else:
    for page in range(1,51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text,"html.parser")
        books = soup.find_all("article", class_= "product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_= "price_color").text
            rating = book.p["class"][1]
            booklist.append({"title": title, "price": price, "rating": rating})

with open("books.json", "w") as f:
    json.dump(booklist,f)

def showall():
    for book in booklist:
        print(f"{book['title']}-{book['price']}")

def showfive():
    for book in booklist:
        if book['rating'] == "Five":
            print(f"⭐ {book['title']}-{book['price']}")
def showfour():
    for book in booklist:
        if book['rating'] == "Four":
            print(f"⭐ {book['title']}-{book['price']}")
def showthree():
    for book in booklist:
        if book['rating'] == "Three":
            print(f"⭐ {book['title']}-{book['price']}")
def showtwo():
    for book in booklist:
        if book['rating'] == "Two":
            print(f"⭐ {book['title']}-{book['price']}")
def showone():
    for book in booklist:
        if book['rating'] == "One":
            print(f"⭐ {book['title']}-{book['price']}")



while True:
    print("\n" + "="*30)
    print("What would you like to do?")
    print("1. View all books ")
    print("2. Show 5 star books")
    print("3. Show 4 star books")
    print("4. Show 3 star books")
    print("5. Show 2 star books")
    print("6. Show 1 star books")
    print("7. Quit")
    while True:
        try:
            n = int(input("Enter 1,2,3,4,5,6 or 7: "))
            if n in [1,2,3,4,5,6,7]:
                break
            else:
                print("Enter a valid value: ")
        except ValueError:
            break
    if n == 1 :
        showall()
    elif n==2 : 
        showfive()
    elif n==3 : 
        showfour()
    elif n==4 : 
        showthree()
    elif n==5 : 
        showtwo()
    elif n==6 : 
        showone()
    else:
        break

    