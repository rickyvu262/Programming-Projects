#ifndef CHICKEN_H
#define CHICKEN_H

#include <string>
#include "Animal.h"

class Chicken : public Animal{
public:
	Chicken(std::string name, int weight, int numOfLegs, int numOfBeaks);
	int get_numOfBeaks();
	void set_numOfBeaks(int numOfBeaks);

	virtual std::string getSound();
	virtual std::string getDescription();
private:
	int numOfBeaks;
};

Chicken::Chicken(std::string name, int weight, int num_leg, int num_beaks) : Animal(name, weight, num_leg){
	this->numOfBeaks = num_beaks;
}

std::string Chicken::getSound(){
	return "WRA, WRA, WROW, WROA, WRO";
}

int Chicken::get_numOfBeaks(){
	return numOfBeaks;
}

void Chicken::set_numOfBeaks(int num_beaks){
	this->numOfBeaks = num_beaks;
}

std::string Chicken::getDescription(){
	std::string a = "The Chicken's name is " + Animal::getName() + "\n";
	std::string b = "It weights " + std::to_string(Animal::getWeight()) + " lb" + "\n";
	std::string c = "It has " + std::to_string(Animal::getNum_leg()) + " legs" + "\n";
	std::string d = "It has " + std::to_string(numOfBeaks) + " beaks" + "\n";
	std::string e = "Its sound is " + getSound() + "\n";
	std::string total = a + b + c + d + e;
	return (total);
}

#endif