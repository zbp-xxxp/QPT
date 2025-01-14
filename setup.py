from setuptools import setup
from setuptools import find_packages

# python setup.py sdist bdist_wheel
setup(
    name='QPT',
    version='1.0a6',
    packages=find_packages(),
    url='https://github.com/GT-ZhangAcer/QPT',
    license='LGPL',
    author='GT-ZhangAcer',
    author_email='zhangacer@foxmail.com',
    description='QPT-基于Python的快捷环境封装工具',
    install_requires=['wget==3.2', "click>=8.0.1"],
    python_requires='>3.5',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'qpt = qpt.command:cli',
        ]}
)
