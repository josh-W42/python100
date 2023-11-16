# Day 30 is about errors and catching them.

# Let's say we're opening a file
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict)
# #   You can capture individual errors with except
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# #   You can capture the error message by using "as"
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# #   Else can be called if no error occurred
# else:
#     content = file.read()
#     print(content)
# #   Finally happens after everything, it is the last stage.
# finally:
#     file.close()
#     print("File was closed.")

# When would we raise our own exceptions?

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)
