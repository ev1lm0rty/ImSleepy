import os

def main():
    final_list = []
    f = open("TimeTable.txt")
    lines = f.readlines()
    for i in lines:
        stripped = i.strip()
        ll = stripped.split()
        final_list.append(ll)
    final_list.pop(0)
    setCron(final_list)
    f.close()

def setCron(ff):
    # Just to be safe
    os.system("sudo cp /etc/crontab /etc/crontab.bak")
    FILENAME = "/etc/crontab"
    f = open(FILENAME , "a")
    for i in ff:
        day = i[0]
        hour = i[1]
        duration = i[2]
        course = i[3]
        final = cron(day , hour , duration , course)
        f.write(final)
        f.write("\n")
    f.close()

def cron(day , hour , duration , course):
    days = ["monday" , "tuesday" , "wednesday" , "thursday" , "friday" , "saturday"]
    d = days.index(day)
    d = d+1
    user = os.getlogin()
    command = f" {user} cd ~/ImSleepy python3 ImSleepy.py bg {course} {duration}"
    cron = f"0  {hour} * * {d} "
    final = cron + command
    return final
    
main()