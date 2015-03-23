#ifndef STUDENTINFO_H
#define STUDENTINFO_H

#include <string>
class StudentInfo{
public:
	StudentInfo(){};	// default constructor 
	StudentInfo(std::string student_name, char student_grade);	// overload constructor 
	void setName(std::string student_name);						// mutator set name
	void setGrade(char student_grade);						// mutator set grade

	std::string getName();										// accessor get name
	char getGrade();										// accessor get grade

private:
	std::string student_name;
	char student_grade;
};

#endif