from bs4 import BeautifulSoup

# read html file in the same directory
# html_file : variable
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())