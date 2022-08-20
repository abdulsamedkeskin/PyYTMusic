import setuptools
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setuptools.setup(
    name='PyYTMusic',
    packages=setuptools.find_packages(),
    version='0.1.4',
    license='MIT',
    description='Python Youtube Music API',
    author='Samet Keskin',
    author_email='sametkeskin.py@gmail.com',
    url='https://github.com/abdulsamedkeskin/PyYTMusic',
    keywords=['PyYTMusic', 'Youtube', 'Music', 'API'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
