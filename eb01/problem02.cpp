/**
You have information about n different recipes. You are given a string array
recipes and a 2D string array ingredients. The ith recipe has the name
recipes[i], and you can create it if you have all the needed ingredients from
ingredients[i]. Ingredients to a recipe may need to be created from other
recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that
you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create.
You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

Example 1:
Input:
recipes = ["bread"],
ingredients = [["yeast", "flour"]],
supplies = ["yeast", "flour", "corn"]

Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
Input:
recipes = ["bread","sandwich"],
ingredients = [["yeast","flour"],["bread","meat"]],
supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can
create the ingredient "bread".

Example 3:
Input:
recipes = ["bread","sandwich","burger"],
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]],
supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create
the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create
the ingredients "bread" and "sandwich".

Constraints:
n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English
letters. All the values of recipes and supplies combined are unique. Each
ingredients[i] does not contain any duplicate values.
*/

#include <cstddef>
#define CATCH_CONFIG_MAIN
#include "catch.hpp"

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

std::vector<std::string>
findAllReciepes(const std::vector<std::string> &recipes,
                const std::vector<std::vector<std::string>> &ingredients,
                const std::vector<std::string> &supplies) {
  /*** CODE HERE ***/
  std::vector<std::string> output; // output
  std::unordered_set<std::string> availableSupplies;
  for (auto it = supplies.begin(); it != supplies.end(); it++)
    availableSupplies.insert(*it);

  bool addedSomething = true;
  while (addedSomething) {

    addedSomething = false;

    for (std::size_t i = 0; i < recipes.size(); i++) {

      const auto thisRecipe = recipes[i];

      if (std::find(output.begin(), output.end(), thisRecipe) == output.end()) {
        // o does not already include this recipe
        bool allIngredientsExist = true;
        for (auto thisIngredient = ingredients[i].begin();
             thisIngredient != ingredients[i].end(); thisIngredient++) {
          if (availableSupplies.find(*thisIngredient) ==
              availableSupplies.end()) {

            //std::cout << "recipe " << thisRecipe
            //          << " missing ingredient: " << *thisIngredient
            //          << std::endl;
            allIngredientsExist = false;
            break;
          }
        }
        if (allIngredientsExist) {
          //std::cout << "all ingredients exist for " << thisRecipe << std::endl;
          availableSupplies.insert(thisRecipe);
          output.push_back(thisRecipe);
          addedSomething = true;
        }
      }
    }
  }
  return output;
}
/*
int main() {
  const auto &recipes = findAllReciepes({"bread"}, {{"yeast", "flour"}},
                                        {"yeast", "flour", "corn"});
  std::cout << "Printing Output recipes ==== ";
  for (const auto &recipe : recipes) {
    std::cout << std::endl << recipe;
  }
}*/

void assert_result(const std::string &test_case,
                   std::vector<std::string> expected,
                   std::vector<std::string> result) {
  std::cout << "\nChecking Test case " << test_case << "\n";
  sort(expected.begin(), expected.end());
  sort(result.begin(), result.end());
  REQUIRE(expected == result);
}

TEST_CASE("compare vector outputs", "[assertions]") {

  assert_result("1", {"bread"},
                findAllReciepes({"bread"}, {{"yeast", "flour"}},
                                {"yeast", "flour", "corn"}));

  assert_result("2", {"bread", "sandwich"},
                findAllReciepes({"bread", "sandwich"},
                                {{"yeast", "flour"}, {"bread", "meat"}},
                                {"yeast", "flour", "meat"}));

  assert_result("3", {"bread", "sandwich", "burger"},
                findAllReciepes({"bread", "sandwich", "burger"},
                                {{"yeast", "flour"},
                                 {"bread", "meat"},
                                 {"sandwich", "meat", "bread"}},
                                {"yeast", "flour", "meat"}));

  assert_result("4", {},
                findAllReciepes({"bread"}, {{"yeast", "flour"}}, {"yeast"}));

  assert_result("5", {"bread"},
                findAllReciepes({"bread"}, {{"yeast", "flour"}},
                                {"yeast", "flour", "corn"}));

  assert_result(
      "6", {"ju", "fzjnm", "q"},
      findAllReciepes({"ju", "fzjnm", "x", "e", "zpmcz", "h", "q"},
                      {{"d"},
                       {"hveml", "f", "cpivl"},
                       {"cpivl", "zpmcz", "h", "e", "fzjnm", "ju"},
                       {"cpivl", "hveml", "zpmcz", "ju", "h"},
                       {"h", "fzjnm", "e", "q", "x"},
                       {"d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"},
                       {"f", "hveml", "cpivl"}},
                      {"f", "hveml", "cpivl", "d"}));

  assert_result("7", {"nkov"},
                findAllReciepes({"qxyj", "vawos", "nkov", "bec", "qiabz"},
                                {{"mxf"},
                                 {"iy", "qxyj", "nkov", "qiabz", "bec"},
                                 {"nw", "xutnl", "e"},
                                 {"eep", "km", "nw", "xutnl", "e", "iy",
                                  "vawos", "qxyj", "qiabz"},
                                 {"nyhyc"}},
                                {"nw", "eep", "iy", "e", "xutnl", "km"}));
  assert_result(
      "8",
      {"xevvq", "izcad", "bxgnm", "i", "hjvu", "tokfq", "z", "g", "b", "hthy"},
      findAllReciepes(
          {"xevvq", "izcad", "p", "we", "bxgnm", "vpio", "i", "hjvu", "igi",
           "anp", "tokfq", "z", "kwdmb", "g", "qb", "q", "b", "hthy"},
          {{"wbjr"},
           {"otr", "fzr", "g"},
           {"fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"},
           {"fzr", "xgp", "wi", "otr", "tokfq", "izcad", "igi", "xevvq", "i",
            "anp"},
           {"wi", "xgp", "wbjr"},
           {"wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"},
           {"xgp", "otr", "wbjr"},
           {"wbjr", "otr"},
           {"wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"},
           {"xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"},
           {"bxgnm"},
           {"wi", "fzr", "otr", "wbjr"},
           {"wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"},
           {"otr", "fzr", "xgp", "wbjr"},
           {"xgp", "wbjr", "q", "vpio", "tokfq", "we"},
           {"wbjr", "wi", "xgp", "we"},
           {"wbjr"},
           {"wi"}},
          {"wi", "otr", "wbjr", "fzr", "xgp"}));
}
