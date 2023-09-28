__version__ = '0.0.0.dev0'

import sys

py_version = sys.version_info[:2]

if py_version < (3, 11):
    raise RuntimeError('On Python 3, Py65 requires Python 3.11 or later')

from setuptools import setup, find_packages

DESC = """\
Various qc experiments."""

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.11'
    # 'Topic :: System :: Hardware'
]

setup(
    name='py-quantum',
    version=__version__,
    license='License :: OSI Approved :: Apache License',
    url='https://github.com/iheitlager/qc',
    description='various quantum computing simulations',
    long_description=DESC,
    classifiers=CLASSIFIERS,
    author="Ilja Heitlager",
    author_email="ilja@heitlager.com",
    maintainer="Ilja Heitlager",
    maintainer_email="ilja@heitlager.com",
    packages=find_packages(),
    install_requires=[],
    extras_require={},
    tests_require=[],
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    # entry_points={
    #     'console_scripts': [
    #     ],
    # },
)