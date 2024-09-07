// This is max heap implemtation with array
#include <iostream>

class MaxHeap {
public:
    MaxHeap(int capacity);
    ~MaxHeap();
    void buildHeap(int [] array);
    void heapify(int index);

    void parent(int index);
    void left(int index);
    void right(int index);
        
    void insert(int key);
    void remove(int key);

    void max();
private:
    int [] *m_heap_array;
    int m_size = 0;
    int capacity = 10; 
}
int main() {
            
    return 0;
}
