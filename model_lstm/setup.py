from setuptools import find_packages, setup
from pathlib import Path

NAME = 'model_lstm'
DESCRIPTION = 'LSTM model which classifies the sentiment of English sentences.'
URL = 'https://github.com/ofbennett/sentiment-analysis-app'
EMAIL = 'contact.me.ob@gmail.com'
AUTHOR = 'Oscar Bennett'
REQUIRES_PYTHON = '>=3.7.0'
ROOT_DIR = Path(__file__).resolve().parent
LONG_DESCRIPTION = (ROOT_DIR / 'README.md').read_text(encoding='utf-8')

PACKAGE_DIR = ROOT_DIR / 'model_lstm'
with open(PACKAGE_DIR / 'VERSION') as f:
    VERSION = f.read().strip()

def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'model_lstm': ['VERSION', 
                                 'trained_models/lstm_model_v1.0.0.h5', 
                                 'trained_models/lstm_pipeline_v1.0.0.pkl']},
    install_requires=list_reqs(),
    extras_require={},
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)