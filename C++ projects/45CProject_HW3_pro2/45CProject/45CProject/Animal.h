#ifndef ANIMAL_H
#define ANIMAL_H

#include <string>
class Animal {
public:
	Animal() {};	// default constructor 
	Animal(std::string name, int weight, int numOfLegs);	// constructor 

	std::string getName();
	int getWeight();
	int getNum_leg();

	void setName(std::string name);
	void setWeight(int weight);
	void setNum_leg(int numOfLegs);

	virtual std::string getSound();
	virtual std::string getDescription();

private:
	std::string name;
	int weight;
	int numOfLegs;
};
#endif