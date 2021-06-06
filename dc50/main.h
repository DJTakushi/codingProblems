#ifndef __MAIN_H__
#define __MAIN_H__
#include <string>
#include <iostream>
class node
{
public:
  node(std::string v){
    val = v;
    l = NULL;
    r = NULL;
    // std::cout <<"new node at address" << this<<std::endl;
  }
  node(char * v){
    val = std::string(v);
    l = NULL;
    r = NULL;
    //std::cout <<"new node at address " << this<< " val = "<< this->val << std::endl;
  }
  void setL(node* n)
  {
    this->l = n;
  }
  void setR(node* n)
  {
    this->r = n;
  }
  node* getL(void)
  {
    return this->l;
  }
  node* getR(void)
  {
    return this->r;
  }
  const char* getVal()
  {
    return val.c_str();
  }
  node* l;
  node* r;
  std::string val;
};

extern "C"
{
    node* node_new(char* v){return new node(v);}
    void node_setL(node* n, node* t){n->setL(t);}
    void node_setR(node* n, node* t){n->setR(t);}
    node* node_getL(node* n){return n->getL();}
    node* node_getR(node* n){return n->getR();}
    const char* node_getVal(void* n){node* myNode = reinterpret_cast<node*>(n);return myNode->getVal();}
}
#endif
