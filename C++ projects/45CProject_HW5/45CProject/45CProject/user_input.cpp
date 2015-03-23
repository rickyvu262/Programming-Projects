#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

void school_names(string valid_state, map<string, vector<string>> school_dict){
	string school_name = "";
	vector<string> school_list = school_dict[valid_state];
	for (vector<string> ::iterator i = school_list.begin(); i != school_list.end(); i++){
		cout << valid_state << ": " << *i << endl;
	}
	/*for (int i = 0; i < school_list.size(); i++){
		school_name += school_list[i] + "\n";
	}
	return school_name;*/
}

void user_input(string input_state, map<string, vector<string>> school_dict){
	while (true){
		cout << "Please enter a State Abbreviation: ";
		cin >> input_state;
		if (input_state == "exit"){
			break;
		}
		else if (school_dict.find(input_state) == school_dict.end()){
			cout << "invalid state abbreviation. Please try again" << endl;
		}
		else{
			/*string school_titles = school_names(input_state, school_dict);
			cout << "The ordered list of university corresponding to " << input_state << ": " << endl;
			cout << school_titles << endl;*/
			school_names(input_state, school_dict);
		}
	}
}