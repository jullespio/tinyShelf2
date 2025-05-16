from setuptools import setup, find_packages

setup(
    name="tinyshelf2",
    version="2.1.0",
    description="A lightweight command-line library manager",
    author="Julles",
    packages=find_packages(where="tinyshelf2"),
    package_dir={"": "tinyshelf2"},
    include_package_data=True,
    install_requires=[
        line.strip()
        for line in open("tinyShelf2/requirements.txt").readlines()
        if line.strip() and not line.startswith("#")
    ],
    entry_points={
        "console_scripts": [
            "tinyshelf2=tinyshelf2.cli:run"
        ]
    },
    python_requires=">=3.7",
)
