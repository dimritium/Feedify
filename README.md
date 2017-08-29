# Feedify
Twitter feeds logger part of tapzo assignment, purely made in python using django framework
## Tech used
1. Django [checkout](https://www.djangoproject.com)
2. Twython twitter API [checkout](https://twython.readthedocs.io/en/latest/)
3. MaterializeCSS [checkout](http://materializecss.com)
4. FontAwesome [checkout](http://fontawesome.io)
5. DjangoGirls [checkout](https://tutorial.djangogirls.org/en/)
6. PythonAnywhere (site hosted on this!) [checkout](www.pythonanywhere.com/)

All the above mentioned, have helped me in someway or the other in making this project a big thanks to them!
## Description
Twython library is used for authentication purpose and getting user feeds, materializeCSS to materialize the ui (yeah a fan of material guidelines).After the user authenticates this app starts a thread for that user which collects latest feeds after some minutes. This app is still in beta! For bugs or hugs feel free to connect! Thank you.
**A user must wait for 5 mins for content to load,(in some conditions)** thats the delay in fetching tweets as twitter has limit of 15 request per 15 mins
### Note:
You won't be able to run this by cloning as:
1) Settings file is missing (contains important data)

Website [visit](http://feedifyme.pythonanywhere.com)
