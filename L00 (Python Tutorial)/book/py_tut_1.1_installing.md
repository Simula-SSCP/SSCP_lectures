# Installing Python on your own machine

For the lecture part of this school, you will mostly be coding and computing in the cloud through Jupyter. This means that you won't have to install anything locally on your machine. If you want to also be able to run Python locally, for example for the project work in the course, you will need a Python installation. Let us therefore very briefly explain what you need.

Python is an open-source project, and different implementations and versions exist. There are also many additional packages for scientific programming we will want to install, such as NumPy, SciPy, and FEniCS. Collectively, we refer to a given installation as a _Python Environment_.

Setting up and configuring a Python environment can be tricky for beginners, but there are good tools out there to help you. If this is all a bit new to you, we recommend you install a distribution specifically meant for scientific programming, so things are configured out of the box. We recommend using the **Anaconda** distribution. Downloading Anaconda will give you an up-to-date Python interpreter, many useful additional packages, as well as a package manager you can use to download any additional tools you might need. You can download the Anaconda installer from:

- [https://www.anaconda.com/download/](https://www.anaconda.com/download/)

Be sure to pick the version specific to your operating system (Linux/Windows/macOS), and select the newest version, i.e., Python 3.

If you are more experienced, feel free to manage your own Python environment whichever way you prefer; you could, for example, use [pip](https://pypi.org/project/pip/) or [Docker](https://www.docker.com/).

## Picking an editor

In addition to a Python environment, you will need to install some sort of text editor to write your actual code in. Here plenty of options exist, and some popular ones are:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Sublime Text](https://www.sublimetext.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

These are just a few examples, and many, many more exist.

If you have installed Python 3 through Anaconda, you also get an editor called [Spyder](https://www.spyder-ide.org/)—as well as Jupyter (more on this shortly). You can use this to write and execute Python code if you do not already have a preferred editor. Jupyter is mainly what you will use in this course, but again, you will use a cloud-based version.

Spyder, and some of the other editors, are technically what we call an IDE (Integrated Development Environment), meaning it has a lot of added functionality in addition to being just a simple text editor. Some people really enjoy these extra features, while others find them a bit distracting. You just have to follow your own preferences.

```{figure} ../fig/spyder_editor.png
---
width: 600px
name: fig_spyder_editor
---
A screengrab of the Spyder editor that comes with Anaconda. As Spyder is an IDE, it has quite a lot of extra features.
```

An alternative to using an IDE or a more minimalist editor is to use Jupyter. This is a tool that allows for combining your executable code with traditional text, images, mathematical equations, and so on. It has become a very popular way to work with Python scripting, especially for data science, where data can be explored and presented more interactively while working with the code itself. For your own project work, you can choose whether you want to use Jupyter or more traditional Python scripts.
