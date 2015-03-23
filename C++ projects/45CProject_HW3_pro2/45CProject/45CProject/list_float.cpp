#include <iostream>
#include <string>

using namespace std;

#include "list.h"

void list_float(){
	// General Test Case where we implement basic functions of the List class and make sure they work as expected
	// In this case, the list stores FLOAT type
	try {
		List<float>* number_list = new List<float>(); // initializes to (0,0)
		cout << "current size of the list is " << number_list->index_current() + 1 << endl;
		for (float i : {1.0, 2.2, 3.5, 4.2, 5.3}){
			number_list->insert(i);
		}

		cout << "the list is [1.0, 2.2, 3.5, 4.2, 5.3]" << endl;

		cout << "current size of the list after insert is now " << number_list->index_current() + 1 << endl;
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
		List<float>* float_list = new List<float>();
		for (float i : {1.1, 2.2, 3.3, 4.2, 5.1}){
			float_list->insert(i);
		}
		cout << "item at 2nd index is " << float_list->at(2) << endl;
		cout << "item at 6th index is " << float_list->at(6) << endl;
	}
	catch (InvalidIndexException e){
		cout << "the index of the list is not a valid index" << endl;
	}

	cout << endl;
	cout << "2. Test access element of empty list case" << endl;
	cout << endl;
	// Test access element of empty list case
	try {
		List<float>* float_list_1 = new List<float>();
		cout << "first item of the list" << float_list_1->first() << endl;
	}
	catch (EmptyListException e){
		cout << "The list is empty. Can't access any element in the list" << endl;
	}

	cout << endl;
	cout << "3. Test inserting element when the list is full" << endl;
	cout << endl;
	// Test inserting element when the list is full
	try{
		List<float>* float_list_2 = new List<float>();
		for (float i : {1.0, 2.2, 3.1, 4.0, 5.2, 6.1, 7.2, 8.2, 8.1, 9.5}){
			float_list_2->insert(i);
		}

		cout << "the list is [ 1.0, 2.2, 3.1, 4.0, 5.2, 6.1, 7.2, 8.2, 8.1, 9.5 ]" << endl;
		cout << "adding float 11.1 to the list " << endl;
		float a[1] = { 11.1 };
		float_list_2->insert(a[0]);
	}
	catch (FullListException e){
		cout << "The list is full. Can't insert anymore element" << endl;
	}

}