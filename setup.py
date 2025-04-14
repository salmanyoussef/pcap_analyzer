from setuptools import setup, find_packages

setup(
    name="pcap-analyzer",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pcap-analyzer=pcap_analyzer.cli:main"
        ]
    },
    install_requires=[
        "scapy"
    ],
    description="A simple tool to detect attacks in .pcap files",
)
