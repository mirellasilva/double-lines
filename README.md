# Double Lines Challenge

Algorithm that draws two lines side by side without overlapping. It must handle an arbitrary amount of points where each 3 consecutive points are forming a 90 degrees angle.

This code was developed in the context of a challenge. Read more about it [here](https://github.com/vjeux/weekly-challenge-2-double-lines).


## Requirements

* Python 
* matplotlib

## How to Run

### Auto

Run: 

```
python3 run_tests.py
```

### Manually
You can both use sys.argv to enter with the points, separated by space, such as `x1 y1 x2 y2 ... xn yn`, or follow instructions for io input.


**Sample run:**

starts vertical down, ends vertical up
```
python3 dlines.py 5 13 5 9 8 9 8 6 2 6 2 9
```
starts vertical down, ends horizontal left
```
python3 dlines.py 2 9 2 6 8 6 8 9 5 9 5 13 2 13
```
starts vertical up, ends vertical down
```
python3 dlines.py 10 10 10 13 7 13 7 10 4 10 4 7 7 7 7 4 13 4 13 1 16 1 16 12 13 12 13 9 11 9 11 2
```
starts horizontal left, ends horizontal left
```
python3 dlines.py 10 13 7 13 7 10 4 10 4 7 7 7 7 4 13 4 13 1 16 1 16 12 13 12 13 9 11 9 11 2 10 2
```
starts horizontal right, ends horizontal right
```
python3 dlines.py 9 11 10 11 10 13 7 13 7 10 4 10 4 7 7 7 7 4 13 4 13 1 16 1 16 12 13 12 13 9 11 9 11 6 18 6
```

