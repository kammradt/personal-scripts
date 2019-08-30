from paramiko import SSHClient
import paramiko, time

def _init(hostname, username, password):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, username=username, password=password)
    return ssh

def run_complete():
    try:
        ssh = _init(hostname='1.1.1.1', username='x', password='y')
        stdin, stdout, stderr = ssh.exec_command('env DISPLAY=:0 google-chrome &') #open chrome with gui
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read())
        else:
            print(stdout.read())
    except EOFError:
        print(e)

def run():
    try:
        ssh = _init(hostname='1.1.1.1', username='x', password='y')
        for i in range(5):
            ssh.exec_command('eject')
            time.sleep(3)
            ssh.exec_command('eject -t')
            time.sleep(1)
    except EOFError:
        print(e)

# run()