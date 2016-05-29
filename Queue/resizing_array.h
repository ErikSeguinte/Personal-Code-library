#include <iostream>
#include<cstdlib>

template<typename T>
class stack {

  public:
    stack();
    stack(int initSize);
    stack(stack &original);
    ~stack();
    void push(T item);
    T pop();
    int getSize();
    void print();

  private:
    void resize(int newSize);
    int size;
    T *array;
    int filled_elements;
};


template<typename T>
stack<T>::stack(): stack(1) {}

template<typename T>
stack<T>::stack(int initSize) {
  size = initSize;
  array = new T[size];
  filled_elements = 0;
}

template<typename T>
void stack<T>::push(T item) {
  if (filled_elements == size){
    int newSize = size * 2;
    resize(newSize);
  }

  *(array + filled_elements) = item;
  filled_elements++;
}

template<typename T>
T stack<T>::pop(){
  // if (filled_elements == 0) {
  //   return NULL;
  // }
  T temp = array[--filled_elements];
  array[filled_elements] = NULL;
  if (filled_elements == size/4  && filled_elements > 0){
    resize(size/2);
  }
  return temp;
}

template<typename T>
void stack<T>::resize(int newSize){
  T *temp = nullptr;
  temp = new T[newSize];

  for (int i = 0; i< filled_elements; i++){
    temp[i] = array[i];
  }

  size = newSize;
  array = temp;
}

template<typename T>
stack<T>::~stack() {
  delete array;
}

template<typename T>
int stack<T>::getSize(){
  return size;
}

template<typename T>
void stack<T>::print(){
  for (int i=0; i < size; i++){
    std::cout << *(array + i) << ' ';
  }

  std::cout << std::endl;
}


