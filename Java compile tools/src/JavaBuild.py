import os, sys

cur_location = os.getcwd()
package_list = []

def get_package(path):
	lst = os.listdir(path)
	file_list = []

	for file in lst:
		if os.path.isdir(path + '/' + file):
			file_list.append(path + '/' + file)

	if len(file_list) == 0:
		return True

	for file in file_list:
		if get_package(file) == True:
			package_list.append(file)

	return False

get_package('.')

package_list = [package[1:len(package)] for package in package_list]

with open('Makefile', 'w') as make:
	for package in package_list:
		make.write('{}: {}/*.java\n\tjavac -cp . {}/*.java\n\n'.format(package[package.index('/') + 1:len(package)], package, package))
