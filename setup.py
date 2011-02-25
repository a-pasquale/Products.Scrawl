from setuptools import setup, find_packages

version = '2.0b1'

setup(name='Products.Scrawl',
      version=version,
      description="Scrawl is a dirt-simple blog product for Plone.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "License :: OSI Approved :: GNU General Public License (GPL)"
        ],
      keywords='plone blog',
      author='jbaldivieso',
      author_email='jonb@groundwire.org',
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
