#include <iostream>
using namespace std;

int prom_user_positive_input(int number){
	while (number < 0){
		cout << "Please enter a positive value: ";
		cin >> number;
	}
	return number;
}