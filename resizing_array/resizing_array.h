#include <iostream>

template<typename T>
class resizing_array {

  public:
    resizing_array();
    resizing_array(int initSize);
    resizing_array(resizing_array &original);
    ~resizing_array();
    void push(T item);
    void pop(T item);
    T get(int index);
    T &operator[](int index);
    int getSize();
    void print();
    
  private:
    void resize(int newSize);
    int size;
    T *array;
    int filled_elements;
};


template<typename T>
resizing_array<T>::resizing_array(): resizing_array(2) {}

template<typename T>
resizing_array<T>::resizing_array(int initSize) {
  size = initSize;
  array = new T[size];
  filled_elements = 0;
}

template<typename T>
void resizing_array<T>::push(T item) {
 if (filled_elements == size){
   int newSize = size * 2;
   resize(newSize);
 }

 *(array + filled_elements) = item;
 filled_elements++;
}

template<typename T>
void resizing_array<T>::resize(int newSize){
  T *temp = nullptr;
  temp = new T[newSize];

  for (int i = 0; i< size; i++){
    temp[i] = array[i];
  }

  size = newSize;
  array = temp;
}

template<typename T>
resizing_array<T>::~resizing_array() {
  delete array;
}

template<typename T>
int resizing_array<T>::getSize(){
  return size;
}

template<typename T>
void resizing_array<T>::print(){
  for (int i=0; i < size; i++){
    std::cout << *(array + i) << ' ';
  }

  std::cout << std::endl;
}
  

