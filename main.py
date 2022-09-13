from bs4 import BeautifulSoup

# read html file in the same directory
# html_file : variable
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    ########################################
    # tags = soup.find('h5')
    # tags2 = soup.find_all('h5')
    # print(tags2)
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    # for course in courses_html_tags:
    #     print(course.text)

    # courses_text_tags = soup.find_all('p')
    # for course_text in courses_text_tags:
    #     print(course_text.text)

    #######################################
    course_cards = soup.find_all('div', class_='card') # class : keyword in python, class_ : attribute for html elements
    for course in course_cards:
        # print(course)
        # print(course.h5)
        # print(course.a.text)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        # print(course_name)
        # print(course_price)
        print(f'{course_name} costs {course_price}')
