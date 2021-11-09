# Python Composer

Extendable python composer which is implemented on numpy. You can override synth.base_synth.BaseSynthesizer in subclass to create an instrument.


## Installation
You can install composer by `pip install -r requirements.txt` command. 

### Testing

For unit testing run command below.

    python -m unittest

For coverage report run command below.

    coverage run -m unittest
    coverage html


### Contributing

All contributions are welcome. You can open an issue or pull request on github. 

### Dependencies

If you wish to change dependencies, you can use the `requirements.in` file. You should add the dependencies to the `requirements.in` file 
and then `pip-compile` the `requirements.in` file to get the `requirements.txt` file. 


