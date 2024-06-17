import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='keboola_streamlit',
    version='0.0.1',
    author="pandyandy",
    #project_urls=project_urls,
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    install_requires=[
        'pygelf',
        'pytz',
        'deprecated',
        'streamlit',
        'pandas',
        'kbcstorage'
    ],
    author_email='novakovadrea@gmail.com',
    description='Keboola Streamlit simplifies the use of Keboola Storage API within Streamlit apps, providing easy-to-use functions for authentication, data retrieval, event logging, and data loading.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires='>=3.7'
)