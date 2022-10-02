# Problem
https://www.hackerrank.com/challenges/one-week-preparation-kit-lego-blocks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-six

You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

d	h	w
1	1	1
1	1	2
1	1	3
1	1	4
Using these blocks, you want to make a wall of height  and width . Features of the wall are:

- The wall should not have any holes in it.
- The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks.
- The bricks must be laid horizontally.

How many ways can the wall be built?

Example



The height is  and the width is . Here are some configurations:

image

These are not all of the valid permutations. There are  valid permutations in all.

Function Description

Complete the legoBlocks function in the editor below.

legoBlocks has the following parameter(s):

int n: the height of the wall
int m: the width of the wall
Returns
- int: the number of valid wall formations modulo

Input Format

The first line contains the number of test cases .

Each of the next  lines contains two space-separated integers  and .

Constraints



Sample Input

STDIN   Function
-----   --------
4       t = 4
2 2     n = 2, m = 2
3 2     n = 3, m = 2
2 3     n = 2, m = 3
4 4     n = 4, m = 4
Sample Output

3  
7  
9  
3375
Explanation

For the first case, we can have:

image


For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. Thus, the number of ways is  and .

# Notes
- Restructuring per Boris Kolpackov's Canonical Project Structure ([https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1204r0.html](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p1204r0.html))

# Configure, build, and install with CMake
### Configure
Navigate to this directory
1. Create `out` subdirectory
```
mkdir out
```
Navigate to this with `cd out`
2. Create CMAke project with parent's `CMakeLists.txt`:
```
cmake ..
```

### Build
(in `out` directory)
```
make
```

Run interface locally:
```
./lb 2 "2 2"
```
### Install
(in `out` directory)
Install with:
```
cmake --install .
```
Observe the installation details
```
root@629cd871f0e1:/cp/hrw1d6_2_legoBlocks/out# cmake --install .
-- Install configuration: ""
-- Installing: /usr/local/lb/lb
-- Set runtime path of "/usr/local/lb/lb" to "/usr/local/lb"
-- Up-to-date: /usr/local/lb/include/legoBlocksInterfaceConfig.h
-- Up-to-date: /usr/local/lb/legoFunctions/liblegoFunctionsStatic.a
-- Up-to-date: /usr/local/lb/liblegoFunctions.so
-- Up-to-date: /usr/local/lb/legoFunctions/legoFunctions.h
-- Installing: /usr/local/lb/lbTest
-- Set runtime path of "/usr/local/lb/lbTest" to "/usr/local/lb"
```

Can run `lb` from `usr/local/lb`:
```
/usr/local/lb/lb 2 "2 2"
```
# Testing
### Function Testing
Function test tools are built in the main CMake build from content in the `tests` directory.  They are generated as `out/tests/lbTest`, and are installed as `/usr/local/lb/lbTest` to test the installation.

##### Library Test
The legoFunctions library `liblegoFunctions.so` is tested by default by running `lbTest`

##### Interface Test
The interface is tested with `lbTest i`
