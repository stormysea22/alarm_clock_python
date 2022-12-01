from datetime import datetime, timezone
from dateutil.parser import parse 
import timezones
import time

# able to set time through an input

alarm_input = input("Set time you want alarm to go off in HH:MM:ss AM/PM TZONE ")

#parse alarm time and convert to UTC
alarm_parse = parse(alarm_input, tzinfos=timezones.assemble_timezones())
alarm_time = alarm_parse.astimezone(timezone.utc)
current_time = datetime.now(timezone.utc)

#run a loop to dertimine if current time = alarm time
while alarm_time > current_time:
    time.sleep(1)
    current_time = datetime.now(timezone.utc)
    print(current_time)
    continue
print("wakeup!")
       

    

