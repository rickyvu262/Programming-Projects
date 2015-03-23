#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>

#include "user_input.h";
#include "state_school_map.h";

using namespace std;
// compare two strings' value
bool compare_school_string(string a, string b){
	return a.compare(b) < 0;
}

void read_write_input_file(){
	// part a: school_state is the map which key = string state and values are vector of string school names
	map <string, vector<string>> school_state = school_map_to_state();
	
	// write to a file "output.txt"
	ofstream file_to_write;
	file_to_write.open("output.txt", ios::app);

	// create a vector mapcopy_school that stored all the school's names 
	vector<string> mapcopy_school;
	for (map<string, vector<string>> ::iterator i = school_state.begin(); i != school_state.end(); i++){
		for (vector <string> ::iterator j = i->second.begin(); j < i->second.end(); j++) {
			sort(i->second.begin(), i->second.end(), compare_school_string);	// for each vector corresponding to that state, sort the name of school alphabetically
			file_to_write << i->first << ": " << *j << endl;					// write to in put file with state name alphabetically sorted (default by std::map) and school name alphabetically of that state
			mapcopy_school.push_back(*j);
		}
	}

	// print out the entire map alphabetically (based on school name)

	// sort mapcopy to have all the school name listed in alphabetical order
	sort(mapcopy_school.begin(), mapcopy_school.end(), compare_school_string);

	// iterate through all the school names in mapcopy_school
	// iterate through all the elements in the map school_state
	// compare the school's name of both vector mapcopy_school and map school_state, if matches -> access the key of map
	// print out state and school names (alphabetically based on school name)
	for (vector <string>::iterator j = mapcopy_school.begin(); j < mapcopy_school.end(); j++){
		for (map<string, vector<string>> ::iterator i = school_state.begin(); i != school_state.end(); i++){
			for (vector <string> ::iterator x = i->second.begin(); x < i->second.end(); x++) {
				if (*j == *x){
					cout << i->first << ": " << *j << endl;
				}
			}
		}
	}

	// part c continously ask user to input State abbreviation until user enter ="exit"
	// return all the school names corresponding to that State. 
	cout << endl;
	string input_string;
	user_input(input_string,school_state);

	// close file to write
	file_to_write.close();
}

void problem2(){
	cout << endl;
	cout << "Problem 2" << endl;
	cout << endl;
	read_write_input_file();
}