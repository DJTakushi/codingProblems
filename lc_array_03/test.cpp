#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <benchmark/benchmark.h>
#include "shifter.h"

int main(int argc, char* argv[]){
  ::benchmark::RunSpecifiedBenchmarks();

  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

class demoTest : public ::testing::Test, public Solution{};
TEST_F(demoTest,example_1){
  std::vector<int> vec = {1,2,3,4,5,6,7};
  rotate(vec,3);
  EXPECT_THAT(vec,testing::ElementsAre(5,6,7,1,2,3,4));
}
TEST_F(demoTest,example_2){
  std::vector<int> vec = {-1,-100,3,99};
  rotate(vec,2);
  EXPECT_THAT(vec,testing::ElementsAre(3,99,-1,-100));
}

static void case1(benchmark::State& state) {
  Solution s;
  for (auto _ : state){
    std::vector<int> vec = {1,2,3,4,5,6,7};
    s.rotate(vec,3);
  }
}
BENCHMARK(case1);


static void case2(benchmark::State& state) {
  Solution s;
  for (auto _ : state){
    std::vector<int> vec = {-1,-100,3,99};
    s.rotate(vec,2);
  }
}
BENCHMARK(case2);
