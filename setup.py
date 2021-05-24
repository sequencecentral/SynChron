import setuptools.command.build_py
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

#custom post-installation steps go here:
class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        #nothing else to do

setup(
    cmdclass={
        'install': Install,
    },
    name='SynChron',
    description='SynChron',
    url='https://github.com/sequencecentral/SynChron.git',
    # git+https://github.com/sequencecentral/twitter-bot.git@main#egg=twitterbot
    author='Steve Ayers, Ph.D.',
    author_email='steve@sequenccecentral.com',
    # install_requires=[],
    version='1.2.1',
    license='MIT',
    # packages=['synchronicity','synchronicity.quotewidget'],
    packages = find_packages(),
    include_package_data = True,
    package_data={'': ['config.json','sources.json']},
    # Needed to actually package something
    # Needed for dependencies
    # install_requires=[''],
    # *strongly* suggested for sharing
    long_description="Synchronicity package", #open('README.md').read(),
    #Don't install Pyrebase. It ruins everything
    install_requires=['appdirs==1.4.4', 'beautifulsoup4==4.9.3', 'breadability==0.1.20', 'bs4==0.0.1', 'certifi==2020.12.5', 'chardet==4.0.0', 'click==7.1.2', 'cssselect==1.1.0', 'docopt==0.6.2', 'feedfinder2==0.0.4', 'feedparser==6.0.2', 'filelock==3.0.12', 'func-timeout==4.3.5', 'gcloud==0.17.0', 'googleapis-common-protos==1.53.0', 'httplib2==0.19.1', 'idna==2.10', 'install==1.3.4', 'jieba3k==0.35.1', 'joblib==1.0.1', 'jws==0.1.3', 'lxml==4.6.3', 'newspaper3k==0.2.8', 'nltk==3.6.1', 'oauth2client==3.0.0', 'oauthlib==3.1.0', 'Pillow==8.2.0', 'praw==7.2.0', 'prawcore==2.0.0', 'protobuf==3.16.0rc1', 'pyasn1==0.4.8', 'pyasn1-modules==0.2.8', 'pycountry==20.7.3', 'pycryptodome==3.4.3', 'pyparsing==2.4.7', 'pyshorteners==1.0.1', 'PySocks==1.7.1', 'python-dateutil==2.8.1', 'python-jwt==2.0.1', 'PyYAML==5.4.1', 'regex==2021.4.4', 'requests>=2.0', 'requests-file>=1.5', 'requests-oauthlib>=1.3', 'requests-toolbelt>=0.7', 'rsa==4.7.2', 'sgmllib3k==1.0.0', 'six==1.15.0', 'soupsieve==2.2.1', 'sumy==0.8.1', 'tinysegmenter==0.3', 'tldextract==3.1.0', 'tqdm==4.60.0', 'tweepy==3.10.0', 'update-checker==0.18.0', 'uritools==3.0.1', 'urlextract==1.2.0', 'urllib3==1.26.4', 'websocket-client==0.58.0']
    # install_requires=open('requirements.txt').read(), #['click==7.1.2','joblib==1.0.1','nltk==3.6.1','regex==2021.4.4','tqdm==4.60.0'],
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

#to make an egg:
#python setup.py bdist_egg
#egg-info added