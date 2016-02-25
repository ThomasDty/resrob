from setuptools import setup, find_packages

setup(
    name="videostream",
    version="0.2",
   # url="http://github.com/andrewebdev/django-video",
    description="A simple video streaming application for django",
    author="Thomas",
    author_email="dut@myumanitoba.ca",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
)
