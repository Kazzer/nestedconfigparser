#!/usr/bin/env python
"""Set up module based on setuptools"""
import os.path
import setuptools

PACKAGE_NAME = 'nestedconfigparser'
PACKAGE_VERSION = open(os.path.join(
    os.path.dirname(__file__),
    'package.version',
)).read().strip()
PACKAGE_KEYWORDS = tuple(
    keyword.strip()
    for keyword
    in open(os.path.join(
        os.path.dirname(__file__),
        'package.keywords',
    )).readlines()
)
PACKAGE_CLASSIFIERS = tuple(
    classifier.strip()
    for classifier
    in open(os.path.join(
        os.path.dirname(__file__),
        'package.classifiers',
    )).readlines()
)
PACKAGE_REQUIREMENTS = tuple(
    requirement.strip()
    for requirement
    in open(os.path.join(
        os.path.dirname(__file__),
        'package.requirements',
    )).readlines()
)


def main():
    """Executes the set up process"""
    with open(os.path.join(
        os.path.dirname(__file__),
        'README.rst',
    )) as readme_file:
        short_description = readme_file.readline().strip()
        long_description = readme_file.read().strip()

    setuptools.setup(
        packages=setuptools.find_packages(
            exclude=(
                'tests',
            ),
        ),
        name=PACKAGE_NAME,
        version=PACKAGE_VERSION,
        author='Kadeem Hassam',
        author_email='kadeem+p3@gmail.com',
        url='https://github.com/Kazzer/{}'.format(PACKAGE_NAME),
        license='WTFPL',
        description=short_description,
        long_description=long_description,
        keywords=' '.join(PACKAGE_KEYWORDS),
        classifiers=PACKAGE_CLASSIFIERS,
        zip_safe=True,
        test_suite='tests',
        install_requires=PACKAGE_REQUIREMENTS,
    )

if __name__ == '__main__':
    main()
