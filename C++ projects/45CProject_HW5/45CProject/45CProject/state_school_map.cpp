#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>

using namespace std;

map<string, vector<string>> school_map_to_state(){

	// reading a file "input.txt" & writing to a file "output.txt" in the working directory
	ifstream file_to_read;
	
	file_to_read.open("input.txt");
	

	// check if the file's name is correct and be able to open the file successfully
	if (file_to_read.fail()){
		cout << "can't open the file " << endl;
	}

	cout << "file has been opened successfully" << endl;
	cout << endl;
	// mapping state to school_name 
	map <string, vector<string>> school_state;

	// read each line of file until the end of file is reached
	string token = "";
	while (!file_to_read.eof()){

		getline(file_to_read, token, ';');	// read each line of file with delimiter ';'
		string state = token;	// get the state string
		getline(file_to_read, token);
		string school = token; //  get the school string

		// if state is not found in map, school is unique to that state, make a map of school to state
		if (school_state.find(state) == school_state.end()){
			//cout << "can't find state " << state << endl;
			vector<string> school_list_unique;
			school_list_unique.push_back(school);
			school_state[state] = school_list_unique;
		}
		// else if key state is found in map -> there are more schools in one state
		// access the school vector (vallues) from the state (key) and append more school to that vector
		// then overload the key with the new values
		else{
			//cout << "find state " << state << endl;
			vector <string> school_had = school_state[state];
			school_had.push_back(school);
			school_state[state] = school_had;
		}

	}
	// close file to prevent memory leaks
	file_to_read.close();
	return school_state;
}