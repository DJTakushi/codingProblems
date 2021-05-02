#ifndef __MAIN_H__
#define __MAIN_H__
#include <string>
class node
{
public:
  node(std::string v){
    val = v;
    l = NULL;
    r = NULL;
  }
  node* l;
  node* r;
  std::string val;
};
#endif
