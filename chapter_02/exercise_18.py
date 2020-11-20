#!/usr/bin/env python3

# (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
# current time in GMT. Revise the program so that it prompts the user ot enter the
# time zone in hours away from (offset to) GMT and displays the time in the speci-
# fied time zone. Here is a sample run:

#   Enter the time zone offset to GMT: -5 [Enter]
#   The current time is 4:50:34

import time

offset = eval(input("Enter the time zone offset to GMT: "))
currentTime = time.time() # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Adjust for offset
totalSeconds += offset * 60 * 60

# Get the current second
currentSecond = totalSeconds % 60

# Obtain the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is", currentHour, ":",
    currentMinute, ":", currentSecond)
