#ifndef DOG_H
#define DOG_H

#include <string>
#include "Animal.h"


class Dog : public Animal{
public:
	Dog(std::string name, int weight, int numOfLegs, int numOfClaws);
	int get_numofClaws();
	void set_numofClaws(int numOfClaws);

	virtual std::string getSound();
	virtual std::string getDescription();
private:
	int numOfClaws;
};


Dog::Dog(std::string name, int weight, int num_leg, int num_claw) : Animal(name, weight, num_leg){
	this->numOfClaws = num_claw;
}

std::string Dog::getSound(){
	return "GOW GOW GOW";
}

std::string Dog::getDescription(){
	std::string a = "The Dog's name is " + Animal::getName() + "\n";
	std::string b = "It weights " + std::to_string(Animal::getWeight()) + " lb" + "\n";
	std::string c = "It has " + std::to_string(Animal::getNum_leg()) + " leg" + "\n";
	std::string d = "It has " + std::to_string(numOfClaws) + " claws" + "\n";
	std::string e = "Its sound is " + getSound() + "\n";
	std::string total = a + b + c + d + e;
	return (total);
}

int Dog::get_numofClaws(){
	return numOfClaws;
}

void Dog::set_numofClaws(int num_claw){
	this->numOfClaws = num_claw;
}


#endif