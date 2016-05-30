#include <iostream>
#include<cstdlib>

template<typename T>
class queue {

  public:
    queue();
    queue(int initSize);
    queue(queue &original);
    ~queue();
    void enqueue(T item);
    T dequeue();
    int getSize();
    void print();

  private:
    void resize(int newSize);
    int size;
    T *array;
    int filled_elements();
    bool isFull();
    int head;
    int tail;
    bool tail_wraps;
    int circular_increment(int);
};


template<typename T>
queue<T>::queue(): queue(1) {}

template<typename T>
queue<T>::queue(int initSize) {
  size = initSize;
  array = new T[size];
  head = 0, tail = 0;
  tail_wraps = false;
}

template<typename T>
void queue<T>::enqueue(T item) {
  if (isFull()){
    int newSize = size * 2;
    resize(newSize);
  }

  array[tail] = item;
  tail = circular_increment(tail);
  if (tail == 0){
    tail_wraps = true;
  }
}

template<typename T>
T queue<T>::dequeue(){
  // if (filled_elements == 0) {
  //   return NULL;
  // }
  T temp = array[head];
  array[head] = NULL;
  head = circular_increment(head);
  if (head == 0) {
    tail_wraps = false;
  }
  if (filled_elements() == size/4  && size > 1){
    resize(size/2);
  }
  return temp;
}

template<typename T>
void queue<T>::resize(int newSize){
  T *temp = nullptr;
  temp = new T[newSize];
  int filled = filled_elements();

  for (int i = 0; i< filled; i++){
    int wrapped_tail = circular_increment(i + head-1);
    temp[i] = array[wrapped_tail];
  }
  head = 0;
  tail = filled;
  tail_wraps = false;
  size = newSize;
  array = temp;
}

template<typename T>
queue<T>::~queue() {
  delete array;
}

template<typename T>
int queue<T>::getSize(){
  return size;
}

template<typename T>
void queue<T>::print(){
  for (int i=0; i < size; i++){
    std::cout << *(array + i) << ' ';
  }

  std::cout << std::endl;
}

template<typename T>
int queue<T>::filled_elements() {
  int true_tail = tail;
  if (tail_wraps) {
    true_tail += (size  );
  }

  return true_tail - head;
}

template<typename T>
bool queue<T>::isFull() {
  //std::cout << "filled = " << filled_elements() << " and size: " << size << " wrapped: " << tail_wraps<< std::endl;
  return (filled_elements() == size);
}


template<typename T>
int queue<T>::circular_increment(int value) {
  value++;
  if (value == size) {
    value = 0;
  }
  return value;
}

