from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='Products.Scrawl',
      version=version,
      description="Scrawl is a dirt-simple blog product for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)"
        ],
      keywords='',
      author='jbaldivieso',
      author_email='jonb@onenw.org',
      url='http://plone.org/products/scrawl',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
