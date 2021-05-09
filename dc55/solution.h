#include "main.h"
#include <string.h>
#include <vector>
std::string shorten(std::string in);
std::string restore(std::string in);
class urlManager{
public:
  std::vector<std::string> urls;
  std::string shorten(std::string in);
  std::string restore(std::string in);
};
