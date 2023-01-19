import os
import string


def Valid_Guest_Amount(user_input):
    valid_input = False
    while not valid_input:
        try:

            if int(user_input) < 1 or int(user_input) > 16:
                raise ValueError
            elif int(user_input) > 0 or int(user_input) < 17:
                return user_input
            else:
                user_input = guest_limit_prompt()

        except ValueError:
            guest = guest_limit_prompt()


def guest_limit_prompt():
    new_attempt = input("We accept bookings for parties"
                        "of 1, and up to 16.").strip("")
