#include <solution.h>

vector<string> Solution::getDescription(){
  vector<string> o;
  string title = string(PROJECT_NAME);
  title+=" "+to_string(VERSION_MAJOR)
        +"."+to_string(VERSION_MINOR);
  string desc = "  ";
  desc += PROJECT_DESCRIPTION;
  string url = "  ";
  url+=PROJECT_HOMEPAGE_URL;
    o.push_back(title);
    o.push_back(desc);
    o.push_back(url);
  return o;
}

// TODO - define functions here!!!
