#ifndef FISH_H
#define FISH_H

#include <string>
#include "Animal.h"

class Fish : public Animal{
public:
	Fish(std::string name, int weight, int numOfLegs, int numOfScales);
	int get_numOfScales();
	void set_numOfScales(int numOfScales);

	virtual std::string getSound();
	virtual std::string getDescription();

private:
	int numOfScales;
};

Fish::Fish(std::string name, int weight, int num_leg, int num_scales) : Animal(name, weight, num_leg){
	this->numOfScales = num_scales;
}

std::string Fish::getSound(){
	return "SPLASH SPLASH SPLASH";
}

int Fish::get_numOfScales(){
	return numOfScales;
}

void Fish::set_numOfScales(int num_scales){
	this->numOfScales = num_scales;
}

std::string Fish::getDescription(){
	std::string a = "The Fish's name is " + Animal::getName() + "\n";
	std::string b = "It weights " + std::to_string(Animal::getWeight()) + " lb" + "\n";
	std::string c = "It has " + std::to_string(Animal::getNum_leg()) + " leg" + "\n";
	std::string d = "It has " + std::to_string(numOfScales) + " scales" + "\n";
	std::string e = "Its sound is " + getSound() + "\n";
	std::string total = a + b + c + d + e;
	return (total);
}


#endif