#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "remove_duplicates_from_sorted_array.h"

int main(int argc, char* argv[]){
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

class demoTest : public ::testing::Test, public Solution{};
TEST_F(demoTest,example_1){
  EXPECT_EQ(1,1);
  std::vector<int> vec = {1,1,2};
  EXPECT_EQ(2, removeDuplicates(vec));
  EXPECT_THAT(vec,testing::ElementsAre(1,2));
}
TEST_F(demoTest,example_2){
  EXPECT_EQ(1,1);
  std::vector<int> vec = {0,0,1,1,1,2,2,3,3,4};
  EXPECT_EQ(5, removeDuplicates(vec));
  EXPECT_THAT(vec,testing::ElementsAre(0,1,2,3,4));
}