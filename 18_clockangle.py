#incomplete
time=input("enter the time in hh:mm format: ")
o_hour_hand=int(time[0:2])
if o_hour_hand>12:
    o_hour_hand-=12
minute_hand=(int(time[3:5]))/5
a_hour_hand=o_hour_hand + (minute_hand/12)
angle=abs((a_hour_hand-minute_hand)*30)
if angle>180:
    angle=360-angle
print("angle between the hour hand and minute hand is",angle)