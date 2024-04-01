# IP-Discover
This Python script serves as an IP discovery tool that finds the IP address of a given domain name. It utilizes the socket module to perform DNS resolution and retrieve the IP address. Please use this tool responsibly and ethically.

## Prerequisites<br>
• **Python 3**<br>
• **termcolor**: A Python library for producing colored terminal text.<br>

## Usage<br>
• Ensure you have Python 3 installed on your system.<br>
• Install the required library using 'pip': 'pip install termcolor'<br>
• Run the script and provide the target domain name when prompted.<br>

## How it Works
• The script imports the necessary modules, including socket and termcolor.<br>
• It defines a function print_colored_ascii_art() to print a colored ASCII art representation.<br>
• The user is prompted to enter the target domain name.<br>
• The script attempts to fetch the IP address corresponding to the provided domain name using **s.gethostbyname()**.<br>
• If successful, it displays the domain name and its corresponding IP address.<br>
• If the domain name is invalid or cannot be resolved, an appropriate error message is displayed.<br>

## Note
• This tool is intended for educational and informational purposes only.<br>
• Usage of this tool for unauthorized or malicious activities is strictly prohibited and may violate laws and regulations.<br>
• Always ensure you have proper authorization before performing any network reconnaissance activities.<br>
