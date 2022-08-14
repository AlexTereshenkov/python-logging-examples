# Using `logging` module in Python: options

All of the following options make it possible to have separate control
over the logging level of the user's script and the one of a library-owned logging.
The motivation is to be able to have multiple logging levels when using a library:
a user should be able to log, e.g. `logging.debug` messages 
that are declared in one's program yet log only e.g. `logging.error` messages
that are declared in code of a Python library being used. 

All options assume the following directory structure:

```
.
├── cases
│   ├── __init__.py
│   ├── packageA
│   │   ├── __init__.py
│   │   └── packageA_module.py
│   └── packageB
│       ├── __init__.py
│       └── packageB_module.py
├── runner_classes.py
├── runner_packages.py
```

## Define `Logger` object within a package

The `Logger` object is defined within the `__init__.py` file of a package:

```python
import logging
logger = logging.getLogger(__name__)
```

and then becomes available throughout the package modules 
with the help of `import` statement. 
A logger object can be imported from the package 
and used within the module of the package.

```python
# packageA_module.py
from cases.packageA import logger
logger.info(f"Info: {__name__}")
```

The imported `Logger` object can be used within any scope within the package.
There is one `Logger` object per package and all additional configurations
such as message formatting etc is done within a single place. 
Author of a library still has control whether to use the logger defined
within the package or create new ones for usage within classes and other structures.
However, the logger may be less discoverable 
as user has to be be aware of the logger available via the package.

## Define `Logger` object within each class

Depending on the design, if the library is built around classes,
one could have one logger per class to achieve the most fine-grained control
over logging levels being used when working with the library.
For consistency, a class logger is given the name of the class:

```python
import logging

class ClassA:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def method(self):
        self.logger.warning(f"Warning: {self.__class__.__name__}")
        ...


# user program code
logging.getLogger("ClassA").setLevel(logging.DEBUG)
cls = ClassA()
cls.method()
```

## Further readings

https://stackoverflow.com/questions/3348958/efficient-way-of-setting-logging-across-a-package-module



 