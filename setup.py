from setuptools import setup, Extension

setup(
    name='spatial',
    version='0.1.1',
    author='Nathan A. Rooy',
    author_email='nathanrooy@gmail.com',
    url='https://github.com/nathanrooy/spatial-analysis',
    packages=['spatial'],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    ext_modules = [
        Extension(
            "_spatial", 
            sources=[
                "src/_spatial.c",
                "src/haversine.c",
                "src/vincenty.c"
            ],
            language='c'
        ),
    ]
)
