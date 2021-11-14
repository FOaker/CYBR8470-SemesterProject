# CYBR8470-SemesterProject
Project for CYBR8470


## Overview
* [Executive Project Summary](#ExecutiveSummary)
* [User Stories](#UserStories)
* [Diagrams](#Diagrams)
* [Prototype](#Prototype)


#### ExecutiveSummary
My web application is a blog site, why should I make a blog site? My idea is to share and record technical articles about cybersecurity here. Users can register, log in, and manage their own articles. You can use it as your own personal collection, and publish your own articles on your blog in a certain chronological order, catalog or label. Blogs are completely personal-centric. Everyone’s blog is different, and a person’s personality can be seen from each person’s blog. Through blogs and articles, you can make many like-minded bloggers. Blog is a good platform for self-exhibition and communication. Through this platform, you can make many blog friends, especially cybersecurity friends.

#### Installation
git clone https://github.com/FOaker/CYBR8470-SemesterProject.git

python manage.py migration

python manage.py migrate

python manage.py createsuperuser

Later on deploying in docker container



#### Getting Started
python manage.py migration

python manage.py migrate

python manage.py createsuperuser

website：127.0.0.1/8000


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
*  As an important password for identity verification, the password must be modified in a more secure way. A more common way is to send a password modification email to the user's pre-bound mailbox



#### Diagrams
#### Mockup
#### Architecture Diagram



#### Prototype
