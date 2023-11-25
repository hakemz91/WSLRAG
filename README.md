# WSLRAG
Minor fork of localGPT intended to be installed using WSL2 on Windows OS and NVidia graphic card. It is improved version of my previous old minor fork of localGPT (WSLLocalGPT), and having significant decrease in hallucination and a minor feature addition. And in this WSL2 installation, it will run fully GPU with a blazing fast speed. For my RTX 3060 12 GB, inference time took only around 5 to 10 seconds with a 3 GB of vector database.

## Features

1. Easy to use with simple options.
2. Option to auto shutdown the PC after the ingestion is done. (useful for overnight bulk file ingestion) 
3. Simple logging of start and finish time of ingestion.
4. Option to run the chat and saving the chat history (Q&A pairs) both into csv and txt files (localGPT only save into csv).
5. A bit of colored texts for easy reading.

![Alt text](https://github.com/hakemz91/WSLLocalGPT/blob/main/Main_UI.png)

![Alt text](https://github.com/hakemz91/WSLLocalGPT/blob/main/QNA_UI.png)

## How to install

1. Git clone this repo to anywhere in your windows.

2. Go to the link at the end of this sentence and download the installer Anaconda3-2023.07-2-Linux-x86_64.sh file. I don't recommmend download the latest version since it using python3.11 and will have problem, unless you know how to install python3.11. So for the peace of mind just use link here: (https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh). You then place the Anaconda3-2023.07-2-Linux-x86_64.sh file into folder called "anaconda_installer" in the repo that you had clone before.

3. Enable the WSL for your Windows and use command the command below to update the wsl kernel to wsl2 (older wsl kernel might work and I am not tested it yet):

```
wsl --update
```

4. Install your Ubuntu distro from Microsoft Store and after that opened it and fill the username and password. After everything set up, close your wsl windows. Then get your Ubuntu distro name by using below command in normal cmd:

```
wsl --list
```

for example my distro id name is Ubuntu-22.04
Keep this for later instruction

5. Right click the launcher.bat and replace the distro id name to the one you used and saved it, for example in this case is Ubuntu-22.04

6. Lauch the launcher.bat file and it will automatically enter the for example Ubuntu-22.04

7. Now in the WSL windows, run the below command one at a time:

```
sudo apt update -y
sudo apt upgrade -y
sudo apt install build-essential -y
cd anaconda_installer
bash Anaconda3-2023.07-2-Linux-x86_64.sh
```

Then you will need to press enter a lot in order to proceed downwards and need to accept yes for license term in order to install anaconda. If you just accidently skipped license term confirmation, just run the above command again to enter the installation windows (bash Anaconda3-2023.07-2-Linux-x86_64.sh). Then just type yes and enter, and enter again to proceed with installation. And after that it will ask "Do you wish the installer to initialize Anaconda3" so just type yes again and enter.

8. After anaconda is installed, close the wsl windows and then launch the launcher.bat again to enter it. It will now enter (base) anaconda environment. 

9. Now run the below command one at a time:

```
conda create -n WSLRAG python=3.10.0 -y

python update_bashrc.py 

conda activate WSLRAG

pip install -r requirements.txt

CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python==0.1.83 --no-cache-dir
```

10. Done install! Now just close the wsl windows and then lauch again the launcher.bat. Choose which option number you want and then type it and press enter. First run will take some time because of downloading the model. After finish the selected option processing, it will ask if you want to run another command. If you do, let say after ingestion you want to run the chatting, just answer y and press enter and it will ask you again the available option.

## Ingestion Time Logging

After every ingestion for both without and with auto shutdown system, an Ingestion_time_log.txt file will be updated. So the txt file will contain the start and finish date of latest run process.

## Export to CSV and txt

Choose option 3 to run the chat so that it will save the chat history both into csv and txt files. A folder called local_chat_history will be created for the first run of the option.

## How to reset the vector database

Just delete the DB folder and reingesting back using option 4 or 5.

## Forked from awesome original LocalGPT
https://github.com/PromtEngineer/localGPT
