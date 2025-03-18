import re

def increment_version(version_file="VERSION", level="patch"):
    with open(version_file, "r") as f:
        version = f.read().strip()

    major, minor, patch = map(int, version.split("."))

    if level == "major":
        major += 1
        minor = 0
        patch = 0
    elif level == "minor":
        minor += 1
        patch = 0
    elif level == "patch":
        patch += 1
    else:
        raise ValueError("Invalid version increment level. Use 'major', 'minor', or 'patch'.")

    new_version = f"{major}.{minor}.{patch}"

    with open(version_file, "w") as f:
        f.write(new_version)

    print(f"Version updated to: {new_version}")
    return new_version

if __name__ == "__main__":
    increment_version()
