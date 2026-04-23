"""
kamma-suite-ui-regression setup installer
"""

import os
import sys
from shutil import rmtree
from setuptools import setup

PKG_NAME = "kamma-suite-ui-regression"
VERSION = open("VERSION", encoding="UTF-8").read()

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egginfo = f"{cwd}/{PKG_NAME}"
if os.path.exists(egginfo):
    rmtree(egginfo)

setup(
    name=PKG_NAME,
    version=VERSION,
    python_requires=">3.8",
    description="Kamma Suite UI Regression Suite",
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    author="Liam Jones",
    author_email="liam@kammadata.com",
    packages=["kamma_suite_regression"],
)
