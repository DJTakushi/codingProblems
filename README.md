# codingProblems
Practice coding problems, solved in python and C++.  \
Unit tests are all in python, and can be individually run in each folder's test python script or by running `test.py` in the head directory (which also builds C++ solutions when necessary).

# Prefixes
  - `az` = Amazon practice problems
  - `dc` = Daily Coding problems
  - `eu` = Project Euler problems

## Dependencies
- python or python3
- cmake
- gcc (and build-essential)

# Notes
 - https://stackoverflow.com/questions/14246119/how-can-i-redirect-the-output-of-unittest-obvious-solution-doesnt-work
    - unittest uses a sandbox that wraps std streams, so 2> has to be used to write to a file instead of display on screen
    - https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure for common structure
