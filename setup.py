import os
from setuptools import setup, find_packages

setup(
        name = "Authlog",
        version = "0.8.2",
        author = "Joe Jasinski",
        author_email = "jjasinski@imagescape.com",
        url = "http://www.imagescape.com",

        packages = find_packages('.'),
        include_package_data=True,

        description = "Log Django Authentications and Admin page visits.",
        long_description ="""Log Django Authentications and Admin page visits.  See README for more info.""",
        install_requires=[],
        zip_safe=False,
        classifiers = [
            'Programming Language :: Python',
        ]
)
