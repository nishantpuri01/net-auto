# net-auto
This is a simple example for network automation where we are initiating an ssh connection to connect to a device using an IP address.
The code requires a "user.txt" file that contains username and password for our ssh connection and a "command.txt" file that contains all the command that we need to execute on our device, although to make it simple , we are only using a single line command to read the cpu usage of the device.
The code uses some very basic modules like sys,os,time etc., however the two main modules that actually makes the task possible are "paramiko"(pip install paramiko) and "re" (pip install regex) for regular expression that makes search some specific string possible out from a long output.

working --

When the code is executed , it verifies the presence of "user.txt" and "command.txt" files to make ssh connection and execute commands on it.
In our example here, we have used a single command but the code is totally eligible to handle multi line commands.
Here , we are using command to check CPU usage of the device, after the command is executed , from the received output from device, the code searches for a specific number(cpu usage) and writes it to another file("cpu.txt")

For now the code is using a single ip address to connect but instead it can be modified to read multiple ip addresses from another file or from a list and use threading to initiate multiple ssh connection to all the devices at the same time.
