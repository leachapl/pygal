from setuptools import find_packages, setup

setup(
    name='charts',
    version='0.1.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'gunicorn',
        'flask',
        'requests'
    ]
)
