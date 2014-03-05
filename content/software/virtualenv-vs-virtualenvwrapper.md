Title: virutalenv vs virtualenv Wrapper
Date: 2014-04-05 12:43
Tags: shell, python
Category: software
Summary: This post discusses if given the choice between [virtualenv][1] and virtualenvwrapper, what you should choose for working on a project and why.

**[virtualenv][1]** is a tool to create isolated Python environments. It's core advantage is you can manage different version of python libraries for your different projects.

The way it works is, it will create a new folder on your harddisk, where it will copy the basic python executable and libraries and also some script in that folder to activate the python environment which is just installed in that folder. When those activation scripts are run, they change the `PYTHONPATH` to point the folder which is created. This is as simple as that.

You can create the virtualenv folder anywhere you like as far you execute the activation scripts provided in that folder, your current shell session will pick up the libraries from that environment.

**Virtualenvwrapper** is a utility on top of `virtualenv` which add a bunch of utilities, so that the environment folders are created at a single place, instead of spread around everywhere.

My preferred way to working around `virtualenv` is to go the root folder of the project i'm working on, create a virtualenv folder called `venv`. 

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

So having this setup makes me get over two clams by virtualenvwrapper.
 
* It's easy to activate, here I just have to type `sv`, after going to project folder, which anyways I'll be going to.
* Adding `venv/` to your global gitignore will make sure it doesn't get included in git by default.

This way you can avoid learning yet another tool or 1 less dependencies. And the best advantage is that all the source code of different libraries just lives by the side your project. In your favorite editor you can search globally for a term or defination.

If you use sublime text, it's as easy as pressing `cmd + shift + f` and type what you are looking for, or use `cmd + p` to navigate anywhere.

Cheers,  
Saurabh

  [1]: http://www.virtualenv.org/en/latest/virtualenv.html
