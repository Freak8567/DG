# DG
So we want to make a POST API for Storing Data into the Database and obiviously we want to see the entry which we added
So on the whole, we want one GET and POST reuqest for saving and querying the objects in the database

So what I will do is to make an API, if you make a GET request through that API you will get all the entry in the database and 
if you make a POST request it will save the data into the database.
I will be using default database of the Django, sqlite3 to keep it simple
and you can enter the url like this assuming that the Django server is running locally on port 8000

curl http://localhost:8000/api/save/    # this is basically a GET request  which gives you all the object in the database 

curl http://localhost:8000/api/save/ -d "date=23/06/2016&time=08:03 PM&message=Rishabh Kushwaha"  
#this is basically a POST request which makes an entry into the database.

Here I have  assumed we are sending only, (date, time and message )  in post request
we can send username and email also but generally we try to keep login information into differnt model(table).
here I am only considering (date, time and message ) as the JSON object in the POST Request.

I have a created a background task using Celery to send the email at the scheduled time. U can have a look at the tasks in the api folder
to get the @periodic_task which is configures to executes every 1 minutes.
So, basically what i Did was to filter the result from the database based on current time and date time every 1 minute and sends the 
filtered object the respective message through a sendEMail function, which uses smtplib module of python to send the email.In email, 
i have commented out the assumption made by me.

I have handled the message null case in the post case request but made the time and date as the required parameter
without which the POST api will not work.
I have taken date, time and message as string in the model object, which can be changed depends on the design.

Can you look into it and tell me if you want to change something.
