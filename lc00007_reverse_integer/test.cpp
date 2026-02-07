// g++ -Wall -g -O2 -pthread reverse_integer.cpp test.cpp /usr/local/lib/libgtest.a -o tests
#include "reverse_integer.h"
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
  int x = 123;
  int result = s->reverse(x);
  EXPECT_EQ(321, result);
}

TEST_F(minTest, example2)
{
  int x = -123;
  int result = s->reverse(x);
  EXPECT_EQ(-321, result);
}

TEST_F(minTest, example_3)
{
  int x = 120;
  int result = s->reverse(x);
  EXPECT_EQ(21, result);
}

TEST_F(minTest, example_4)
{
  int x = 1534236469;
  int result = s->reverse(x);
  EXPECT_EQ(0, result);
}


int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  int ret = RUN_ALL_TESTS();
  return ret;
}