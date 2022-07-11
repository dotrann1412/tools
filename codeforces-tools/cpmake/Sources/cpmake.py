import os, sys, time

if(len(sys.argv) <= 1):
	sys.exit("Problems not found")

problems_list = [problem for problem in sys.argv[1:len(sys.argv)]]

template_signature = """/*
 * Author : DoTran
 * Created: %s
**/

""" %time.ctime(time.time())

#if you need to create script file with template
#create a cpp template file and change the path to the template file
#or delete the next 4 lines if u dont need to create a script file with template
template_path = "/mnt/w/Template/CPP Template/CPTemplate.cpp"

template_ostream = open(template_path, 'r')
str_template = template_ostream.read()
template_ostream.close()

for problem in problems_list:
	with open(problem + ".cpp", 'w') as problem_file:
		problem_file.write(template_signature)
		problem_file.write(str_template) #delete this line if u dont need to use template

print("Created script file(s) for: " + str(problems_list))