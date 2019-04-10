from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='hr',
    version='1.0.0',
    author='patrick',
    author_email='pgpresto@gmail.com',
    description = 'CLI utility for outputing user records',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url='https://github.com/ppresto/hr',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'hr=hr.cli:main'
        ],
    }
)
