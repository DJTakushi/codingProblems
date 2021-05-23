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
        output = std::to_string(it-urls.begin());

    //generate new
    if(output == "")
    {
      urls.push_back(in);
      int len = urls.size();
      output = std::to_string(len-1);
    }
    /*for(std::vector<std::string>::iterator it = urls.begin(); it != urls.end(); ++it)
    {
      int index = it - urls.begin();
      std::cout<<" Index = " <<index << "  url = " <<*it<<"\n";
    }
    std::cout<<"urlManager::shorten output = "<<output<<"\n";*/
    return output;
}
std::string urlManager::restore(std::string in){
    std::string output = "";
    int index = std::stoi(in);
    if(index < urls.size())
      output = urls[index];
    //std::cout <<"urlManager::restore output = "<<output<<"\n";
    return output;
}

extern "C"
{
  void* createUrlManager(void){
    return new(std::nothrow) urlManager;
  }
  void deleteUrlManager(void* ptr){
    delete /*(std::nothrow)*/ (urlManager*)ptr;
  }
  char* shorten(void* manager, char* input){
    try
    {
      urlManager* ref = reinterpret_cast<urlManager*>(manager);
      std::string output = ref->shorten(std::string(input));
      return createNewCharPtr(output);
    }
    catch(...)
    {return NULL;}
  }
  char* restore(void* manager, char* query){
    try
    {
      urlManager* ref = reinterpret_cast<urlManager*>(manager);
      std::string output = ref->restore(std::string(query));
      return createNewCharPtr(output);
    }
    catch(...)
    {return NULL;}
  }
}
char * createNewCharPtr(std::string str)
{
  char *cstr = new char[str.length() + 1];//todo - clean up this memory leak
  strcpy(cstr, str.c_str());
  //printf("returning address: %p\n", cstr);
  return cstr;
}
void freeCharPtr(char *ptr)
{
    //printf("freeing address: %p\n", ptr);
    free(ptr);
}
