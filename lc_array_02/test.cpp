#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "stock_trader.h"

int main(int argc, char* argv[]){
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

class demoTest : public ::testing::Test, public Solution{};
TEST_F(demoTest,example_1){
  std::vector<int> vec = {7,1,5,3,6,4};
  EXPECT_EQ(7, maxProfit(vec));
}

TEST_F(demoTest,example_2){
  std::vector<int> vec = {1,2,3,4,5};
  EXPECT_EQ(4, maxProfit(vec));
}

TEST_F(demoTest,example_3){
  std::vector<int> vec = {7,6,4,3,1};
  EXPECT_EQ(0, maxProfit(vec));
}