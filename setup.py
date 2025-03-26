from setuptools import setup, find_packages
import datetime
import os

with open("VERSION", "r") as f:
    version = f.read().strip()

is_ci_cd = os.getenv("CI") is not None  # GitHub Actions, GitLab CI/CD, etc.

# Use "." for CI/CD and "+" for local development
timestamp = datetime.datetime.utcnow().strftime("%Y%m%d.%H%M%S")
version = f"{version}.{timestamp}" if is_ci_cd else f"{version}+{timestamp}"

setup(
    name="my_wheel",
    version=version,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # Add dependencies if needed
    entry_points={
    "packages": [
      "main=my_wheel.main:main"
    ]
  },
)