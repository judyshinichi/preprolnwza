""" Suvarnabhumi Airport """
def main():
    """ confused mak mak """
    from_where = input().replace("(", "").replace(")", "").split(" ")
    from_ans = from_where[-1]
    to_where = input().replace("(", "").replace(")", "").split(" ")
    to_ans = to_where[-1]
    time = input().replace(":", " ").split(" ")
    timeformat = time[-1]
    if "SYD" in to_ans:
        time_ans1 = int(time[0]) + 12
        time_ans2 = int(time[1])
        to_ans = "SYD"
    elif "SGN" in to_ans:
        time_ans1 = int(time[0]) + 1
        time_ans2 = int(time[1]) + 50
        if time_ans2 >= 60:
            time_ans1 = time_ans1 + time_ans2 // 60
            time_ans2 = time_ans2 % 60
        to_ans = "SGN"
    elif "ATL" in to_ans:
        time_ans1 = int(time[0]) + 33
        time_ans2 = int(time[1]) + 55
        if time_ans2 >= 60:
            time_ans1 = time_ans1 + time_ans2 // 60
            time_ans2 = time_ans2 % 60
        to_ans = "ATL"
    elif "YVR" in to_ans:
        time_ans1 = int(time[0]) + 26
        time_ans2 = int(time[1]) + 20
        if time_ans2 >= 60:
            time_ans1 = time_ans1 + time_ans2 // 60
            time_ans2 = time_ans2 % 60
        to_ans = "YVR"
    elif "KTM" in to_ans:
        time_ans1 = int(time[0])
        time_ans2 = int(time[1]) - 15
        if time_ans2 < 0:
            time_ans1 -= 1
            time_ans2 += 60
        if time_ans2 >= 60:
            time_ans1 = time_ans1 + time_ans2 // 60
            time_ans2 = time_ans2 % 60
        to_ans = "KTM"
    while time_ans1 > 12:
        if time[-1].upper() == ("AM") and time_ans1 // 12 % 2 != 0:
            timeformat = time[-1].replace("AM", "PM")
        elif time[-1].upper() == ("PM") and time_ans1 // 12 % 2 != 0:
            timeformat = time[-1].replace("PM", "AM")
        time_ans1 -= 12
    print("%s - %s" %(from_ans, to_ans))
    print("%02d:%02d %s" %(time_ans1, time_ans2, timeformat))
main()
