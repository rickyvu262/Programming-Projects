#include <iostream>
#include <string>
#include "Studentinfo.h"

using namespace std;


StudentInfo::StudentInfo(string name, char grade){
	this->student_name = name;
	this->student_grade = grade;
}

string StudentInfo::getName(){
	return student_name;
}

char StudentInfo::getGrade(){
	return student_grade;
}

