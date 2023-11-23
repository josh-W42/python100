# import smtplib
#
# my_email = "my_email.@gmail.com"
# # To get a password to use:
# #   You could use your actual password (wouldn't recommend)
# #   Or you could use an app password (google recommends not creating these)
# password = "Yeah I'm not putting a password here"
#
# # Establish Connection Phase
#
# # Here is where you'll need the address to the smtp server that we'll route to.
# #   In our case, we'll be using gmail.
#
# # Also, when you use "with" the connection is automatically closed for you. (similar to files)
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # This line is very important! By using the smtp in TLS mode it encrypts the emails we send.
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="my_test_email@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
import random
# Working with datatime lib
#
# import datetime as dt
#
# # How to get the current year, month, day etc...
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=1, day=12, hour=3)
# print(date_of_birth)


# Small app idea by using both libs

import smtplib
import datetime as dt

my_email = "my_email.@gmail.com"
# To get a password to use:
#   You could use your actual password (wouldn't recommend)
#   Or you could use an app password (google recommends not creating these)
password = "Yeah I'm not putting a password here"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# Ok so the idea is that every monday, you would get a motivational quote
# but alone it would have to be opened everyday.
# In order to run it everyday automatically, the course suggests using python anywhere
# to run the code in the cloud and schedule when it should run.

# I will not be doing this!