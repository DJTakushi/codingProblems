#include "solution.h"
#include <algorithm>
//create class with restore/shorten functions
//class creates a vector
//  value is url
//  index in an ascii/letter representation becomes short URl
/*urlManager::urlManager()
{}*/

std::string urlManager::shorten(std::string in)
{
    std::string output = "";
    //check if already exists
    std::vector<std::string>::iterator it;
    it = std::find(urls.begin(),urls.end(),in);
    if(it != urls.end())
        output = *it;

    //generate new
    if(output == "")
    {
      urls.push_back(in);
      int len = urls.size();
      output = std::to_string(len);
    }
    return output;
}
std::string urlManager::restore(std::string in){
    std::string output = "";
    int index = std::stoi(in);
    if(index < urls.size())
      output = urls[index];
    return output;
}
