from bs4 import BeautifulSoup
import requests

def find_books():
    html_file = requests.get('https://books.toscrape.com/').text
    soup = BeautifulSoup(html_file, 'lxml')
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for book in books:
        book_name = book.article.h3.a.text
        price = book.find('p', class_='price_color').text
        more_info = 'https://books.toscrape.com/' + book.article.h3.a['href']
        
        with open('books.txt', 'a') as bookwrite:
            bookwrite.write(f'Name: {book_name}\n')
            bookwrite.write(f'Price: {price.strip()}\n')
            bookwrite.write(f'More info: {more_info}\n\n')
            
if __name__ == '__main__':
    find_books()
    print('All books are saved successfully')