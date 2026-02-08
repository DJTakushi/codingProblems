#ifndef INTEGER_CONTAINER_IMPL_HPP_
#define INTEGER_CONTAINER_IMPL_HPP_

#include "integer_container.hpp"
#include <list>

class IntegerContainerImpl : public IntegerContainer {
  std::list<int> _l;
  virtual int Add(int value);
  virtual bool Delete(int value);
  virtual std::optional<int> GetMedian();
};

#endif // INTEGER_CONTAINER_IMPL_HPP_
