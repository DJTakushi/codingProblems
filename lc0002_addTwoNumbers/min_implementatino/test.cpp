// g++ -Wall -g -O2 -pthread addTwoNumbers.cpp test.cpp /usr/local/lib/libgtest.a -o tests
#include "addTwoNumbers.h"
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

TEST_F(minTest, 2_4_3_and_5_6_4)
{
  ListNode *n1 = new ListNode(2, new ListNode(4, new ListNode(3)));
  ListNode *n2 = new ListNode(5, new ListNode(6, new ListNode(4)));

  ListNode *a = s->addTwoNumbers(n1, n2);
  EXPECT_EQ(7, a->val);
  EXPECT_EQ(0, a->next->val);
  EXPECT_EQ(8, a->next->next->val);
  EXPECT_EQ(nullptr, a->next->next->next);
}

TEST_F(minTest, 0_and_0)
{
  ListNode *n1 = new ListNode(0);
  ListNode *n2 = new ListNode(0);

  ListNode *a = s->addTwoNumbers(n1, n2);
  EXPECT_EQ(0, a->val);
  EXPECT_EQ(nullptr, a->next);
}

TEST_F(minTest, seven9s_and_four9s)
{
  ListNode *n1 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9)))))));
  ListNode *n2 = new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))));

  ListNode *a = s->addTwoNumbers(n1, n2);
  EXPECT_EQ(8, a->val);
  EXPECT_EQ(9, a->next->val);
  EXPECT_EQ(9, a->next->next->val);
  EXPECT_EQ(9, a->next->next->next->val);
  EXPECT_EQ(0, a->next->next->next->next->val);
  EXPECT_EQ(0, a->next->next->next->next->next->val);
  EXPECT_EQ(0, a->next->next->next->next->next->next->val);
  EXPECT_EQ(1, a->next->next->next->next->next->next->next->val);
  EXPECT_EQ(nullptr, a->next->next->next->next->next->next->next->next);
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  int ret = RUN_ALL_TESTS();
  return ret;
}