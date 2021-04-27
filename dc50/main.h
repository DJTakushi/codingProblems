#include <string>
class node
{
public:
  node(std::string v){
    val = v;
    l = 0;
    r = 0;
  }
  node* l;
  node* r;
  std::string val;
};
