import datetime

current_Time = datetime.datetime.now()

current_Hour = current_Time.hour #Important for wishing
current_Min = current_Time.minute #Optional

#wishing logic here
if 4 <= current_Hour < 12:
	wish = "Good Morning Boss"
	
elif 12 <= current_Hour < 18:
	wish = "Good Afternoon Boss"
	
else:
	wish = "Good Evening Boss"

print(f"{wish} the time is {current_Hour}:{current_Min}")