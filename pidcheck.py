import os


def checkpid(x):

	dirlist = os.listdir("/proc")
	for num in dirlist:
		try:
			with open(('/proc/'+num+'/cmdline'), 'r') as content_file:
				content = content_file.read()
				if x in content:
					print(num)
		except:
			pass
