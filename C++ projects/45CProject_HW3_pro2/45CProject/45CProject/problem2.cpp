#include <iostream>
#include <string>
#include "Animal.h"
#include "Dog.h"
#include "Fish.h"
#include "Chicken.h"
#include "Spider.h"

#include "list.h"

using namespace std;

void problem2(){
	Animal *d1 = new Dog("Pupu", 5, 4, 4); // A dog object
	cout << d1->getDescription() << endl;
	Animal *f1 = new Fish("fish beauty", 12, 0, 2); // A Fish object
	cout << f1->getDescription() << endl;
	Animal *c1 = new Chicken("Opla", 24, 2, 1);// A Chicken Object
	cout << c1->getDescription() << endl;
	Animal *s1 = new Spider("Spider Man", 10, 8, false);// A Spider object
	cout << s1->getDescription() << endl;

	// part b. Implementing a list from problem 1 to add certain animals. 
	List<Animal>* animal_list = new List<Animal>();
	Animal a[4] = { *d1, *f1, *c1, *s1 };
	for (int i : {0, 1, 2, 3}){
		animal_list->insert(a[i]);
	}

	//cout << animal_list->first() << endl;
	
	//cout << "this is the first animal " <<  << endl; 
	// Tranverse the list and print out all description of each animal in the list
	
}