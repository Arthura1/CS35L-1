
STEPS:
After examining the main function and observing the nested for loops, I put 
the contents of main function into a separate function called multiThreadFunction.

Then I included <pthread.h> in the header and wrote statements for creating threads
and joining threads. Since ray-tracing is an Embarrassingly Parallel problem, there is no 
communication between threads and workload can be divided equally.

I then made some variables global because the function would need to access it.


ISSUES I RAN INTO:
My initial approach of distributing the work to different threads was to divide the
image into nthread squares of equal sizes and then call the function on all these
divisions. However, this would require a lot of modifications of the original code, so
I thought of another approach.

Another challenging task was figuring out what to pass to pthread_create and to typecast
in multiThreadFunction.

APPROACH:
I passed in different 'x' values (to initialize px) to multiThreadFunction and 
incremented 'px' by nthreads.This method distributes the ray-tracing work equally by 
dividing the image's 1pixel wide cross sections equally among the threads.

CONCLUSIONS:

The multithreaded implementation of SRT improves performance significanly. 
This can be clearly seen by the times of execution:

1 thread: real	0m58.630s
2 threads:real	0m32.577s
4 threads:real	0m21.757s
8 threads:real	0m12.188s

Thus multithreading with 8 parallel threads is almost 5 times faster than doing
the same task with 1 thread.
