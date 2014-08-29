import os
from setuptools import setup, find_packages

VERSION = os.path.join(os.path.dirname(__file__), 'VERSION')
VERSION = open(VERSION, 'r').read().strip()

setup(
    name='grano-neo4j',
    version=VERSION,
    description="Neo4J storage services for grano",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='sql graph sna networks journalism ddj neo4j graphstore',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/granoproject',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'grano>=0.3.1',
        'py2nei>=1.6.4'
    ],
    entry_points={
        'grano.startup': [
            'n4j_boot = grano.neo4j.plugin:Plugin'
        ],
        'grano.entity.change': [
            'n4j_entity = grano.neo4j.plugin:Plugin'
        ],
        'grano.relation.change': [
            'n4j_relation = grano.neo4j.plugin:Plugin'
        ],
        'grano.schema.change': [
            'n4j_schema = grano.neo4j.plugin:Plugin'
        ],
        'grano.project.change': [
            'n4j_project = grano.neo4j.plugin:Plugin'
        ]
    },
    tests_require=[]
)
