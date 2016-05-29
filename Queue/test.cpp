#include "resizing_array.h"

int main(){
  stack<int> myArray;
  int size = 10;
  for (int i = 0; i < size; i++){
    myArray.push(i);
  }
  myArray.print();

  for (int i = 0; i < size-2; i++){
    std::cout << myArray.pop() << std::endl;
  }
  myArray.print();
  myArray.push(11);
  myArray.print();
  myArray.pop();
  myArray.pop();
  myArray.print();
  std::cout << myArray.pop() << std::endl;
  myArray.print();
}
