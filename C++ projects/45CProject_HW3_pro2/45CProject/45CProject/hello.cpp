/*

#include <iostream>
#include <string>

using namespace std;


class Dog : public Animal{
public:
	Dog(string name, int weight, int numOfLegs, int numOfClaws);
	int get_numofClaws();
	void set_numofClaws(int numOfClaws);

	virtual string getSound();
	virtual string getDescription();
private:
	int numOfClaws;
};


Dog::Dog(string name, int weight, int num_leg, int num_claw) : Animal(name, weight, num_leg){
	this->numOfClaws = num_claw;
}

string Dog::getSound(){
	return "GOW GOW GOW";
}

string Dog::getDescription(){
	string a  = "The Dog's name is " + Animal::getName() + "\n";
	string b =  "It weights " + to_string(Animal::getWeight()) + " lb" + "\n";
	string c = "It has " + to_string(Animal::getNum_leg()) + " leg" + "\n";
	string d = "It has " + to_string(numOfClaws) + " claws" + "\n";
	string e = "Its sound is " + getSound() + "\n";
	string total = a+b+c+d+e;
	return (total);
}

int Dog::get_numofClaws(){
	return numOfClaws;
}

void Dog::set_numofClaws(int num_claw){
	this->numOfClaws = num_claw;
}

class Fish : public Animal{
public:
	Fish(string name, int weight, int numOfLegs, int numOfScales);
	int get_numOfScales();
	void set_numOfScales(int numOfScales);

	virtual string getSound();
	virtual string getDescription();

private:
	int numOfScales;
};

Fish::Fish(string name, int weight, int num_leg, int num_scales) : Animal(name, weight, num_leg){
	this->numOfScales = num_scales;
}

string Fish::getSound(){
	return "SPLASH SPLASH SPLASH";
}

int Fish::get_numOfScales(){
	return numOfScales;
}

void Fish::set_numOfScales(int num_scales){
	this->numOfScales = num_scales;
}

string Fish::getDescription(){
	string a = "The Fish's name is " + Animal::getName() + "\n";
	string b = "It weights " + to_string(Animal::getWeight()) + " lb" + "\n";
	string c = "It has " + to_string(Animal::getNum_leg()) + " leg" + "\n";
	string d = "It has " + to_string(numOfScales) + " scales" + "\n";
	string e = "Its sound is " + getSound() + "\n";
	string total = a + b + c + d + e;
	return (total);
}

class Chicken : public Animal{
public:
	Chicken(string name, int weight, int numOfLegs, int numOfBeaks);
	int get_numOfBeaks();
	void set_numOfBeaks(int numOfBeaks);

	virtual string getSound();
	virtual string getDescription();
private:
	int numOfBeaks;
};

Chicken::Chicken(string name, int weight, int num_leg, int num_beaks) : Animal(name, weight, num_leg){
	this->numOfBeaks = num_beaks;
}

string Chicken::getSound(){
	return "WRA, WRA, WROW, WROA, WRO";
}

int Chicken::get_numOfBeaks(){
	return numOfBeaks;
}

void Chicken::set_numOfBeaks(int num_beaks){
	this->numOfBeaks = num_beaks;
}

string Chicken::getDescription(){
	string a = "The Chicken's name is " + Animal::getName() + "\n";
	string b = "It weights " + to_string(Animal::getWeight()) + " lb" + "\n";
	string c = "It has " + to_string(Animal::getNum_leg()) + " legs" + "\n";
	string d = "It has " + to_string(numOfBeaks) + " beaks" + "\n";
	string e = "Its sound is " + getSound() + "\n";
	string total = a + b + c + d + e;
	return (total);
}

class Spider : public Animal{
public:
	Spider(string name, int weight, int numOfLegs, bool isVenomous);
	virtual string getSound();
	virtual string getDescription();
private:
	bool isVenomous;
};

Spider::Spider(string name, int weight, int num_leg, bool venomous) : Animal(name, weight, num_leg){
	this->isVenomous = venomous;
}

string Spider::getSound(){
	return "HIZZ HIZZ HIZZ";
}

string Spider::getDescription(){
	string a = "The Spider's name is " + Animal::getName() + "\n";
	string b = "It weights " + to_string(Animal::getWeight()) + " lb" + "\n";
	string c = "It has " + to_string(Animal::getNum_leg()) + " leg" + "\n";
	string d = "";
	if (isVenomous == true){
		string d = "It is poison. \n";
	}
	else {
		string d = "It is not poison. \n";
	}
	string e = "Its sound is " + getSound() + "\n";
	string total = a + b + c + d + e;
	return (total);
}

int main(){
	Animal *d1 = new Dog("Pupu", 5, 4, 4);
	cout << d1 -> getDescription() << endl;

	Animal *f1 = new Fish("fish beauty", 12, 0, 2);
	cout << f1->getDescription() << endl;

	Animal *c1 = new Chicken("Opla", 24, 2, 1);
	cout << c1->getDescription() << endl;

	Animal *s1 = new Spider("Spider Man", 10, 8, true);
	cout << s1->getDescription() << endl;

	return 0;
}

*/