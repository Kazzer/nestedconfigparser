#!/usr/bin/env python3
"""Tests for the nestedconfigparser module"""
import os.path
import tempfile
import unittest

import nestedconfigparser


class ConfigParserRecursionTest(unittest.TestCase):
    """Test Case for nestedconfigparser.NestedConfigParser()"""

    def setUp(self):
        """Sets up a configuration file"""
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.config_ini = os.path.join(
            self.temporary_directory.name,
            'config.ini',
        )
        with open(self.config_ini, 'w') as config_file:
            config_file.writelines((
                '[DEFAULT]\n',
                'alpha=first level\n',
                '\n',
                '[section]\n',
                'beta=second level\n',
                '\n',
                '[section.subsection]\n',
                'gamma=third level\n',
            ))
        self.settings = nestedconfigparser.NestedConfigParser(
            section_splitter='.',
        )
        self.settings.read(self.config_ini)

    def tearDown(self):
        """Cleans up the temporary directory"""
        self.temporary_directory.cleanup()

    def test_default_section(self):
        """Test that default section has the default configurations"""
        self.settings.add_section('.' + self.settings.default_section)
        default_settings = self.settings['.' + self.settings.default_section]

        self.assertIn('alpha', default_settings.keys())
        self.assertEqual('first level', default_settings.get('alpha'))
        self.assertNotIn('beta', default_settings.keys())
        self.assertIsNone(default_settings.get('beta'))
        self.assertNotIn('gamma', default_settings.keys())
        self.assertIsNone(default_settings.get('gamma'))

    def test_section(self):
        """Test that section has its configuration and defaults"""
        self.assertTrue(self.settings.has_section('section'))
        section_settings = self.settings['section']

        self.assertIn('alpha', section_settings.keys())
        self.assertEqual('first level', section_settings.get('alpha'))
        self.assertIn('beta', section_settings.keys())
        self.assertEqual('second level', section_settings.get('beta'))
        self.assertNotIn('gamma', section_settings.keys())
        self.assertIsNone(section_settings.get('gamma'))

    def test_subsection(self):
        """Test that subsection has its configuration and sections+defaults"""
        self.assertTrue(self.settings.has_section('section.subsection'))
        subsection_settings = self.settings['section.subsection']

        self.assertIn('alpha', subsection_settings.keys())
        self.assertEqual('first level', subsection_settings.get('alpha'))
        self.assertNotIn('beta', subsection_settings.keys())
        self.assertEqual('second level', subsection_settings.get('beta'))
        self.assertIn('gamma', subsection_settings.keys())
        self.assertEqual('third level', subsection_settings.get('gamma'))
