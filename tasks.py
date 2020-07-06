import os
from celery import Celery
app = Celery('tasks', broker='amqp://localhost')

@app.task
def watchdog():
	dirlist = os.listdir("/home/user/matan/exercisewatchdog/")
	i=0
	print(dirlist)
	for num in dirlist:
		i+=1
	while(1!=0):
		dirlist1 = os.listdir("/home/user/matan/exercisewatchdog/")
		i1=0
		for num in dirlist1:
			i1+=1
		if(i1>i):
			for num in dirlist1:
				t=0
				for n in dirlist:
					if(num==n):
						t=1
				if(t==0):
					os.rename(("/home/user/matan/exercisewatchdog/"+num), "/home/user/matan/exercisewatchdog/files/"+num)
					print('moving')
