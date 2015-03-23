#include <iostream>
#include <string>

using namespace std;

#include "list.h"

void list_string(){
	// General Test Case where we implement basic functions of the List class and make sure they work as expected
	// In this case, the list stores str type
	try {
		List<string>* string_list = new List<string>();
		cout << "current size of the list is " << string_list->index_current() + 1 << endl;
		string x = "hello";
		string y = "my";
		string z = "name";
		string_list->insert(x);
		string_list->insert(y);
		string_list->insert(z);


		cout << "the list is [hello, my, name]" << endl;

		cout << "current size of the list after insert is now " << string_list->index_current() + 1 << endl;
		cout << "item at indicated index is " << string_list->at(2) << endl;
		cout << "first item is " << string_list->first() << endl;
		cout << "last item is " << string_list->last() << endl;

		cout << endl;
		cout << "item has been removed is " << string_list->remove(2) << " at the index " << string_list->index_current() << endl;
		cout << "current size of the list after remove is " << string_list->index_current() + 1 << endl;
		cout << "last item is " << string_list->last() << endl;
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


	// Test invalid Index case
	cout << endl;
	cout << "1. Test invalid index case" << endl;
	cout << endl;
	try{
		List<string>* string_list_test = new List<string>();
		string a[3] = { "hello", "my", "name" };
			string_list_test->insert(a[2]);

			cout << "item at 2nd index is " << string_list_test->at(2) << endl;
			cout << "item at 6th index is " << string_list_test->at(6) << endl;
	}
	catch (InvalidIndexException e){
		cout << "the index of the list is not a valid index" << endl;
	}

	cout << endl;
	cout << "2. Test access element of empty list case" << endl;
	cout << endl;
	// Test access element of empty list case
	try {
		List<string>* string_list_1 = new List<string>();
		cout << "first item of the list" << string_list_1->first() << endl;
	}
	catch (EmptyListException e){
		cout << "The list is empty. Can't access any element in the list" << endl;
	}

	cout << endl;
	cout << "3. Test inserting element when the list is full" << endl;
	cout << endl;
	// Test inserting element when the list is full
	try{
		List<string>* string_list_2 = new List<string>();
		string a[10] = { "hello", "my", "name","one","two","three","four","five","six","ten" }; 
		string_list_2->insert(a[0]);
		string_list_2->insert(a[1]);
		string_list_2->insert(a[2]);
		string_list_2->insert(a[3]);
		string_list_2->insert(a[4]);
		string_list_2->insert(a[5]);
		string_list_2->insert(a[6]);
		string_list_2->insert(a[7]);
		string_list_2->insert(a[8]);
		string_list_2->insert(a[9]);

		cout << "the list is [ hello, my, name, one, two, three, four, five, six, ten ]" << endl;
		cout << "adding string OLAA to the list " << endl;
		string a_1 = "OLAA" ;
		string_list_2->insert(a_1);
	}
	catch (FullListException e){
		cout << "The list is full. Can't insert anymore element" << endl;
	}

}