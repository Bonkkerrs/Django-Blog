from canvasapi import Canvas
import re
API_URL = 'https://oc.sjtu.edu.cn'
API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
canvas = Canvas(API_URL, API_KEY)
courses = canvas.get_courses()
for course in courses:
        users = course.get_users()
        for user in users:
            userdict = user.__dict__
            canvas_id = userdict.get("id")
            name = userdict.get("short_name")
            sortable_name = userdict.get("sortable_name")
            physical_id = sortable_name.split('-')[0]
            r = re.search(r"\((?P<semester_id>[0-9\-]+)\)-(?P<sjtu_id>[A-Za-z0-9]+)-(?P<classroom_id>.+)-(?P<name>.+)\Z",
                          course.course_code)
            r = r.groupdict()
            print(r)
            origin = r.get("name")
            semester = r.get("semester_id")
            print(canvas_id,name,physical_id,origin)
            break
