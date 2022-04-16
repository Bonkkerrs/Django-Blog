import numpy as np
from django.shortcuts import render, HttpResponse, redirect
from course_page.models import Course, CanvasUserAccount
from canvasapi import Canvas
from django.contrib.auth import authenticate, logout
import re
import os
import datetime
from course_page.canvas_grab.get_files import File, get_file_dict, download_file

class UnpublishedAssignment():
    def __init__(self, name, due_at, unlock_at, html_url):
        self.name = name
        self.due_at = due_at
        self.unlock_at = unlock_at
        self.html_url = html_url

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self.html_url == other.html_url and self.name == other.name:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.html_url < other.html_url:
            return True
        else:
            return False

class PublishedAssignment():
    def __init__(self, name, due_at, grade, if_submitted, html_url,status):
        self.name = name
        self.due_at = due_at
        self.grade = grade
        self.if_submitted = if_submitted
        self.html_url = html_url
        self.status = status

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if self.html_url == other.html_url and self.name == other.name:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.html_url < other.html_url:
            return True
        else:
            return False



def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=username,password=pwd)
        print(request.POST)
        if user is not None:
            return redirect('/courses/')
        else:
            return render(request,'login.html')
    else:
        print(request.COOKIES)
        if request.COOKIES.get('is_login'):
            return redirect('/courses/')
        else:
            return render(request,'login.html')


def course(request):
    print(request.COOKIES)
    if request.COOKIES.get('is_login') == 'False':
        return render(request, 'login.html')
    else:
        sem = None
        # course_name = models.CharField(max_length=32)
        # course_code = models.CharField(max_length=16)
        # semester = models.CharField(max_length=16)
        # course_id = models.CharField(max_length=16)

        # 更新课表
        # API_URL = 'https://oc.sjtu.edu.cn'
        # API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
        # canvas = Canvas(API_URL, API_KEY)
        # courses = canvas.get_courses()
        # c_list = []
        # for course in courses:
        #     r = re.search(r"\((?P<semester_id>[0-9\-]+)\)-(?P<sjtu_id>[A-Za-z0-9]+)-(?P<classroom_id>.+)-(?P<name>.+)\Z",
        #                   course.course_code)
        #     r = r.groupdict()
        #
        #     course_name = r.get("name")
        #     course_code = r.get("sjtu_id")
        #     semester = r.get("semester_id")
        #     course_id = course.id
        #
        #     ret = Course.objects.filter(course_name=course_name,course_code=course_code,semester=semester,course_id=course_id)
        #     if not ret:
        #         c = Course(course_name=course_name,course_code=course_code,semester=semester,course_id=course_id)
        #         c_list.append(c)
        # Course.objects.bulk_create(c_list)
        semester_list = Course.objects.values_list("semester", flat=True)
        semester_list = np.unique(list(semester_list))
        semester_dict = {}
        for semester in semester_list:
            num = Course.objects.filter(semester=semester).count()
            semester_dict[semester] = num
        active_sem = None
        if sem != None:
            course_list = enumerate(Course.objects.filter(semester=sem))
            active_sem = sem
        else:
            course_list = enumerate(Course.objects.all())

        return render(request, 'courses.html', locals())


def courses(request, sem):
    # print(request.COOKIES)
    # if request.COOKIES.get('is_login') is None:
    #     return render(request, 'login.html')
    # else:
        # course_name = models.CharField(max_length=32)
        # course_code = models.CharField(max_length=16)
        # semester = models.CharField(max_length=16)
        # course_id = models.CharField(max_length=16)

        # 更新课表
        # API_URL = 'https://oc.sjtu.edu.cn'
        # API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
        # canvas = Canvas(API_URL, API_KEY)
        # courses = canvas.get_courses()
        # c_list = []
        # for course in courses:
        #     r = re.search(r"\((?P<semester_id>[0-9\-]+)\)-(?P<sjtu_id>[A-Za-z0-9]+)-(?P<classroom_id>.+)-(?P<name>.+)\Z",
        #                   course.course_code)
        #     r = r.groupdict()
        #
        #     course_name = r.get("name")
        #     course_code = r.get("sjtu_id")
        #     semester = r.get("semester_id")
        #     course_id = course.id
        #
        #     ret = Course.objects.filter(course_name=course_name,course_code=course_code,semester=semester,course_id=course_id)
        #     if not ret:
        #         c = Course(course_name=course_name,course_code=course_code,semester=semester,course_id=course_id)
        #         c_list.append(c)
        # Course.objects.bulk_create(c_list)
        semester_list = Course.objects.values_list("semester", flat=True)
        semester_list = np.unique(list(semester_list))
        semester_dict = {}
        total = 0
        for semester in semester_list:
            num = Course.objects.filter(semester=semester).count()
            total += num
            semester_dict[semester] = num
        active_sem = None
        if sem != '':
            course_list = enumerate(Course.objects.filter(semester=sem))
            active_sem = sem
        else:
            course_list = enumerate(Course.objects.all())
        return render(request, 'courses.html', locals())


def get_users(request):
    API_URL = 'https://oc.sjtu.edu.cn'
    API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
    canvas = Canvas(API_URL, API_KEY)
    courses = canvas.get_courses()
    u_list = []
    for course in courses:
        try:
            users = course.get_users()
            for user in users:
                userdict = user.__dict__
                canvas_id = userdict.get("id")
                name = userdict.get("short_name")
                sortable_name = userdict.get("sortable_name")
                physical_id = sortable_name.split('-')[0]
                r = re.search(
                    r"\((?P<semester_id>[0-9\-]+)\)-(?P<sjtu_id>[A-Za-z0-9]+)-(?P<classroom_id>.+)-(?P<name>.+)\Z",
                    course.course_code)
                r = r.groupdict()
                origin = r.get("name")
                semester = r.get("semester_id")
                origin_id = Course.objects.get(course_name=origin, semester=semester).id
                ret = CanvasUserAccount.objects.filter(canvas_id=canvas_id, name=name, physical_id=physical_id,
                                                       origin_id=origin_id)
                if not ret:
                    u = CanvasUserAccount(canvas_id=canvas_id, name=name, physical_id=physical_id, origin_id=origin_id)
                    u_list.append(u)
        except:
            pass

    CanvasUserAccount.objects.bulk_create(u_list)

    return render(request, 'get_users.html', locals())


def specific_course_page(request, course_id):
    c = Course.objects.get(course_id=course_id)
    course_name = c.course_name
    course_code = c.course_code
    API_URL = 'https://oc.sjtu.edu.cn'
    API_KEY = 'p7YhXM3h6PSXapEl7Fy57neXuM33zUPBTg5HXQbR21PInFp73XPSddUpGKG7fqG0'
    canvas = Canvas(API_URL, API_KEY)
    course = canvas.get_course(course_id)

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
                unlock_time += datetime.timedelta(hours=8)
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
                due_at += datetime.timedelta(hours=8)
            submission_type = assignment.get_submission(374301).submission_type
            if submission_type:
                has_submitted_submissions = True
            else:
                has_submitted_submissions = False

            if if_locked:
                upa = UnpublishedAssignment(name, due_at, unlock_time, html_url)
                unpublished.append(upa)
            else:
                assignment_id = assignment.id
                score = submission_dict[assignment_id]
                if score == None:
                    score = ''
                status = ''
                if has_submitted_submissions:
                    status = '已提交'
                elif due_at == None:
                    status = '无截止日期'
                elif due_at < now:
                    status = '超时未提交'
                else:
                    status = '未提交'
                pa = PublishedAssignment(name, due_at, score, has_submitted_submissions, html_url, status)
                published.append(pa)
    published = np.unique(published)
    unpublished = np.unique(unpublished)

    published = enumerate(published)
    unpublished = enumerate(unpublished)


    return render(request, 'course_base.html', locals())

def signout(request):
    logout(request)
    response = render(request, 'signout.html')
    response.delete_cookie('is_login')
    return response


def file_download_page(request, course_id):
    c = Course.objects.get(course_id=course_id)
    course_name = c.course_name
    file_dict, file_list = get_file_dict(course_id)
    file_list = enumerate(np.unique(file_list))
    if request.method == 'POST':
        download_list = request.POST.getlist('selected_downloads')
        directory = os.path.join('/Users/david',request.POST.get('directory'))
        print(request.POST)
        for f in download_list:
            f_obj = file_dict[int(f)]
            download_file(f_obj,directory)

        return render(request,'files.html',locals())

    else:
        return render(request,'files.html',locals())