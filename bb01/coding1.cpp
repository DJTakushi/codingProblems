/*

1.Trenton
2.Princeton
3.New Brunswick
4.Edison
5.Metropark
6.Newark
7.Secaucus
8.NY Penn Station

1.Trenton
2.Princeton
5.Metropark
6.Newark
3.New Brunswick
4.Edison
7.Secaucus
8.NY Penn Station

Write a class called "Sequencer" which prints all received data to standard output in order, according to the data's sequence number.
You can assume a method "handle" gets called providing the data (std::string) and its sequence number (int).

*/
#include <string>
#include <iostream>
#include <map>
using namespace std;
void printStation(string name){
    cout<< name<<endl;

}

void acceptStations(int id, string name){
    static int lastStationId =0;
    static map<int,string> stationQueue;
    if(id-1==lastStationId){
      printStation(name);
      lastStationId=id;


    //   list<map<int,string>::iterator> delQueue;
      for(auto it = stationQueue.begin(); it!=stationQueue.end();it++)
      {
          if(it->first -1==lastStationId)
          {
            printStation(it->second);
            lastStationId=it->first;
            // stationQueue.erase(it);
          }
      }
    }
    else{
        stationQueue[id]=name;
    }


}

int main(void)
{
    acceptStations(1,"Trenton");
    acceptStations(2,"Princeton");
    acceptStations(5,"Metropark");
    acceptStations(6,"Newark");
    acceptStations(3,"New Brunswick");
    acceptStations(4,"Edison");
    acceptStations(7,"Secaucus");
    acceptStations(8,"NY Penn Station");
}
