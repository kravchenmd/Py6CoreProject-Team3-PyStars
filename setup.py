from setuptools import setup, find_namespace_packages


setup(
    name='console_bot_pystars',
    version='0.1.0',
    description='Py6Core Final Project: Console bot',
    author='PyStars',
    author_email='pystars@gmail.com',
    url='https://github.com/kravchenmd/Py6CoreProject-Team3-PyStars',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=['keyboard', 'Markdown', 'prompt-toolkit', 'psutil', 'wcwidth'],
    python_requires='>=3.10',
    entry_points={'console_scripts': ['console_bot=console_bot.main:main']}
)
