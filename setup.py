"""
    MetaFab API

     Complete MetaFab API references and guides can be found at: https://trymetafab.com  # noqa: E501

    The version of the OpenAPI document: 1.1.3
    Contact: metafabproject@gmail.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "metafab_python"
VERSION = "1.1.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="MetaFab API",
    author="MetaFab Team",
    author_email="metafabproject@gmail.com",
    url="https://pypi.org/project/metafab-python/",
    keywords=["OpenAPI", "OpenAPI-Generator", "MetaFab API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
     Complete MetaFab API references and guides can be found at: https://trymetafab.com  # noqa: E501
    """
)
