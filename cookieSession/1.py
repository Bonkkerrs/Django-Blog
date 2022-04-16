from canvasapi import Canvas
API_URL = 'https://oc.sjtu.edu.cn'
API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
canvas = Canvas(API_URL,API_KEY)
courses = canvas.get_courses()

for course in courses:
    # assignments = course.get_assignments()
    # for assignment in assignments:
    #     print(assignment.__str__)
    print(course.course_code)
    



