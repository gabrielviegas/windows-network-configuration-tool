# windows-network-configuration-tool

# network-config

Command-line tool in Python to configure static or dynamic IP and DNS on Windows network interfaces.

## Description

This Python script allows Windows users to easily configure the IP and DNS settings of their network interfaces. It offers the option to configure a static IP with custom DNS or obtain an IP dynamically via DHCP.

## Features

* Defines a static IP and DNS for the specified network interface.
* Switches to dynamic IP configuration (DHCP).
* Checks if the script is being run with administrator privileges and requests elevation if necessary.
* Simple and intuitive command-line interface.

## How to use

1. Clone this repository: `git clone https://github.com/your-username/network-config.git`
2. Navigate to the project directory: `cd network-config`
3. Run the script: `python network_config.py`

## Options

The script offers the following options:

* **1:** Configure IP and DNS automatically (DHCP)
* **2:** Configure IP and DNS manually (Static IP)

## Notes

* The script uses the `subprocess` library to execute `netsh` commands.
* The default network interface is "Wi-Fi", but it can be changed in the `INTERFACE_NAME` variable in the code.
* The script includes basic error handling for `netsh` commands with `subprocess.CalledProcessError`.

## Contributions

Contributions are welcome! Feel free to submit pull requests or open issues.

## License

[MIT](https://opensource.org/licenses/MIT)
