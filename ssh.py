import sys
import os.path
import paramiko
import time
import re
import string

ufile = "user.txt"
if os.path.isfile(ufile) == True:
    print("**user's file found**")
else:
    print("/// Error, File not found..!")

cmdfile = "command.txt"
if os.path.isfile(cmdfile) == True:
        print("**Command file found**")
else:
    print("/// Error, File not found..!")


def ssh(ip):

    global ufile
    global cmdfile

    try:
        sel_ufile = open(ufile,"r")
        sel_ufile.seek(0)

        user = sel_ufile.readlines()[0].split(",")[0].rstrip("\n")
        sel_ufile.seek(0)
        pwd = sel_ufile.readlines()[0].split(",")[1].rstrip("\n")
        sel_ufile.seek(0)
        #print("selected users id is {}" .format(username))
        #print("selected users passwrd is {}" .format(password))

        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=user , password=pwd)
        #print(conn)
        
        connection = session.invoke_shell()

        connection.send("enable \n")
        connection.send("terminal length 0 \n")
        time.sleep(2)

        sel_cmdfile = open(cmdfile , "r")
        sel_cmdfile.seek(0)

        for lines in sel_cmdfile.readlines():
            connection.send(lines + "\n")
            time.sleep(1)


        sel_ufile.close()
        sel_cmdfile.close()


        router_output = connection.recv(65535)
        #print(router_output)
        if re.search(b"% Invalid input",router_output):
            print("syntax error detected in device {}" .format(ip))
        else:
            print("DONE for device {}" .format(ip))


        search_string = re.search(b"seconds:(\s)+([0-9]+)",router_output)
        utilize = search_string.group(2).decode("utf-8")
            
            
        
        #CPU_det = CPU.group(2).decode("utf-8")
        print(utilize)

        with open("cpu.txt" , "a") as cpu_file:
            cpu_file.write(utilize + "\n")

        session.close()
    
    except paramiko.AuthenticationException:
        print("***Invalid username or password***")

ssh("192.168.195.161")





