# Feedify
Twitter feeds logger, purely made in python using django framework
</br><b>It's live [here](http://feedifyme.pythonanywhere.com)</b>
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
**A user must wait for 5 mins for content to update,(in some conditions)** thats the delay in fetching tweets as twitter has limit of 15 request per 15 mins
### Note:
* There was a bug due to which tweets had date of 28 August, I hope further tweets date issue to be fixed (users signed up after 29 Aug won't face issues), date issue patch is directly on production server not on GitHub
* You won't be able to run this by cloning as:
  * Settings file is missing (contains important data)


