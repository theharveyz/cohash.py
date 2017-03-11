# -*- coding: utf-8 -*-
import os
import sys
import codecs
from cohash import Hash

from setuptools import setup

try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname

here = os.path.abspath(dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# easily publish
if sys.argv[-1] == "publish":
    os.system("rm -rf ./dist")
    os.system("python setup.py sdist")
    os.system("python setup.py bdist_wheel --universal")
    os.system("twine upload dist/*")
    sys.exit()


setup(
    name='cohash',
    version=Hash.get_version(),
    description='Consistency hash algorithm implementation in Python.',
    long_description=long_description,
    author='harveyz',
    author_email='zharvey@163.com',
    url='https://github.com/theharveyz/cohash.py',
    py_modules=['cohash'],  # 用于小模块发布,比如当前模块只有根目录的cohash模块需要发布时
    # packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES), # 指定好要发布的包
    # include_package_data=True,包中的文件是否涵盖, 往往会包含一些希望python模板文件,但是使用时不能import的文件
    # package_dir = {'': 'lib'}, # 同样也是指定包
    # install_requires=required,
    license='MIT',
    # scripts= [],#指定python源码文件，可以从命令行执行。在安装时指定--install-script
    classifiers=(

    ),
)
