#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -- linear (grows in direct proportion of the input size) O(1) * O(n^3) * O(n^2)


b) O(n log n) -- logarithmic O(1) * O(n) * O(1) * O(n) * O(1) * O(1) = O(n log n)


c) O(n) -- linear (grows in direct proportion of the input size)

## Exercise II


1. Start in the middle of the building (Binary search)
2. If the egg DOES break:
    - Floor F is less than the middle of the building.
    - Continue one floor down from the middle until we find floor F
3. If the egg DOESN'T break 
    - Floor F is higher than the middle of the building.
    - Continue one floor up from the middle until we find floor F

O(logN) because 1/2 time