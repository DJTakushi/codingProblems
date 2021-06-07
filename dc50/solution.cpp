#include "solution.h"
// #include <iostream>
int myFunction (node* head)
{
  int output = 0;
  int l = 0;
  int r = 0;
  if (head->l)
    l = myFunction(head->l);
  if (head->r)
    r = myFunction(head->r);
  // std::cout << "l="<<l<<" r="<<r<<std::endl;
  if(head->val =="+")
    output = l + r;
  else
  {
    if(head->val =="-")
      output = l - r;
    else
    {
      if(head->val =="*")
        output = l * r;
      else
      {
        if(head->val =="/")
          output = l/r;
        else
          output = std::stoi(head->val);
      }
    }
  }
  // std::cout << "Returning " << output <<std::endl;
  return output;
}
