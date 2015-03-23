#include <iostream>
#include "Animal.h"

using namespace std;

Animal::Animal(string name, int weight, int num_leg){			//initialize constructor
	this->name = name;
	this->weight = weight;
	this->numOfLegs = num_leg;
}

string Animal::getSound(){
	return "Animal- have this sound";
}

string Animal::getDescription(){
	return "This Animal's Description";
}

string Animal::getName(){
	return name;
}

int Animal::getWeight(){
	return weight;
}

int Animal::getNum_leg(){
	return numOfLegs;
}

void Animal::setName(string name){
	this->name = name;
}

void Animal::setWeight(int weight){
	this->weight = weight;
}

void Animal::setNum_leg(int num_leg){
	this->numOfLegs = num_leg;
}