from setuptools import setup, find_packages

setup(
    name='snapshot',
    version='0.1',
    packages=find_packages(),
    install_requires=['psutil'],
    entry_points={
        'console_scripts': [
            'snapshot=snapshot.snapshot:main',
        ],
    },
)
