#include <iostream>
#include "score_problem4.h"

using namespace std;


int factorial(int number){// solve for question 1
	if (number <= 1){
		return 1;
	}
	else
		return number * factorial(number - 1);
}

int multiply(int number){ // solve for question 2
	for (int i = 0; i < 3; i++){
		number = pow(2, number);
	}
	return number;
}

int math_computation(){ // solve for question 3
	int number;
	number = (3 * (4 + 8)) / ((4 * 2) / (5 - 1));
	return number;
}


int question1(){ // calculate the correct answer, compare input answer vs correct, return 1 if correct, 0 if incorrect
	int answer_solve;
	int total_correct; 
	int correct_answer_1 = factorial(5);
	cout << "5! = ";
	cin >> answer_solve;
	total_correct = check_answer(answer_solve, correct_answer_1);
	return total_correct; 
	
}

int question2(){ // calculate the correct answer, compare input answer vs correct, return 1 if correct, 0 if incorrect
	int answer_solve;
	int total_correct; 
	int correct_answer_2 = multiply(2);
	cout << "(2^(2^(2^2))) = ";
	cin >> answer_solve;
	total_correct = check_answer(answer_solve, correct_answer_2);
	return total_correct;
}

int question3(){ // calculate the correct answer, compare input answer vs correct, return 1 if correct, 0 if incorrect
	int answer_solve;
	int total_correct;
	int correct_answer_3 = math_computation();
	cout << "(3 * (4 + 8)) / ((4 * 2) / (5 - 1)) = ";
	cin >> answer_solve;
	total_correct = check_answer(answer_solve, correct_answer_3);
	return total_correct;
}

int question4(){ // calculate the correct answer, compare input answer vs correct, return 1 if correct, 0 if incorrect
	int answer_solve; int correct_answer_4;
	int total_correct;
	correct_answer_4 = 1 + 3 + 2;
	cout << "1+3+2 = ";
	cin >> answer_solve;
	total_correct = check_answer(answer_solve, correct_answer_4);
	return total_correct;
}

void problem4(){
	int correct_total = 0;
	int incorrect_total = 0;

	cout << "Welcome to our math quiz program! Please enter the answer to the following questions: " << endl;
	int correct1  = question1();
	int correct2  = question2();
	int correct3  = question3();
	int correct4  = question4();

	//cout << correct1 << "," << correct2 << "," << correct3 << "," << correct4 << endl;

	correct_total = correct1 + correct2 + correct3 + correct4; // Total correct number
	incorrect_total = 4 - correct_total; // incorrect number

	cout << "Number of correct answers: " << correct_total << endl;
	cout << "Number of incorrect answers: " << incorrect_total << endl;
	float percentage = ((float)(correct_total)/ (float)(correct_total + incorrect_total)) * 100; // calculate percentage of correct over total
	cout << "Quiz Percentage: " << percentage << " %" << endl;

}