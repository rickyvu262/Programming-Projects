#include <iostream> // include standard library
#include <cstdlib>
#include <ctime>

using namespace std;

#include "problem2.h"

void problem2(){
	int correct_number, guess_number;

	srand(time(NULL)); // computer will generate the random number everytime we re-run the program. 
	correct_number = rand() % (1 + 100); // a random number from 1 to 100 
	//cout << correct_number  << endl;

	cout << "Please enter a number between 0-100 inclusively: ";
	cin >> guess_number;

	//check whether number is correct by check within range and compare with correct number. 
	while (guess_number != correct_number){
		if (0 > guess_number || guess_number > 100){ 
			cout << "Invalid range, try again: ";
			cin >> guess_number;
		}

		else if (guess_number < correct_number){
			cout << "Too small, try again: ";
			cin >> guess_number;
		}
		else if (guess_number > correct_number){
			cout << "Too large, try again: ";
			cin >> guess_number;
		}
	}
	cout << "That's correct! the number is " << guess_number << endl;
}