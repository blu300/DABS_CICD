from setuptools import setup, find_packages

with open("VERSION", "r") as f:
    version = f.read().strip()

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