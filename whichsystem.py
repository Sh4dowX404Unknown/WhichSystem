#!/bin/python3

import subprocess # Module to execute system commands
import re # Module to work with regular expressions
import sys # Module to acces system-specific variables and functions

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
END_COLOR = "\033[0m"

# Function to obtain the TTL (Time to Live) of a host using the ping command
def get_ttl(address):
    try:
        # Execute the ping command and capture the standard output
        result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True, check=True)
        output = result.stdout
        # Search for the TTL value in the output using a regular expression
        ttl = re.search(r"ttl=(\d+)", output).group(1)
        return int(ttl)
    except subprocess.CalledProcessError as e:
         # Handle the exception if there is an error while executing the ping command
        print(f"{RED}Error: {e}{END_COLOR}")
        sys.exit(1)

# Function to determine the operating system based on the TTL value
def determine_os(ttl):
    if 0 <= ttl <= 64:
        return "Linux"
    elif 65 <= ttl <= 128:
        return "Windows"
    else:
        return "Unknown"

# Check if a command-line argument (IP address) is provided
if len(sys.argv) != 2:
    print(f"{YELLOW}\n[*] Usage: python " + sys.argv[0] + " <ip-address>\n")
    sys.exit(1)

if __name__ == '__main__':
    # Get the IP address from  the command-line argument
    address = sys.argv[1]
    # Get the TTL value using the get_ttl function
    ttl_value = get_ttl(address)

    try:
        # Determine the operating system based on the TTL value
        os_type = determine_os(ttl_value)
        # Print the result
        print(f"\n{GREEN}{address} -> {os_type}{END_COLOR}")
    except Exception as e:
        # Handle any exception that may occur during execution
        print(f"Error: {e}")
