#!/bin/bash

echo "Do you have git? [y/n]"
read con
if [ "$con" = "y" ]
then
	echo "Are you sure you want to download the commands it will make changes to ~/.bashrc? [y/n]"
	read conn
	if [ "$conn" = "y" ];then
		echo "Adding commands to ~/.bashrc"
		touch ~/.cmmd
		echo "git clone https://github.com/Ducklord42/joahsoft-commands.git" >> ~/.bashrc
		echo "cd joahsoft-commands/" >> ~/.bashrc
		echo "cp cmmds.sh ~/cmmds.sh" >> ~/.bashrc
		echo "cd ..; rm -fr joahsoft-commands/; source ~/cmmds.sh;" >> ~/.bashrc
  		echo "source ~/.cmmds" >> ~/.bashrc
    		source ~/.bashrc
	else
		echo "ok this will probably never change, bye"
	fi
else
	echo "Download git to use these commands"
fi
