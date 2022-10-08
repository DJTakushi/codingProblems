#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
using namespace std;

/*
Problem Description
===================
Given one directional airport routes, devise a solution that can provide the path from Airport A to Airport B.

Example: path from Airport A -> D
Expected Input:
A -> B
B -> C
C -> D
B -> D
C -> A

Expected Output:
A,B,C,D
A,B,D

1- add_route(start, destination)
 - adds a ONE WAY connecting flight from start to destination

2- print_all_routes(start, destination)
 - prints all possible routes from start to destination
*/
class airportManager{
private:
    map<string, vector<string>> airports;//   // JFK [ohare, lax, ki]
public:
    void add_route(string start, string destination){
        if(this->airports.find(start)==airports.end()){
            vector<string> c;
            // add something to map
            // map<string, vector<string>)
            // vector<string> some_vector;
            // a_map.insert( std::pair<"abc", some_vector> )
            this->airports[start]=c;
        }
        this->airports[start].push_back(destination);
    }
    void print_all_routes(string start, string destination){
        vector<vector<string>> solutions; // jfk ohare lax
        list<vector<string>> queue;  // nodes to look at
        list<vector<string>> queueNew;
        // set<string> alreadyQueried;//
        vector<string> startVector;
        startVector.push_back(start);
        queue.push_back(startVector);
        while(queue.size()>0){
            //iterate through queue
            for(auto it = queue.begin();it!=queue.end();it++)
            {
                //check if this path meets our destination
                if(it->back()==destination)
                    solutions.push_back(*it);
                else{// add other paths to our queue IF the airport hasn't already been queried
                    string currentAirport = it->back();
                    vector<string> currentAirportDestinations= airports[currentAirport];
                    for(auto jt = currentAirportDestinations.begin();jt!=currentAirportDestinations.end();jt++)
                    {
                        vector<string> currentPath = *it;
                        //add appended vector to queue if jt's destination hasn't occurred in the path yet
                        if(find(currentPath.begin(), currentPath.end(), *jt)== currentPath.end()){
                            // cout <<"adding "<<*jt<< "to vector"<<endl;
                            currentPath.push_back(*jt);
                            queueNew.push_back(currentPath);
                        }
                    }

                }

            }
            queue.clear();
            queue=queueNew;
            queueNew.clear();
        }

        for(auto it = solutions.begin();it!=solutions.end();it++){
            for(auto jt = it->begin(); jt!=it->end();jt++){
                string space = jt+1==it->end()?"":" ";
                cout << *jt << space;
            }
            cout << endl;
        }
    }


};


int main() {
    airportManager am;
    am.add_route("A","B");
    am.add_route("B","C");
    am.add_route("C","D");
    am.add_route("B","D");
    am.add_route("C","A");

    am.print_all_routes("A","D");
//     Example: path from Airport A -> D
// Expected Output:
// A,B,C,D
// A,B,D
    return 0;
}
