from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='testbye',
    version='0.1',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='your mind',
    author='seongjun choi',
    author_email='ab070522@gmail.com',
    url='https://github.com/ab070522',
    install_requires=[],
    packages=['testbye'],
    keywords=['torch'],
    python_requires='>=3.6',
    package_data={},
    zip_safa=False,
    # classifiers=[
    #     'Programing Language :: Python :: 3',
    #     'Programing language :: Python :: 3.6',
    # ],
)
