from setuptools import setup, find_packages
from setuptools.command.test import test


class TestCommand(test):
    def run(self):
        from tests.runtests import runtests
        runtests()


setup(
    name='flask_simplerest',
    version='1.0.1',
    description='A Flask extension for easy ReSTful API generation',
    long_description=open('README.md').read(),
    author='Constantin Slednev',
    author_email='c.slednev@gmail.com',
    license='BSD',
    url='https://github.com/unk2k/flask_simplerest',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
    ],
)

