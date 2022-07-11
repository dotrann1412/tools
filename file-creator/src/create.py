import sys, os

def file_creator(file_list):
	for file in file_list:
		if os.path.exists(file) == False:
			with open(file, 'w') as _:
				continue
		else:
			print(file + " is already existed");

def folder_creator(folder_list):
	for folder in folder_list:
		if os.path.exists(folder) == False:
			os.mkdir(folder)
		else:
			print(folder + " is already existed");

if len(sys.argv) <= 1:
	exit('Command error')

file_list = []
folder_list = []
f = False
d = False

def split_command(argv):
	for i in range(1, len(argv)):
		if argv[i] == '-d' or argv[i] == '--dir':
			d = True
			f = False
			continue
		if argv[i] == '-f' or argv[i] == '--file':
			f = True
			d = False
			continue
			
		if f == True:
			file_list.append(argv[i])
		if d == True:
			folder_list.append(argv[i])

split_command(sys.argv)
file_creator(file_list)
folder_creator(folder_list)

if len(file_list) != 0:
	print('created successfully: ' + str(file_list))

if len(folder_list) != 0:
	print('created successfully: ' + str(folder_list))