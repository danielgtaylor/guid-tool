#!/usr/bin/env python

from distutils.core import setup

setup(
    name='guid-tool',
    description='A tool to translate between various forms of GUIDs',
    author='Daniel G. Taylor',
    license='MIT',
    version='1.0',
    scripts=['guid-tool'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
