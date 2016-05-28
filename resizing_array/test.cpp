#include "resizing_array.h"

int main(){
  resizing_array<int> myArray;
  int size = 10;
  for (int i = 0; i < size; i++){
    myArray.push(i);
  }
  myArray.print();
}
