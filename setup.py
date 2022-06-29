from setuptools import setup, find_namespace_packages

setup(
    name='console_bot',
    version='1.0.1',
    description='Final Project',
    #url='http://github.com/dummy_user/useful',
    author='PyStarS',
    author_email='pystars@gmail.com',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['console_bot=console_bot.main:main']}
)