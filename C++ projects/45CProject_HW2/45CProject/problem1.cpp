#include <iostream> // include standard library
#include <string> // include string library

using namespace std;
#include "problem1.h"
#include "circle.h"
#include "Rectangle.h"
#include "triangle.h"
#include "ask_pos_input.h"

void problem1(){
	int base, height, length, width, radius;

	cout << "Please enter triangle's base: ";
	cin >>  base; // store base input in base var
	base = prom_user_positive_input(base); // ask user to input a positive number and store that new value in base

	cout << "Please enter the trianngle's height: ";
	cin >>  height; // store height input
	height = prom_user_positive_input(height);

	cout << "Please enter the rectangle's length: ";
	cin >>  length; // store length input
	length = prom_user_positive_input(length);

	cout << "Please enter the rectangle's width: ";
	cin >>  width; // store width input
	width = prom_user_positive_input(width);

	cout << "Please enter the circle's radius: ";
	cin >>  radius; // store radius input
	radius = prom_user_positive_input(radius);

	cout << "Area of triangle is " << area_triangle(base, height) <<"." << endl;
	cout << "Area of rectangle is " << area_rectangle(length,width) << "." << endl;
	cout << "Area of triangle is " << area_circle(radius) << "." << endl;

}