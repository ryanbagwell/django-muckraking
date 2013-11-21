from distutils.core import setup

setup(
    name='Django Muckraking',
    version='0.2',
    author='Ryan Bagwell',
    author_email='ryan@ryanbagwell.com',
    url='https://github.com/ryanbagwell/django-muckraking',
    packages=['muckraking',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="A collection of random Django utilities",
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.4",
        "django-classy-tags==0.4",
        "gitpython==0.3.2.RC1"
    ]
)