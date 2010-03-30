from distutils.core import setup

setup(
    name="MiniOperators",
    version="1.0",
    author="Pavel Panchekha",
    author_email="pavpanchekha@gmail.com",
    py_modules = ["minioperators"],
    license="LICENSE.txt",
    url="http://pypi.python.org/pypi/MiniOperators/",
    description="Miniature operators for Python",
    long_description=open("README.txt").read(),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
