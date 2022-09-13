from bs4 import BeautifulSoup

# read html file in the same directory
# html_file : variable
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find('h5')
    # tags2 = soup.find_all('h5')
    # print(tags2)
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    # for course in courses_html_tags:
    #     print(course.text)

    courses_text_tags = soup.find_all('p')
    for course_text in courses_text_tags:
        print(course_text.text)