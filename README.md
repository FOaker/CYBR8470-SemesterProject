# CYBR8470-SemesterProject

Project for CYBR8470

**Check the website tree [This link to raw Design](/pic/Tree.png).**

**Check the website content [This link to raw Design](/pic/content.png).**

**Check the website front page [This link to raw Design](/pic/front.png).**

**Check the website recover password [This link to raw Design](/pic/recover.png).**

**Check the website register [This link to raw Design](/pic/register.png).**

**Check the website search and page number [This link to raw Design](/pic/search.png).**

**Check the website userinfo [This link to raw Design](/pic/userinfo.png).**

**Check the website article writing [This link to raw Design](/pic/article.png).**

**Check the website admin [This link to raw Design](/pic/root.png).**


## Overview
* [Executive Project Summary](#ExecutiveSummary)
* [User Stories](#UserStories)
* [Diagrams](#Diagrams)
* [Hardening](#Hardening)
* [Deployment](#Deployment)
* [Presentation](#Presentation)
* [Prototype](#Prototype)





#### ExecutiveSummary
My web application is a blog site, why should I make a blog site? My idea is to share and record technical articles about cybersecurity here. Users can register, log in, and manage their own articles. You can use it as your own personal collection, and publish your own articles on your blog in a certain chronological order, catalog or label. Blogs are completely personal-centric. Everyone’s blog is different, and a person’s personality can be seen from each person’s blog. Through blogs and articles, you can make many like-minded bloggers. Blog is a good platform for self-exhibition and communication. Through this platform, you can make many blog friends, especially cybersecurity friends.

#### Installation
#### Option 1:
In your terminal or Pycharm

git clone https://github.com/FOaker/CYBR8470-SemesterProject.git

python manage.py migration

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

#### Option 2(some problems with docker configuration):
In Docker

git clone https://github.com/FOaker/CYBR8470-SemesterProject.git

wget https://github.com/twbs/bootstrap/releases/download/v4.1.3/bootstrap-4.1.3-dist.zip

unzip bootstrap and put two files jquery.js and popper.js in static file

cd CYBR8470-SemesterProject/blog/blog

vi settings.py(orin Atom)

ALLOWED_HOSTS = ['192.168.64.1', 'localhost']
Replace ‘192.168.64.1’ with your ip address.
to get your server ip, you need to open a Powershell and type (use ifconfig instead for Mac/Linux):
ipconfig --all
find your ipv4 address on the ip record for the ethernet card attached to your machine
alternatively, you can go to http://google.com and search for ‘my ip address

docker compose up

sudo docker run -it -d --name mysite -p 80:8000 log_web(Use commend: "docker images" check your image and replace)

sudo docker exec -it mysite /bin/bash 

python manage.py createsuperuser

sh start.sh

http://your_server_ip check website


#### Getting Started
website：127.0.0.1/article/article-list/
Register your account


#### License
The MIT License (MIT)

Copyright (c) Matthew L. Hale 2017

insert MIT License text here






#### Userstories

#### User stories 1

As an administrator, I want to moderate the blog, so I can prevent abusive behaviors and ensure policy compliance.

**Acceptance Criteria:**
* As an administrator, I can read blog articles very well.
  * “ Given I am an administrator, I can add, delete, or modify articles. Because there will always be irrelevant articles that disrupt the blog environment. With the function of managing the blog, then, I can make the technical atmosphere of the blog better. "  

#### User stories 2

As a user, I want to share and view technical articles about cybersecurity, so I can register and log in and view other technical articles.

**Acceptance Criteria:**
* Users can use the function of the blog to share their own experience. By sharing their technical experience, other users can obtain relevant knowledge and experience after viewing it. 
  * “ Given I am a user, I can register and log in and search for articles that interest me. Through my own article sharing, I can make many friends with the same hobbies. Then, I can make my Friends know me better. " 

#### User stories 3

As a technical reviewer, I want to participate in the review of technical articles, so I can write my own thoughts in the comment area.

**Acceptance Criteria:**
* Technical reviewer, I can write a review to get more people involved
  * “ Given I am technical commentator, when I am interested in this article or have questions about the article, I can write my own comments in the comment area. At the same time, more people can be involved. Then, technical commenters can be well integrated into the blog."



#### Misuser stories 1 
As a cyber spoiler, I want to modify and delete the user's articles, which has achieved the purpose of breaking the blog rules.

**Mitigations:**
* I will perform a strict verification mechanism for users, such as: data = user_login_form.cleaned_data. In addition, I will restrict permissions for each user. The user must log in and must be the user to delete it. This is the authority.

#### Misuser stories 2 
As an Internet hacker, I want to modify the user's password to get all the user's information in the blog.

**Mitigations:**
*  As an important password for identity verification, the password must be modified in a more secure way. A more common way is to send a password modification email to the user's pre-bound mailbox.

#### Misuser stories 3
As an Internet hacker, I want to conduct CSRF attacks to obtain user information.

**Mitigations:**
*  When a user visits a django site, there is a hidden field csrf_token in the form that django feedbacks to the user. This value is randomly generated on the server side and is different every time; Before the backend processes the POST request, django will verify whether the csrf_token in the requested cookie is consistent with the csrf_token in the form. If they are consistent, the request is legal, otherwise the request may be from a CSRF attack, and a 403 server is forbidden is returned.



#### Diagrams
#### Mockup
![](/pic/2.png)
**Or check the raw resource [This link to raw Design](/pic/2.png).**
#### Architecture Diagram
![](/pic/4.png)
**Or check the raw resource [This link to raw Design](/pic/4.png).**

#### Hardening
1. Use email authentication（API：Django-password-reset）to change password to ensure the integrity of the password.

2. Need to log in to operate the addition, deletion, and modification of the database

Use {% if user == article.author %} or {% if user.is_authenticated %}

Use if request.user != article.author:

        return HttpResponse("Don't have permission")
        
3. User account password matching

user = authenticate(username=data['username'], password=data['password'])

4. Inclue super user (admin)

5. Verify login decorator

import django.contrib.auth.decorators import login_required
@login_required(login_url='/userprofile/login/')

6. HTML cleaned

Use .cleaned_data to html

7. upload function

use {% csrf_token %} to avoid csrf

8. comment function

use {% csrf_token %} to avoid xss


#### Deployment
Deploy in AWS Elastic Beanstalk
![](/pic/deploy.png)
http://django-env.eba-we2t3r5u.us-west-2.elasticbeanstalk.com/


#### Presentation
https://unomaha.zoom.us/rec/share/cDm1fxIc0JGr8-wHd6x2Fe9CFErhetyMsramlBoqFgxR3ksByGwGNFAKgPeDNH0.pegN1VXwcrm47X3J?startTime=1639643902000

#### Prototype
**Check the code [This link to code](/blog/).**
