# Adv.-Data-Structure-project

For this project, I hope to create a visual representation of the Fibonacci Heap data structure. The final design will be set on fixed data set size and is not designed for dynamic creation of heaps becasue this will require keeping track of many pointers and the current library used was not designed for that.

As the visualization currently stands it is able to implement the **insert(), find_min() and extract_min()** operations. However the extract_min operation is not fully implemented to consolidate the nodes of similar degrees together. Graphically, there was difficulty accounting for the nodes separately after creation as this was intended as an automated process.

To initialize the heap instance simply make a call to the Heap class such as **fib = Heap()**

For the insert operation into our heap object Fib this is performed by a simple call such as **fib.insert(key)**, where key is any integer on the number line. Currently we can insert any n number of nodes into the display screen, but since the screen is currently a fixed size, the node eventually go out of the display

The find minimum and extract minimum operations are called by **fib.find_min()** & **fib.extract_min()**. Following an extract minimum operation, the find_min() operation should be called next to update the visual aid of the heap to show the new position of the min root node.
