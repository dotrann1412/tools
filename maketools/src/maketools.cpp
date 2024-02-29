#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <set>
#include <map>

using namespace std;

#define vt vector
#define pb push_back

string toLower(string& s){
	for(auto& x: s) 
		if(x >= 'A' && x <= 'Z') 
			x += 32;
	return s;
}

string fileName(string& s) {
	string fname = "";
	for(int iter = 0; s[iter] != '.' && iter < s.size(); ++iter) 
		fname += s[iter];
	return fname;
}

string fileExtension(string& s) {
	string extension = "";
	for(int iter = s.size() - 1; iter >= 0 && s[iter] != '.'; --iter)
		extension = s[iter] + extension;
	return extension;
}

map<string, vt<string>> split(vt<string>& s) {
	map<string, vt<string>> result;
	for(auto x: s) {
		result[fileName(x)].pb(fileExtension(x));
	}
	return result;
}

bool makefileCreater(vt<string>& fileList)
{
	cerr << "Creating Makefile for " << fileList.size() << " file(s)." << ".\n";

	map<string, vt<string>> dependency = split(fileList);
	fstream f("Makefile", ios::out);

	f << "MAKEFLAGS += --silent\n\n";
	f << "cc = g++\n";
	f << "cflags = -std=c++17 -g -c\n\n";

	string fx;
	int entity = 0;

	for(auto x: dependency) {
		vt<string> fileExtensionList = x.second;

		if(x.second.size() == 1 && x.first != "main") continue; 

		f << x.first << ".o : ";

		for(int iter = 0; iter < fileExtensionList.size(); ++iter)
			f << x.first + "." + fileExtensionList[iter] + " ";

		f << "\n\t" << "$(cc) $(cflags) -o " << x.first + ".o " << x.first << +".cpp";
		f << "\n\n";
		if(x.first != "main")
			fx = fx + x.first + string(".o ");
		++entity;
	}

	if(entity == 0) {
		cerr << "Project not found" << '\n';
		f.close();
		system("rm -f -- makefile");
		return 0;
	}

	f << "all: main.o " << fx << '\n';
	f << "\t" << "$(cc) -std=c++17 -g -o main main.o " + fx << "\n\n";

	f << "clean:\n\trm -f -- main -f -- *.o -f -- *.exe";
	f << '\n';
	f.close();

	return 1;
}

int main(int argc, char** argv)
{
	vt<string> commandList;
	for(int i = 1; i < argc; ++i)
		commandList.pb(argv[i]);

	system("ls *.cpp *.h >tmp.file");

	vt<string> fileList;
	fstream f("tmp.file", ios::in);
	
	while(!f.eof()) {
		string s; getline(f, s);
		if(s != "\n");
			fileList.pb(s);
	}

	fileList.pop_back();
	f.close();
	system("rm -f -- tmp.file");

	for(auto x: fileList) if(x == "main.cpp") {
		bool res = makefileCreater(fileList);
		if(res) return cerr << "Create Makefile completed" << '\n', 0;
		return cerr << "Create Makefile not completed" << '\n', 1;
	}

	cerr << "main.cpp not found" << '\n';
	return 0;
}