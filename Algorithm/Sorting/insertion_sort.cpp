#include <iostream>

void insertionSort(int *array, int sizeOfArray) {
    if (sizeOfArray <= 1) {
        return;
    }

    for (int i = 1; i < sizeOfArray; ++i) {
        int key = array[i];
        int j = i;
        while (j > 0 && array[j-1] > key) {
            array[j] = array[j-1];
            --j; 
        }
        array[j] = key;
    }

}
void showArray(int *array, int sizeOfArray) {
    for (int i = 0; i < sizeOfArray; ++i) {
        std::cout << array[i];

        // For print the , except the last
        if (i != sizeOfArray - 1) {
            std::cout << ",";
        }
    }
}

int main()
{
    int array[] = {100, 200, 8, 91, -1, 10, 8};
    int sizeOfArray = sizeof(array) / sizeof(int);
    insertionSort(array, sizeOfArray);
    showArray(array, sizeOfArray);
}