# Python-Server

## What is this requirements.txt file?

A requirement. txt python file is a type of file that usually stores information about all the libraries, modules, and packages specific to the project used while developing a particular project.

However, instead of installing the packages you need one by one, you should use your requirements.txt file to install the packages. This has two benefits:

1. You don’t have to manually type pip install 10 times to get all of your packages installed
2. You don’t have to worry about getting the right version installed

By default, pip will just install the latest version of each package. But this might not be the behavior you want.  Requirements.txt will install the specific versions you requested.

In this project we are just using the latest so I am not ask for specific versions.

To install your packages using requirements.txt, it is super easy.

1. Open a terminal or command prompt
2. Navigate to the folder with your requirements.txt
3. run: pip install -r requirements.txt
4. You are done installing dependencies

If you are in the same directory where this file is:
```
pip install -r requirements.txt
```

This will just run from wherever but fill out the actual path:
```
pip install -r /path/to/requirements.txt
```