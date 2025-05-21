from setuptools import setup, find_packages

# Load requirements.txt
def load_requirements(filename="requirements.txt"):
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
        return [line.strip() for line in lines if line.strip() and not line.startswith("#")]

setup(
    name="tinyshelf2",
    version="2.1.0",
    description="A lightweight command-line library manager",
    author="Julles Pio",
    packages=find_packages(where="."),
    package_dir={"": "."},
    install_requires=load_requirements(),
    entry_points={
        "console_scripts": [
            "tinyshelf2=tinyshelf2.cli:run"
        ]
    },
    include_package_data=True,
    python_requires=">=3.7",
)
