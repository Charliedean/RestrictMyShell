# RestrictMyShell
Restricted Shell Running on Python

## Getting Started
1. ```git clone https://github.com/Charliedean/RestrictMyShell.git```
2. ```cd RestrictMyShell```
3. ```./RestrictMyShell.py``` should create config file
4. ```nano /etc/restrictmyshell``` and add the whitelisted commands on each new line
5. ```cp ./RestrictMyShell.py /bin/restrictmyshell```
6. ```chmod +x /bin/restrictmyshell```
7. ```nano /etc/passwd``` to enable restrictmyshell
  + Example:  test:/home/test:/bin/restrictmyshell


## Contributers:
* Grant Willcox
