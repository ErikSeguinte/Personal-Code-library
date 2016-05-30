#include "resizing_array.h"

int main(){
  queue<int> myArray;
  int size = 10;
  for (int i = 0; i < size; i++){
    myArray.enqueue(i);
  }
  myArray.print();

  for (int i = 0; i < size-2; i++){
    std::cout << myArray.dequeue()<< " expected: " << i << std::endl;
  }
  myArray.print();
  myArray.enqueue(11);
  myArray.print();
  myArray.dequeue();
  myArray.dequeue();
  myArray.print();
  std::cout << myArray.dequeue() << std::endl;
  myArray.print();
}
