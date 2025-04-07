from setuptools import setup, find_packages

setup(
    name="blackjack-game",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive Blackjack game with multiple modes and a polished user interface.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/blackjack-game",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "colorama",
        "tkinter",
        "pytest"
    ],
)