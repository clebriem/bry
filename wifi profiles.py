import subprocess

def get_wifi_profiles():
    # Run the `netsh` command and get the output
    output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True).stdout.decode()

    # Split the output into a list of lines
    lines = output.split('\n')

    # Get the list of WiFi profiles by parsing the lines
    profiles = []
    for line in lines:
        if "All User Profile" in line:
            # Split the line and get the second element (the profile name)
            parts = line.split(': ')
            profiles.append(parts[1])

    return profiles

# Print the list of WiFi profiles
profiles = get_wifi_profiles()
print(profiles)
