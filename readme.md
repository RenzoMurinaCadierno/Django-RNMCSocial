RNMC Social
========================================

Overview
----------------------------------------

This one is a first attempt at a back-end multi-user blog web app I have tackled as a practice project, alongside my initial approach at Heroku for app deployment. It is up and running at https://rnmcsocial.herokuapp.com/

The idea behind this project is to let users create and join groups and post comments in them, what would be the foundation of blogging social networks like Reddit or Facebook.

Signup, login, logout, authentications, group creation and joining, posting and removing comments are all handled by Class-based views using Django framework. Since my aim here is to work at wiring the back-end, the front-end is a bit too basic, so sorry for that. It was made with Bootstrap 3 and some custom CSS.

I have put together this example up following Jose Portilla's proposed exercise on his 'Python and Django Full Stack Web Developer Bootcamp' Udemy course. Definitely check it out if you want to learn this framework, HTML, CSS, JQuery, Bootstrap and Python basics from scratch. 

Also, the background theme was copied from Thibaut Foussard's example at https://codepen.io/Thibka/pen/mWGxNj. Awesome creation, by the way.

Thank you for reading and for taking your time to check this project out!

Instructions
------------------------------------------

Nothing new other than what you basically do in a social network, pretty much intuitive.

- Create a user using the "Signup" option.
- Once the user is created (or if you already have a registered user), jump into your account with "Login".
- Check all available groups on "Groups". Click on them to join or leave.
- Post on the groups you desire using "Post".
- If you desire, you can create your own group by tapping on "Create group".
- While cheking a group's posts, you can click on the user who commented to be able to see all of their comments. It also applies to yourself. You can also view your posts by tapping on your user icon in the navbar.