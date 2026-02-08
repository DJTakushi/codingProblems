#include "integer_container_impl.hpp"
#include <iostream>
// TODO: implement interface methods here
int IntegerContainerImpl::Add(int value) {
  _l.push_back(value);
  return _l.size();
}

bool IntegerContainerImpl::Delete(int value) {
  auto it = _l.begin();
  for (auto it = _l.begin(); it != _l.end(); ++it) {
    if (value == *it) {
      _l.erase(it);
      return true;
    }
  }
  return false;
}

std::optional<int> IntegerContainerImpl::GetMedian() {
  if (_l.size() == 0) {
    std::cout << "list size = 0" << std::endl;
    return std::nullopt;
  }

  std::list<int> l2 = _l;
  _l.sort();
  for (auto it = _l.begin(); it != _l.end(); ++it) {
    std::cout << *it << ",";
  }
  std::cout << std::endl;

  size_t lsize = _l.size();
  int counter = 0;
  std::list<int>::iterator it = _l.begin();

  std::cout << "l2size/2 = " << lsize / 2 << std::endl;
  while (int(counter) < int((lsize / 2))) {
    counter = counter + 1;
    it++;
    std::cout << "counter incrementing" << std::endl;
  }
  std::cout << "counter " << counter << std::endl;
  if (lsize % 2 == 0) { // even; average idx + prev-idx
    double p1 = double(*it);
    it--;
    double p2 = double(*(it));
    std::cout << "p1 : " << p1 << ", p2 : " << p2 << std::endl;
    double median = p2;//(p1 + p2) / 2.0;
    std::cout << "even median : " << median << std::endl;
    return median;
  } else {
    return *it;
  }
}
