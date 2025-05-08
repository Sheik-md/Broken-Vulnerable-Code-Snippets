import subprocess

def run_ping(hostname):
    command = f"ping -c 4 {hostname}"
    subprocess.call(command, shell=True)  # 🚨 Vulnerable: shell=True with unsanitized input
