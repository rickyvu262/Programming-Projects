#ifndef SPIDER_H
#define SPIDER_H

#include <string>
#include "Animal.h"

class Spider : public Animal{
public:
	Spider(std::string name, int weight, int numOfLegs, bool isVenomous);
	virtual std::string getSound();
	virtual std::string getDescription();
private:
	bool isVenomous;
	std::string poison;
};

Spider::Spider(std::string name, int weight, int num_leg, bool venomous) : Animal(name, weight, num_leg){
	this->isVenomous = venomous;
}

std::string Spider::getSound(){
	return "HIZZ HIZZ HIZZ";
}

std::string Spider::getDescription(){
	std::string a = "The Spider's name is " + Animal::getName() + "\n";
	std::string b = "It weights " + std::to_string(Animal::getWeight()) + " lb" + "\n";
	std::string c = "It has " + std::to_string(Animal::getNum_leg()) + " leg" + "\n";
	if (isVenomous == true){
		poison = "It is poison.";
	}
	else {
		poison = "It is not poison.";
	}
	std::string e = "Its sound is " + getSound() + "\n";
	std::string total = a + b + c + poison + e;
	return (total);
}


#endif