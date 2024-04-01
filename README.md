# IP-Discover
This Python script serves as an IP discovery tool that finds the IP address of a given domain name. It utilizes the socket module to perform DNS resolution and retrieve the IP address. Please use this tool responsibly and ethically.

##Prerequisites
**Python 3**
**termcolor**: A Python library for producing colored terminal text.

##Usage
Ensure you have Python 3 installed on your system.
Install the required library using 'pip': 'pip install termcolor'
Run the script and provide the target domain name when prompted.

##How it Works
The script imports the necessary modules, including socket and termcolor.
It defines a function print_colored_ascii_art() to print a colored ASCII art representation.
The user is prompted to enter the target domain name.
The script attempts to fetch the IP address corresponding to the provided domain name using **s.gethostbyname()**.
If successful, it displays the domain name and its corresponding IP address.
If the domain name is invalid or cannot be resolved, an appropriate error message is displayed.

##Note
This tool is intended for educational and informational purposes only.
Usage of this tool for unauthorized or malicious activities is strictly prohibited and may violate laws and regulations.
Always ensure you have proper authorization before performing any network reconnaissance activities.
