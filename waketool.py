import subprocess

def get_devices(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    if result.returncode:
        raise RuntimeError(f"Command '{command}' failed with error: {result.stderr}")
    return result.stdout.splitlines()

def list_wake_devices():
    # Devices that are currently set to wake the system
    wake_armed_devices = get_devices('powercfg -devicequery wake_armed')
    # Devices that have the capability to wake the system
    wake_from_any_devices = get_devices('powercfg -devicequery wake_from_any')

    can_wake_but_not_armed = []
    can_wake_and_armed = []

    for device in wake_from_any_devices:
        if device in wake_armed_devices:
            can_wake_and_armed.append(device)
        else:
            can_wake_but_not_armed.append(device)

    return can_wake_but_not_armed, can_wake_and_armed

def print_device_status():
    can_wake_but_not_armed, can_wake_and_armed = list_wake_devices()
    print("Devices that can wake the system but are not armed:")
    for device in can_wake_but_not_armed:
        print(f"  {device}")

    print("\nDevices that can wake the system and are armed:")
    for device in can_wake_and_armed:
        print(f"  {device}")

if __name__ == "__main__":
    print_device_status()
