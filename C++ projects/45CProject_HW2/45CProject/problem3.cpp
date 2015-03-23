#include <iostream> // include standard library
#include <cstdlib>
#include <ctime>


using namespace std;

#include "problem3.h"


void printNums(int n){
	if (n < 0){
		return;
	}
	cout << n << " ";
	printNums(n - 1);
}


void printNumsReverse(int n){

	if (n > 0){
		printNumsReverse(n - 1); // recursive pattern 
		cout << n << " ";
	}
	else { // base case number equal to 0
		cout << n << " ";
	}
}

int power(int base, int exponent){
	if (base == 0){
		return 0;
	}

	else if (exponent == 0){
		return 1;
	}
	else {
		return base * power(base, exponent - 1);
	}
}
bool isPrime(int num, int divisor){
	if (num == 2){
		return true;
	}
	if (num == 1){
		return false;
	}
		
	if (divisor == 1){
		return true;
	}
	else {
		if (num % divisor == 0){
			return false;
		}
		else {
			return isPrime(num, divisor - 1);
		}
	
	}
}
void problem3a(){
	// Part 3.a 
	int number;

	cout << "Please enter a positive number: ";
	cin >> number;

	printNums(number);
	cout << endl;
	printNumsReverse(number);
	cout << endl;
}
void problem3b(){
	// part 3.b
	int base, pow;
	cout << "Please enter a base: ";
	cin >> base;
	cout << "Please enter an exponent: ";
	cin >> pow;

	int result = power(base, pow);
	cout << "power (" << base << "," << pow << ") = "<< result << endl;

}
void problem3c(){
	//part 3.c
	int number; 
	int divisor = 2;
	cout << "Please Enter a positive number: ";
	cin >> number;

	if (isPrime(number, divisor) == true){
		cout << number << " is a prime number" << endl;
	}
	else{
		cout << number << " is not a prime number" << endl;
	}

}
void problem3(){
	problem3a();
	problem3b();
	problem3c();

}