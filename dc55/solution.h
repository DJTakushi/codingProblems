#include "main.h"
#include <string.h>
#include <vector>
#include <iostream>
#include <new>
std::string shorten(std::string in);
std::string restore(std::string in);
class urlManager{
public:
  std::vector<std::string> urls;
  std::string shorten(std::string in);
  std::string restore(std::string in);
};
extern "C"
{
  void* createUrlManager(void);
  void deleteUrlManager(void* ptr);
  char* shorten(void* manager, char* input);
  char* restore(void* manager, char* query);
  void freeCharPtr(char *ptr);
}
char * createNewCharPtr(std::string str);
