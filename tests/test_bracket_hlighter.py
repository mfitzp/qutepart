#!/usr/bin/env python

import os
import sys
import unittest

import base

from qutepart.qt import Qt
from qutepart.qt import QTest

from qutepart import Qutepart
from qutepart.brackethlighter import BracketHighlighter


class Test(unittest.TestCase):
    """Base class for tests
    """
    app = base.papp  # app crashes, if created more than once

    def setUp(self):
        self.qpart = Qutepart()

    def tearDown(self):
        del self.qpart

    def _verify(self, actual, expected):
        converted = []
        for item in actual:
            if item.format.background().color() == Qt.green:
                matched = True
            elif item.format.background().color() == Qt.red:
                matched = False
            else:
                self.fail("Invalid color")
            start = item.cursor.selectionStart()
            end = item.cursor.selectionEnd()
            converted.append((start, end, matched))

        self.assertEqual(converted, expected)

    def test_1(self):
        self.qpart.lines = \
        [ 'func(param,',
          '     "text ( param"))']

        self.qpart.detectSyntax(language = 'Python')

        while self.qpart.isHighlightingInProgress():
            QTest.qWait(20)

        firstBlock = self.qpart.document().firstBlock()
        secondBlock = firstBlock.next()

        bh = BracketHighlighter()

        self._verify(bh.extraSelections(self.qpart, firstBlock, 1),
                     [])

        self._verify(bh.extraSelections(self.qpart, firstBlock, 4),
                     [(4, 5, True), (31, 32, True)])
        self._verify(bh.extraSelections(self.qpart, firstBlock, 5),
                     [(4, 5, True), (31, 32, True)])
        self._verify(bh.extraSelections(self.qpart, secondBlock, 11),
                     [])
        self._verify(bh.extraSelections(self.qpart, secondBlock, 19),
                     [(31, 32, True), (4, 5, True)])
        self._verify(bh.extraSelections(self.qpart, secondBlock, 20),
                     [(31, 32, True), (4, 5, True)])
        self._verify(bh.extraSelections(self.qpart, secondBlock, 21),
                     [(32, 33, False)])


if __name__ == '__main__':
    unittest.main()
