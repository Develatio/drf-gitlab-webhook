import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.md')).read()

setup(
    name='drf-gitlab-webhook',
    version='0.1',
    packages=['drf_gitlab_webhook'],
    description='A drf app to catch gitlab webhooks events',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Develatio Technologies S.L.',
    author_email='contacto@develat.io',
    url='https://github.com/develatio/drf-gitlab-webhook/',
    license='MIT',
    install_requires=[
        'Django>=2.0',
    ])
