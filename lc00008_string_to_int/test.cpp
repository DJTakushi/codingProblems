// g++ -Wall -g -O2 -pthread reverse_integer.cpp test.cpp /usr/local/lib/libgtest.a -o tests
#include "my_atoi.h"
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
  int result = s->myAtoi("42");
  EXPECT_EQ(42, result);
}

TEST_F(minTest, example2)
{
  int result = s->myAtoi(" -042");
  EXPECT_EQ(-42, result);
}

TEST_F(minTest, example_3)
{
  int result = s->myAtoi("1337c0d3");
  EXPECT_EQ(1337, result);
}

TEST_F(minTest, example_4)
{
  int result = s->myAtoi("0-1");
  EXPECT_EQ(0, result);
}

TEST_F(minTest, example_5)
{
  int result = s->myAtoi("words and 987");
  EXPECT_EQ(0, result);
}

TEST_F(minTest, example_6)
{
  int result = s->myAtoi("-91283472332");
  EXPECT_EQ(-2147483648, result);
}

TEST_F(minTest, example_7)
{
  int result = s->myAtoi("");
  EXPECT_EQ(0, result);
}

TEST_F(minTest, example_8)
{
  int result = s->myAtoi("+1");
  EXPECT_EQ(1, result);
}
int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  int ret = RUN_ALL_TESTS();
  return ret;
}