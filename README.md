# Adv.-Data-Structure-project

For this project, I hope to create a visual representation of the Fibonacci Heap data structure. This design will be set on fixed data set and is not designed for dynamic creation of heaps. A dynamic creation of the visual aid for the heap structure will require a more developed graphics library that can keep track of the individual nodes created.

As the visualization currently stands it is able to implement the **insert(), find_min() and extract_min()** operations. However the extract_min operation is not fully implemented to consolidate the 

To initialize the heap instance simply make a call to the Heap class such as **fib = Heap()**

For the insert operation into our heap object Fib this is performed by a simple call such as **fib.insert(key)**, where key is any integer on the number line. Currently we can insert any n number of

The find minimum and extract minimum operations are called by **fib.find_min()** & **fib.extract_min()**. Following an extract minimum operation, the find_min() operation should be called next to update the visual aid of the heap to show the new position of the min root node.
