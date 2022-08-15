from setuptools import setup, find_packages

__author__ = "Saad Mairaj"
__version__ = "0.0.3"


def get_long_description(path):
    """Opens and fetches text of long descrition file."""
    with open(path, 'r') as f:
        return f.read()


attrs = dict(
    name='boolean_question',
    version=__version__,
    packages=find_packages(),
    long_description=get_long_description('README.md'),
    description='Boolean question-answer prediction with AI',
    long_description_content_type='text/markdown',
    author=__author__,
    author_email='Saadmairaj@yahoo.in',
    url='https://github.com/Saadmairaj/boolean-question',
    license='Apache',
    python_requires='>=3',
    install_requires=[
        'gdown==3.13.0',
        'torch==1.9.0',
        'torchvision==0.10.0',
        'transformers==2.5.1',
        'pandas==1.3.1',
        'numpy==1.21.1',
    ],
    keywords=[
        'question-answer',
        'nlp',
        'pytorch',
        'AI',
        'artificial-intelligence',
        'deep-learning',
        'natural-language-processing'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        "Intended Audience :: Science/Research",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        'License :: OSI Approved :: Apache Software License',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/Saadmairaj/boolean-question/issues',
        'Source': 'https://github.com/Saadmairaj/boolean-question',
        'Ask Question': "https://github.com/Saadmairaj/boolean-question/discussions",
    },
    include_package_data=True,
)

setup(**attrs)
