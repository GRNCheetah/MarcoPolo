#!/bin/sh
who=` whoami 2>/dev/null`

system_info()
{
	echo  "[33m### SYSTEM INFORMATION ###"
	unameinfo=` uname -a 2>/dev/null`
	if [ "$unameinfo" ]; then
		echo  "[*] Kernel Information:\n$unameinfo"
		echo  "\n"
	fi

	procver=` cat /proc/version 2>/dev/null`
	if [ "$procver" ]; then
		echo  "[*] Kernel Information(Cont):\n$procver"
		echo  "\n"
	fi

	hostnamed=` hostname 2>/dev/null`
	if [ "$hostnamed" ]; then
		echo  "[*] Hostname:\n$hostnamed"
		echo  "\n"
	fi
}

user_info() 
{
		
	#current user
	echo  "[33m### USER/GROUP ###"
	currusr=` id 2>/dev/null`
	if [ "$currusr" ]; then
		echo  "[*] Current user/group info:\n$currusr"
		echo  "\n"
	fi


	#who else is logged on
	loggedonusrs=` w 2>/dev/null`
	if [ "$loggedonusrs" ]; then
		echo  "[-] Who else is logged on:\n$loggedonusrs" 
		echo  "\n"
	fi

	#contents of /etc/passwd
	readpasswd=` cat /etc/passwd 2>/dev/null`
	if [ "$readpasswd" ]; then
		echo  "[-] Contents of /etc/passwd:\n$readpasswd" 
		echo  "\n"
	fi

	#checks to see if roots home directory is accessible
	rthmdir=` ls -ahl /root/ 2>/dev/null`
	if [ "$rthmdir" ]; then
		echo  "[33m[+] We can read root's home directory!\n$rthmdir" 
		echo  "\n"
	fi

	#looks for files we can write to that don't belong to us
	if [ "$thorough" = "1" ]; then
		grfilesall=` find / -writable ! -user \`whoami\` -type f ! -path "/proc/*" ! -path "/sys/*" xec ls -al {} \; 2>/dev/null`
		if [ "$grfilesall" ]; then
			echo  "[-] Files not owned by user but writable by group:\n$grfilesall" 
			echo  "\n"
		fi
	fi

	#lists current user's home directory contents
	if [ "$thorough" = "1" ]; then
		homedircontents=` ls -ahl ~ 2>/dev/null`
		if [ "$homedircontents" ] ; then
			echo  "[-] Home directory contents:\n$homedircontents" 
			echo  "\n" 
		fi
	fi
}

env_info()
{
	echo  "[33m### ENVIRONMENTAL #######################################"

	#env information
	envinfo=` env 2>/dev/null | grep -v 'LS_COLORS' 2>/dev/null`
	if [ "$envinfo" ]; then
		echo  "[-] Environment information:\n$envinfo" 
		echo  "\n"
	fi

	#current path configuration
	pathinfo=` echo $PATH 2>/dev/null`
	if [ "$pathinfo" ]; then
		pathswriteable=` ls -ld $(echo $PATH | tr ":" " ")`
		echo  "[-] Path information:\n$pathinfo" 
		echo  "$pathswriteable"
		echo  "\n"
	fi

	
	#lists available shells
	shellinfo=` cat /etc/shells 2>/dev/null`
	if [ "$shellinfo" ]; then
		echo  "[-] Available shells:\n$shellinfo" 
		echo  "\n"
	fi
}

cron_info()
{
	echo  "[33m### JOBS/TASKS ##########################################" 

	#are there any cron jobs configured
	cronjobs=` ls -la /etc/cron* 2>/dev/null`
	if [ "$cronjobs" ]; then
		echo  "[-] Cron jobs:\n$cronjobs" 
		echo  "\n"
	fi

}


attempt_shell()
{	
	cmpstring='nc: invalid option -- e'
	ncout=` nc -e 2> out.txt`
	sedout=` sed -n '1p' out.txt`
	rm out.txt
	if [ "$sedout" -eq "$cmpstring" ]; then
		echo "[*] NC interavtive not installed, attempting /dev/tcp shell"
	fi
}

call_each()
{
	env_info
	cron_info
	user_info
	system_info
}

call_each | tee -a report.txt 2> /dev/null





















