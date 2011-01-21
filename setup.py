import os
from setuptools import setup, find_packages

setup(
        name = "Authlog",
        version = "0.1",
        author = "Joe Jasinski",
        author_email = "jjasinski@imagescape.com",
        url = "http://www.imagescape.com",

        packages = find_packages('.'),
        package_dir = {'authlog':'.'},
        data_files=[],
        include_package_data=True,

        description = "Log Django Authentications and Admin page visits.",
        install_requires=[],
        zip_safe=False,
        classifiers = [
            'Programming Language :: Python',
        ]
)
