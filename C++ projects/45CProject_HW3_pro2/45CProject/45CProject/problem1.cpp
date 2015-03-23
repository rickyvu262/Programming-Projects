#include <iostream>
#include <string>

using namespace std;


#include "list_int.h"
#include "list_float.h"
#include "list_str.h"

void problem1(){
	cout << "Here is the implemenation of Int Type on the List class" << endl;
	list_int();
	
	cout << endl;

	cout << "Here is the implementation of Float type on the List class" << endl;
	list_float();


	cout << endl;
	cout << "Here is the implementation of String type on the List class" << endl;
	list_string(); 
}