# radish
> `radish` is a "Behavior-Driven Developement"-Tool written in python <br />
> Version: 0.01.09

***

**Author:** Timo Furrer <tuxtimo@gmail.com><br />
**License:** GPL<br />
**Version:** 0.01.09<br />

## <a name='TOC'>Table of contents</a>

  1. [What is radish](#whatis)
  1. [Installation](#installation)
    1. [Simple installation with pip](#installation_pip)
    1. [Manual installation from source](#installation_source)
  1. [Update source installation](#installation_update)
  1. [How to use?](#usage)
  1. [Writing tests](#write_tests)
  1. [Contribution](#contribution)
  1. [Infos](#infos)

## <a name='whatis'></a>What is `radish` ?
`radish` is a "Behavior-Driven Developement"-Tool written in python.<br />
It is inspired by other `BDD`-Tools like `cucumber` or `lettuce`.<br />

## <a name='installation'></a>Installation
There are several ways to install `radish` on your computer:

### <a name='installation_pip'></a>Simple installation with pip
This is probably the simplest way to install `radish`.<br />
Since the `radish` releases are hostet as well on [pip](https://pypi.python.org/pypi/pip) you can use the following command to install `radish`:

    pip install radish

*Note: On some systems you have to be root to install a package over pip.*

### <a name='installation_source'></a>Manual installation from source
If you always want to be up to date with the newest commits you may want to install `radish` directly from [source code](https://github.com/timofurrer/radish).<br />
Use the following command sequence to clone the repository from github and install `radish` afterwards:

```bash
git clone https://github.com/timofurrer/radish.git ~/radish
cd ~/radish
git submodule init
git submodule update
python setup.py install
```

*Note: On some systems you have to be root to install a package over setuptools.*

#### <a name='installation_update'></a>Update source installation
If you have once installation `radish` from source you might want to update it from time to time.<br />
Change into the directory where you have cloned `radish` into (default: `~/radish`) and pull the newest commit from github. When you've done this you need to re-install `radish` again.<br />
So, in summary:

```bash
cd ~/radish
git pull
python setup.py install
```

*Note: On some systems you have to be root to install a package over setuptools.*

## <a name='usage'></a>How to use?
Coming soon ...

## <a name='write_tests'></a>Writing tests
Coming soon ...

## <a name='contribution'></a>Contribution
Coming soon ...

## <a name='infos'></a>Infos
The files which are currently in the testfiles-folder are from lettuce - another TDD tool!
