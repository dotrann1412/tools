import os, sys, re, regex

package_list = []
script_file_list = []
main_file_list = []

main_function_based = "publicstaticvoidmain(String[]args)"

def build_project_file_tree(path):
	lst = os.listdir(path)
	file_list = []

	for file in lst:
		if os.path.isdir(path + '/' + file):
			file_list.append(path + '/' + file)
		elif file.find(".java") != -1:
			script_file_list.append(path + '/' + file)

	if len(file_list) == 0:
		return True

	for file in file_list:
		if build_project_file_tree(file) == True:
			package_list.append(file)

	return False

build_project_file_tree('.')

#https://stackoverflow.com/questions/2319019/using-regex-to-remove-comments-from-source-files
def remove_comments(string):
	pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
	# first group captures quoted strings (double or single)
	# second group captures comments (//single-line or /* multi-line */)
	regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
	def _replacer(match):
		# if the 2nd group (capturing comments) is not None,
		# it means we have captured a non-quoted (real) comment string.
		if match.group(2) is not None:
			return "" # so we will return empty to remove the comment
		else: # otherwise, we will return the 1st group
			return match.group(1) # captured quoted-string
	return re.sub(r'".+?"' ,"",regex.sub(_replacer, string))

def detect_main_function():
	for file in script_file_list:
		scriptlines = ""
		with open(file, 'r') as script_file:
			scriptlines = script_file.readlines();
		script = ""
		for line in scriptlines:
			line = line.strip().replace('{', '').replace('}', '').replace(' ', '')
			if len(line) == 0:
				continue
			script += line + '\n'

		script = remove_comments(script)
		print(script)
		if script.find(main_function_based) != -1:
			main_file_list.append(file)

package_list = [package[1:len(package)] for package in package_list]
detect_main_function()

with open('Makefile', 'w') as make:
	make.write('MAKEFLAGS += --silent\n')
	destination_file_str = ""
	for package in package_list:
		make.write('{}.class: {}/*.java\n\tjavac -cp . {}/*.java -d .\n\n'.format(package[package.index('/') + 1:len(package)], package, package))
		destination_file_str += "{}/*.class ".format(package)
	make.write('clean:\n\t{}'.format(destination_file_str))
