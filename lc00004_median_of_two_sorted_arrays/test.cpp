// g++ -Wall -g -O2 -pthread medianOfTwoSortedArrays.cpp test.cpp /usr/local/lib/libgtest.a -o tests
#include "medianOfTwoSortedArrays.h"
#include <gtest/gtest.h>

// Test fixture for CAN0 uptime tests
class minTest : public ::testing::Test
{
protected:
  Solution *s;
  virtual void SetUp()
  {
    s = new Solution();
  }

  virtual void TearDown()
  {
    delete s;
  }
};

TEST_F(minTest, example1)
{
  vector<int> n1 = {1,3};
  vector<int> n2 = {2};

  double result = s->findMedianSortedArrays(n1, n2);
  EXPECT_EQ(2.0, result);
}

TEST_F(minTest, example2)
{
  vector<int> n1 = {1,2};
  vector<int> n2 = {3,4};

  double result = s->findMedianSortedArrays(n1, n2);
  EXPECT_EQ(2.5, result);
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  int ret = RUN_ALL_TESTS();
  return ret;
}