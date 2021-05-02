#include "solution.h"
int myFunction (node* head)
{
  int output = 0;
  int l,r = 0;
  if (head->l)
    l = myFunction(head->l);
  if (head->r)
    r = myFunction(head->r);
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
  return output;
}
