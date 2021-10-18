import requests, json
import os, sys, time

if(len(sys.argv) <= 1):
	sys.exit("Contest ID not found")

url = 'https://codeforces.com/api/contest.standings?contestId=' + str(sys.argv[1]) + '&from=1&count=1'

#the idea is call the codeforces api and recieve the json data of score board
#this data include the info abt contest and score board, we dont card abt score board
#but at this tools, we dont care about the ranking of user handle
response_data = requests.post(url)
response_data_json = json.loads(response_data.text)

if(response_data_json['status'] != 'OK'):
	sys.exit(response_data_json['comment'])

contest_name = response_data_json['result']['contest']['name']

#split contest problems index from result
problems_index_list = [problem['index'] for problem in response_data_json['result']['problems']]

print("Contest name: " + contest_name)
print("Started time: " + time.ctime(response_data_json['result']['contest']['startTimeSeconds']))
print("Problems list: " + str(problems_index_list))

#change the default contest directory
contest_directory = 'W:/Coding/Contest/Codeforces/' + contest_name

if(os.path.exists(contest_directory) == False):
	os.mkdir(contest_directory)

template_signature = """/*
 * Author : DoTran
 * Created: %s
**/

""" %time.ctime(time.time())

#if you need to create script file with template
#create a cpp template file and change the path to the template file
#or delete the next 4 lines if u dont need to create a script file with template
template_path = "W:/Template/CPP Template/CPTemplate.cpp"

template_ostream = open(template_path, 'r')
str_template = template_ostream.read()
template_ostream.close()

for problem in problems_index_list:
	with open(contest_directory + "/" + problem + ".cpp", 'w') as problem_file:
		problem_file.write(template_signature)
		problem_file.write(str_template)

#generate the in/out file at contest directory
os.system("echo >\"" + contest_directory + "/inp.txt\"")
os.system("echo >\"" + contest_directory + "/out.txt\"")

#open contest folder with sublime text - change if you use a nother code editor or delete
#if you dont want to use
os.system("subl.exe \"" + contest_directory + "\"")