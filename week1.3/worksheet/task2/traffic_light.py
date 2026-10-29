"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"
internal_time = 0

for i in range(maxtime + 1) :
    
    if (internal_time < 4):
        state = "red"
    elif (internal_time < 7):
        state = "red_amber"
    elif (internal_time < 12):
        state = "green"
    else :
        state = "amber"
    print(f"Time {systime:03} State {state}")
    internal_time += 1
    systime += 1
    if (internal_time // 15 > 0):
        internal_time = 0
# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14