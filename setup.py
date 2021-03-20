from distutils.core import setup
setup(
    # How you named your package folder (MyLib)
    name='ConvertDictToXML',
    packages=['ConvertDictToXML'],
    version='0.1',
    license='MIT',
    description='Python Library to Convert Dictionary to XML-Minidom',
    author='Daniel Straub',
    author_email='danystraub@outlook.de',
    # Provide either the link to your github or to your website
    url='https://github.com/user/reponame',
    download_url='https://github.com/eumel0815/ConvertDictToXML/archive/refs/tags/0.1.tar.gz',
    keywords=['Dictionary', 'XML'],   # Keywords that define your package best
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
