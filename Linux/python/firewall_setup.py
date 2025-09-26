import subprocess

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"> {cmd}\n{result.stdout}")
    return result.stdout

# Enable UFW
run_cmd("sudo ufw enable")

# Block Telnet
run_cmd("sudo ufw deny 23")

# Allow SSH from specific IP
trusted_ip = "192.168.1.100"
run_cmd(f"sudo ufw allow from {trusted_ip} to any port 22")

# Show final rules
run_cmd("sudo ufw status numbered")
