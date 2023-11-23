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


# Small