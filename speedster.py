speed_limit = int(input(" Give the speed limit of the road"))
speed = int(input("enter your speed:"))
level = (speed - speed_limit)/5
if speed < 60:
    print("OK")
elif speed > speed_limit:
    if level > 12:
        print("Yay you go to jail. demerit points:" +str (level))
    else:
        print("demerit points:" + str(level))