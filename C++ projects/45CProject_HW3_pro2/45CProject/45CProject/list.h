#ifndef LIST_H
#define LIST_H

#include <iostream>
#include <string>
#include "Animal.h"

using namespace std;

class InvalidIndexException{}; // invalid index exception class
class EmptyListException{}; // empty list exception class
class FullListException{}; // list is full exception class


template  <class T>
class List{
public:
	List();											// default constructor
	List(int size, int max_size);
	~List();										// destructor 
	T at(int i);									// return element at index i
	bool empty() { return index < 0; }				// return true if list empty
	bool is_full(){ return index >= max_size - 1; }			// return true if size equals or greater than max_Size
	T first();										// return element at index 0, throw exception if list empty
	T last();										// return element at index -1, throw exception if list empty
	T &insert(T &item);						// insert item at the end of list, throw exception if list full
	T remove(int i);							// remove element at end of list. shift all elements inserted down by 1. Throw exception if no elemnet at index i. 
	int index_current() { return index; }
	int size_current() { return size; }


private:
	int size;
	T* stack_item;
	int max_size;
	int index;
};

template<class T>
List<T>::List(){ // default constructor 
	max_size = 10;
	index = -1;
	size = index + 1;
	stack_item = new T[max_size];
}

template<class T>
List<T>::List(int size_length, int max_size){ // overload constructor
	this->size = size_length;
	this->max = max_size;
	this->stack_item = new T[max_size];
}

template<typename T>
List<T>:: ~List(){
	delete []stack_item;
}

template <typename T>
T List<T>::at(int i){ // return the element at that indicated i index
	if (i < 0 || i > index)
		throw InvalidIndexException();
	return stack_item[i];
}


template <typename T>
T & List<T>::insert(T & item) { // insert an element to the top of the array
	if (is_full())
		throw FullListException();
	return stack_item[++index] = item;
}

template <typename T>
T List<T>::remove(int i){ // remove an item at that index from array by shifting all elements from i to end by -1 index
	if (i < 0 && i > index)
		throw InvalidIndexException();
	T * stack_item_1 = new T[index];
	for (int x = 0; x < i; x++){
		stack_item_1[x] = stack_item[x];
	}
	for (int j = i; j < index; j++) {
		stack_item_1[j] = stack_item[j + 1]; 
	}
	stack_item = stack_item_1;
	index = index - 1;
	return stack_item[index];
}

template <typename T>
T List<T>::first(){ // return 1st element of the list
	if (empty())
		throw EmptyListException();
	return stack_item[0];
}

template <typename T>
T List<T>::last(){ // return last element of the list
	if (empty())
		throw EmptyListException();
	return stack_item[index];
}

#endif