# codingProblems
# Notes
 - https://stackoverflow.com/questions/14246119/how-can-i-redirect-the-output-of-unittest-obvious-solution-doesnt-work
    - unittest uses a sandbox that wraps std streams, so 2> has to be used to write to a file instead of display on screen
    - https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure for common structure
