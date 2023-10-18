from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # tags = soup.find('h5') # it will get you first match
    # courses_tags = soup.find_all('h5')
    # for course in courses_tags:
    #     print(course.text)
    course_containers = soup.find_all('div', class_= 'card')
    for course in course_containers:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}')