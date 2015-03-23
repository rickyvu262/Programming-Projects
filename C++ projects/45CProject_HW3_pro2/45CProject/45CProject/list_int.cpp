#include <iostream>
#include <string>

using namespace std;

#include "list.h"

void list_int(){

	// General Test Case where we implement basic functions of the List class and make sure they work as expected
	// In this case, the list stores INT type
	try {
		List<int>* number_list = new List<int>(); // initializes to (0,0)
		cout << "current size of the list is " << number_list->index_current() +1 << endl;
		for (int i : {1, 2, 3, 4, 5}) {
			number_list->insert(i);
		}
		
		cout << "the list is [1,2,3,4,5]" << endl;

		cout << "current size of the list after insert is now " << number_list->index_current()+1 << endl;
		cout << "item at indicated index is " << number_list->at(2) << endl;
		cout << "first item is " << number_list->first() << endl;
		cout << "last item is " << number_list->last() << endl;

		cout << endl;
		cout << "item has been removed is " << number_list->remove(4) << " at the index " << number_list->index_current() << endl;
		cout << "current size of the list after remove is " << number_list->index_current() + 1 << endl;
		cout << "last item is " << number_list->last() << endl;
		
	}
	catch (InvalidIndexException e){
		cout << "the index of the list is not a valid index" << endl;
	}
	catch (EmptyListException e){
		cout << "The list is empty. Can't access any element in the list" << endl;
	}
	catch (FullListException e){
		cout << "The list is full. Can't insert anymore element" << endl;
	}


	cout << endl;
	cout << "1. Test invalid Index case" << endl;
	cout << endl;
	// Test invalid Index case
	try{
		List<int>* int_list = new List<int>();
		for (int i : {1, 2, 3, 4, 5}){
			int_list->insert(i);
		}
		cout << "the list is [1,2,3,4,5]" << endl;
		cout << "item at indicated index is " << int_list->at(2) << endl;
		cout << "item at indicated index is " << int_list->at(6) << endl;
	}
	catch (InvalidIndexException e){
		cout << "the index of the list is not a valid index" << endl;
	}

	cout << endl;
	cout << "2. Test access element of empty list case" << endl;
	cout << endl;
	// Test access element of empty list case
	try {
		List<int>* int_list_1 = new List<int>();
		cout << "the list is []" << endl;
		cout << "first item of the list" << int_list_1->first() << endl;
	}
	catch (EmptyListException e){
		cout << "The list is empty. Can't access any element in the list" << endl;
	}
	
	cout << endl;
	cout << "3. Test inserting element when the list is full" << endl;
	cout << endl;
	// Test inserting element when the list is full
	try{
		List<int>* int_list_2 = new List<int>();
		for (int i : {1, 2, 3, 4, 5, 6, 7, 8, 8, 9}){
			int_list_2->insert(i);
		}
		cout << "adding int 11 to the list " << endl;
		int a[1] = { 11 };
		int_list_2->insert(a[0]);
	}
	catch (FullListException e){
		cout << "The list is full. Can't insert anymore element" << endl;
	}
	
}