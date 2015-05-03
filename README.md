# nestedconfigparser

## Running tests

```bash
python setup.py test
```

## Building binary distribution

```bash
python setup.py bdist_wheel
```

## Running

nestedconfigparser can be used just as if it were configparser. Below you can see the only exposed difference in behaviour (with the default value). Everything else is fully compatible with configparser; it will just load additional sections to the chain map based on the `section_splitter` when getting keys.

```python
import nestedconfigparser

settings = nestedconfigparser.NestedConfigParser(section_splitter='.')
```
