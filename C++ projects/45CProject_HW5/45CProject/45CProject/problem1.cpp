#include <iostream>
#include <vector>
#include <string>
#include "Studentinfo.h"
#include <algorithm>
#include <locale>


using namespace std;

// define a function to compare 2 strings
// using string::compare() to compare two strings
bool compare_name_string(StudentInfo a, StudentInfo b){
	string student_1_name = a.getName();
	string student_2_name = b.getName();
	string student_1_lower = student_1_name;
	string student_2_lower = student_2_name;

	for (int i = 0; i < student_1_name.size(); i++){
		student_1_lower[i] = tolower(student_1_name[i]);
	}
	for (int j = 0; j < student_2_name.size(); j++){
		student_2_lower[j] = tolower(student_2_name[j]);
	}
	
	return student_1_lower.compare(student_2_lower) < 0;
	
}

// insert student objects in the correct alphabetical order
vector<StudentInfo> insert_ordered(vector <StudentInfo> vector_student, StudentInfo s1){
	if (vector_student.size() == 0){
		vector_student.push_back(s1);
		return vector_student;
	}
	else if (vector_student.size() == 1){
		if (compare_name_string(vector_student[0], s1)){
			vector_student.push_back(s1);
		}
		else {
			vector_student.insert(vector_student.begin(), s1);
		}
	}
	else if (vector_student.size() > 1){
		for (vector<StudentInfo> ::iterator i = vector_student.begin(); i != vector_student.end(); i++){
			if (compare_name_string(s1, *i)) {
				i = vector_student.insert(i, s1);
				break;
			}
			else if (compare_name_string(*i, s1) == true && compare_name_string(s1, *(i + 1)) == true){
				vector_student.insert(i + 1, s1);
				break;
			}
		}
	}
	else{
		vector_student.push_back(s1);
	}
		return vector_student;
	}

void problem1(){
	cout << "Problem 1" << endl;
	cout << endl;
	// create various students StudentInfo objects 
	StudentInfo student_1("Steven Gomez", 'D');
	StudentInfo student_2("Johnathan Lam", 'B');
	StudentInfo student_3("jOHNATHAN LAM", 'A');
	StudentInfo student_4("Leresa Truong", 'C');
	StudentInfo student_5("Johnathan Lam", 'A');
	StudentInfo student_6("Aeron Huezon", 'A');
	StudentInfo student_7("aeron Huezon", 'A');

	//create a vector and insert student objects to the vector in lexigraphical order
	vector <StudentInfo> student_vector;
	student_vector = insert_ordered(student_vector, student_1);
	student_vector = insert_ordered(student_vector, student_2);
	student_vector = insert_ordered(student_vector, student_3);
	student_vector = insert_ordered(student_vector, student_4);
	student_vector = insert_ordered(student_vector, student_5);
	student_vector = insert_ordered(student_vector, student_6);
	student_vector = insert_ordered(student_vector, student_7);
	

	//Using iterator to access the element in the vector and print out these elements 
	for (vector <StudentInfo>::iterator i = student_vector.begin(); i < student_vector.end(); i++){
		StudentInfo info_student = *i; // dereference to access each studentInfo object
		cout << info_student.getName() << " earns the " << info_student.getGrade() << " grade" << endl; 
	}

}

