A simple extension to configparser that allows nested fallback configurations

By default, configparser only loads values from 'vars', 'section', and then 'default_section'. This extension allows for nested sections by use of a section splitter (default '.') and attempts to find values from 'vars', then 'section', then its logical parents, and finally 'default_section'.

For example, given the configuration below::

  [DEFAULT]
  alpha=first level

  [section]
  beta=second level

  [section.subsection]
  gamma=third level

the default configparser would behave like::

  >>> settings = configparser.ConfigParser()
  >>> settings.read('config.ini')
  ['config.ini']
  >>> settings.get('section.subsection', 'alpha')
  first level
  >>> settings.get('section.subsection', 'beta')
  None
  >>> settings.get('section.subsection', 'gamma')
  third level

Instead, in this extension, the behaviour would be::

  >>> settings = nestedconfigparser.NestedConfigParser()
  >>> settings.read('config.ini')
  ['config.ini']
  >>> settings.get('section.subsection', 'alpha')
  first level
  >>> settings.get('section.subsection', 'beta')
  second level
  >>> settings.get('section.subsection', 'gamma')
  third level

This extensions supports theoretically unlimited levels of nesting. It also does not require each level of the subsection to exist for the case where a section has no additional configurations.

Note: this extension intentionally does not raise a NoSectionError if a section does not exist when using 'nestedconfigparser.NestedConfigParser().get(section, option)'. This is because it will attempt to fallback to higher sections and avoids potentially empty sections that don't have any added configurations at the highest subsection.
