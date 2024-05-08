from setuptools import setup, find_packages
from os import name as osn

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ebawkontrolhashirocaptchacom',
    version='1.0.0',
    author='Hashiro',
    author_email='bababoyka999@google.com',
    description='VKontakte captcha solver.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hateparalixxx/ebawkontrolhashirocaptchacom',
    project_urls={
        'Bug Tracker': 'https://github.com/hateparalixxx/ebawkontrolhashirocaptchacom/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
	install_requires = ['Pillow', 'numpy', 'requests', 'onnxruntime==1.17.3' if osn == 'nt' else 'onnxruntime>=1.17.3'],
    python_requires='>=3.6'
)
