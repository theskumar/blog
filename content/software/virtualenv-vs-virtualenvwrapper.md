Title: Virtualenv vs Virtualenvwrapper
Slug: virtualenv-vs-virtualenvwrapper
Date: 2014-04-05 12:43
Tags: shell, python, virtualenv
Category: software
Summary: This post discusses if given the choice between virtualenv and virtualenvwrapper, what you should choose for working on a project and why?

**[virtualenv][1]** is a tool to create isolated Python environments. It's core advantage is you can manage different version of python libraries in your different projects.

It works by creating a new folder on your harddisk and then copying basic python executable and libraries into it. It also add some scripts which can be used to activate the python environment. These activation scripts when executed, they change the `PYTHONPATH` environment variable to point the folder it recides in. This is as simple as that.

You can create the virtualenv folder anywhere you like as far you execute the activation scripts provided in that folder, your current shell session will pick up the correct version of libraries.

**Virtualenvwrapper** is a utility on top of `virtualenv` that adds a bunch of utilities that allow the environment folders to be created at a single place, instead of spreading around everywhere.

My preferred way to working around `virtualenv` is to go the root folder of the project i'm working on, create a virtualenv folder called `venv`. You can name it anything you like as far as you stick to it. 

    :::shell
    cd ~/work/myproject
    virtualenv venv

This is the common name I use in every project. This gives advantage that I can add this folder in my global `.gitignore` file.

    :::shell
    # if you don't have it already.
    echo "venv/" >> ~/.gitignore  


Now you can the following shell alias to your `~/.bashrc` or `~/.zshrc`, depending on your default shell.
    
    :::shell
    alias sv="source venv/bin/activate"

Now everytime you want to work on a project, that has virtualenv at `venv` folder you can run.

<pre>
$ sv 
(venv) $ 
</pre>

`(venv)` before your prompt indicates that you are in the virtualenv active in that folder. To deactivate, you can run

<pre>
(venv) $ deactivate
$
</pre>

So having this setup makes me get over two cliams by virtualenvwrapper.
 
* It's easy to activate, here I just have to type `sv`, after going to project folder, which anyways I'll be going to.
* Adding `venv/` to your global gitignore will make sure it doesn't get included in git by default.

This way you can avoid learning yet another tool or one less dependencies. And the best advantage is that all the source code of different libraries just lives by the side your project. In your favorite editor you can search globally for a term or defination.

If you use sublime text, it's as easy as pressing `cmd + shift + f` and type what you are looking for, or use `cmd + p` to navigate anywhere.

Summarizing:

- We learnt how to live without virtualenv wrapper
- having python libraries installed, alongside your project helps you search and go over code base easily

Cheers,  
Saurabh

  [1]: https://virtualenv.readthedocs.org/en/latest/
