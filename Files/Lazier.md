# Being Lazy on another level

## About
So our college provided us with free aws. Let's use it for good.
<br>
Follow the steps below and never worry about attending class again

## Steps
1. Create a AWS EC2 Instance (Ubuntu Server)
2. Login using ssh to your instance.
3. Clone the [ImSleepy](https://github.com/mrjoker05/ImSleepy) in your home dir.
4. Run it once and you will get the list of your courses in CoursesList.md file ( It will come in handy next time).
5. Close the program.
6. Open TimeTable.txt file and edit it according to your timetable.
    ```
    # Day # Start Hour # Duration # Course_Number ( From the CoursesList.md file)
    ```
7. Run the CronSet.py file ```python3 CronSet.py``` as root.
8. Leave the instance running.

## Conclusion
Your script will now run and attend your classes automatically.
<br>
P.S you can do this on your own machine (if it is up almost all the time)