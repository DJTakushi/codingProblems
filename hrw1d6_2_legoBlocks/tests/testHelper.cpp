#include <testHelper.h>


vector<string> commandToStrings(string command){
    vector<string> o;
    std::array<char, 128> buffer;
    // std::string result;
    FILE *pipe;
    pipe = popen(command.c_str(), "r");
    if (!pipe)
    {
      std::cerr << "Couldn't start command." << std::endl;
    }
    else
    {
       while (fgets(buffer.data(), 128, pipe) != NULL) {
         // std::cout << "Reading..." << std::endl;
         o.push_back(buffer.data());
         // result += buffer.data();
        }
        auto returnCode = pclose(pipe);//not necessary, but could be helpful
    }
    return o;
}
