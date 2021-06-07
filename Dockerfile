# create with *docker build . -t <desiredRepoName>
FROM ubuntu

RUN apt update -y
RUN apt upgrade -y
RUN apt install gcc -y
RUN apt install cmake -y
RUN apt install build-essential -y
RUN apt install git -y
RUN apt install python -y
RUN apt install python3 -y

#adds git repos, but these should probably be in the host filesystem to
#allow for easier editing of content.  Vim is cool, but not always easy to navigate.

RUN git clone https://github.com/DJTakushi/codingProblems.git
