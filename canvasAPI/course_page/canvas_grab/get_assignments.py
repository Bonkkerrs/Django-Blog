from canvasapi import Canvas
import re
import datetime
class UnpublishedAssignment():
    def __init__(self, name, due_at, unlock_at, html_url):
        self.name = name
        self.due_at = due_at
        self.unlock_at = unlock_at
        self.html_url = html_url

    def __str__(self):
        return self.name

class PublishedAssignment():
    def __init__(self, name, due_at, grade, if_submitted, html_url):
        self.name = name
        self.due_at = due_at
        self.grade = grade
        self.if_submitted = if_submitted
        self.html_url = html_url

    def __str__(self):
        return self.name

API_URL = 'https://oc.sjtu.edu.cn'
API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course('44374')

submission_dict = {}
for submission in course.get_multiple_submissions():
    submission_dict[submission.assignment_id] = submission.score



assignment_groups = course.get_assignment_groups()
now = datetime.datetime.now()
unpublished = []
published = []
format = '%Y-%m-%dT%H:%M:%SZ'
for assignment_group in assignment_groups:
    for assignment in course.get_assignments():
        if_locked = None
        unlock_at = assignment.unlock_at
        if unlock_at:
            unlock_time = datetime.datetime.strptime(unlock_at, format)
            if unlock_time > now:
                if_locked = True
            else:
                if_locked = False
        else:
            if_locked = False

        name = assignment.name
        html_url = assignment.html_url
        due_at = assignment.due_at
        if due_at:
            due_at = datetime.datetime.strptime(due_at, format)
        has_submitted_submissions = assignment.has_submitted_submissions

        if if_locked:
            upa = UnpublishedAssignment(name,due_at,unlock_at,html_url)
            unpublished.append(upa)
        else:
            assignment_id = assignment.id
            score = submission_dict[assignment_id]
            pa = PublishedAssignment(name,due_at,score,has_submitted_submissions,html_url)
            published.append(pa)


print(published)
print(unpublished)



        # print(name, html_url, due_at, has_submitted_submissions)
        # print(assignment.id)







