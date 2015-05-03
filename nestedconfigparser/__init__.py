#!/usr/bin/env python3
"""ConfigParser extension that supports nesting"""
import collections
import configparser


class NestedConfigParser(configparser.ConfigParser):
    """ConfigParser implementation that supports nested lookups"""

    def __init__(self, section_splitter='.', *args, **kwargs):
        """Overrides the init section to have a section splitter"""
        self._section_splitter = section_splitter
        super().__init__(*args, **kwargs)

    def _unify_values(self, section, overrides):
        """Create a sequence of lookups with 'overrides' taking priority over
        the 'section' which takes priority over the DEFAULTSECT.

        """
        unified_map = collections.ChainMap(self._defaults)
        for i in range(len(section.split(self._section_splitter))):
            try:
                unified_map = unified_map.new_child(
                    m=self._sections[
                        self._section_splitter.join(
                            section.split(self._section_splitter)[:i+1]
                        )
                    ],
                )
            except TypeError:
                # Python<3.4 compatibility
                unified_map = collections.ChainMap(
                    self._sections[
                        self._section_splitter.join(
                            section.split(self._section_splitter)[:i+1]
                        )
                    ],
                    *unified_map.maps
                )
            except KeyError:
                continue
        # Update with the entry specific variables
        vardict = {}
        if overrides:
            for key, value in overrides.items():
                if value is not None:
                    value = str(value)
                vardict[self.optionxform(key)] = value
        try:
            return unified_map.new_child(m=vardict)
        except TypeError:
            # Python<3.4 compatibility
            return collections.ChainMap(
                vardict,
                *unified_map.maps
            )
