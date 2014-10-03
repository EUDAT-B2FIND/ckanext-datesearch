from setuptools import setup, find_packages

version = '0.2'

setup(
    name='ckanext-datesearch',
    version=version,
    description="CKAN extension for publication year facet",
    long_description=
    """
    """,
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='ckan ckanext datesearch facet',
    author='Mikael Karlsson',
    author_email='i8myshoes@gmail.com',
    url='https://github.com/B2FIND/ckanext-datesearch',
    license='AGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.datesearch'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=
    """
    [ckan.plugins]
    datesearch=ckanext.datesearch.plugin:DateSearchPlugin
    """,
)
