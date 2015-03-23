#include <iostream> // include standard library
#include <string> // include string library
#include <vector>
using namespace std;

template <class T>
void printVector(vector<T>){
	for (int i = 0; i < v.size(); i++){
		cout << "v[" << i << "] = " << v[i] << endl;
	}
}

int main(){
	vector <int> v; // Vector containing int elements 
	for (int i = 0; i < 5; i++){
		v.push_back(i);
	}


	printVector(v);

	// front() - return 1st elements
	// back() - return last elements
	// pop_back() - delets the last element

	return 0;
}

