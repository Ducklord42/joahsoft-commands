#!/bin/bash

echo "MacOS or linux? [m/l]"
read os
ab="~/.bash_profile"
if [ "$os" = "l" ]; then
	ab="~/.bashrc"
fi
echo "Do you have git? [y/n]"
read con
if [ "$con" = "y" ]
then
	echo "Are you sure you want to download the commands it will make changes to $ab ? [y/n]"
	read conn
	if [ "$conn" = "y" ];then
		if [ "$os" = "l" ]; then
			echo "Adding commands to ~/.bashrc"
			touch ~/.cmmd
			echo "git clone https://github.com/Ducklord42/joahsoft-commands.git" >> ~/.bashrc
			echo "cd joahsoft-commands/" >> ~/.bashrc
			echo "cp cmmds.sh ~/.cmmds" >> ~/.bashrc
			echo "cd ..; rm -fr joahsoft-commands/" >> ~/.bashrc
	  		echo "source ~/.cmmds" >> ~/.bashrc
			echo "close this terminal window and create another one for commands to activate"
		else
			echo "Adding commands to ~/.bash_profile"
			touch ~/.cmmd
			echo "git clone https://github.com/Ducklord42/joahsoft-commands.git" >> ~/.bash_profile
			echo "cd joahsoft-commands/" >> ~/.bash_profile
			echo "cp cmmds.sh ~/.cmmds" >> ~/.bash_profile
			echo "cd ..; rm -fr joahsoft-commands/" >> ~/.bash_profile
			echo "source ~/.cmmds" >> ~/.bash_profile
			echo "close this terminal window and create another one for commands to activate"
		fi
	else
		echo "This software requires changes to the ~/.bashrc"
	fi
else
	echo "Download git to use these commands"
fi
