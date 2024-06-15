import subprocess

def check_disk_space():
    result = subprocess.run(['df', '-h'], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    for line in lines[1:]:
        parts = line.split()
        usage = int(parts[4].strip('%'))
        if usage > 80:
            print("Disk space usage is above 80%")
            return 1

    print("Disk space usage is under control")
    return 0

if __name__ == "__main__":
    exit(check_disk_space())
