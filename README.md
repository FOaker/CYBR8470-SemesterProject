# CYBR8470-SemesterProject
Project for CYBR8470


## Overview
* [Executive Project Summary](#project-name)
* [UserStories](#UserStories)
* [Diagrams](#Diagrams)
* [Prototype](#Prototype)


#### Executive Summary

#### Installation
#### Getting Started
#### License

#### Userstories

#### User stories 1

As a freshman, especially at the beginning of school, in this new environment, I want to meet some new people by chatting and making friends to enrich my spare time, so that I can make my life Full of enthusiasm and passion.

**Acceptance Criteria:**
* Freshman students use the chat app to make friends 
  * “Given I am a freshman, there are not many other quick ways to meet new friends, so I downloaded the chat application. When I open the chat application on my phone, I can find some people with common goals , That is, people who all want to make friends. Then, I can spend less time meeting some new friends."  

#### User stories 2

As a person with a talent for music, I want to show my talents when I get along with my friends, so that I can show my talents anytime and anywhere, so that the other person can appreciate myself.

**Acceptance Criteria:**
* Music talents use the Chat application to showcase their musical talents in order to get praise and appreciation from the other party. 
  * “Given I am a music talent and love music, I downloaded the chat application. After practicing for a while, I can show my talents in front of my friends without special musical equipment. Then, I can make my Friends know me better." 

#### User stories 3

As a person who likes to communicate with each other face to face, I want to know how far the two people are, and know my current location at any time, so that I don’t get lost and miss the opportunity to meet each other.

**Acceptance Criteria:**
* The person attending the appointment uses the chat application to get his/her current location on the earth and calculate the distance between the current location and the other party’s destination, so he/she can successfully find the other party.
  * “Given I am an appointment person and I like to communicate with each other face to face, I downloaded the chat application. When I want to know the distance of the other person but cannot determine my current location, I can open the chat application to get my current location , And then you can know the location of the other party. Then, you can successfully find the other party."



#### Misuser stories 1 
As a cyber thief who wants to know personal information, I want to use some external tools to sniff users' personal information from chat applications, so that these users' information can be used to locate, blackmail or threaten them.

**Mitigations:**
* I will not use insecure communication between the mobile application and the database, but use a more secure backend, such as Firebase for Google Cloud Platform API. Therefore, the chat mobile application data will become very difficult to capture.
* During the registration phase, the chat application will not collect actual user information except for name and email address. Because when we are designing this APP, when the user is asked to enter his/her name, we do not recommend entering the user’s real name into our system. In this case, even if the eavesdropper can obtain the user's e-mail, he/she does not know the real name that can correspond to the e-mail, so this increases the difficulty of extortion.

#### Misuser stories 2 
As an Internet hacker in social engineering, I want to collect user location information from chat applications in order to sell this information to stakeholders.

**Mitigations:**
* This chat application is actually accessing the user's location, but we use the google map API to obtain real-time information. In other words, all information is instant.



#### Diagrams
#### mockup
#### architecture diagram



#### Prototype
