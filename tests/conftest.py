#!/usr/bin/env python
# encoding: utf-8

import pytest


def pytest_addoption(parser):
    parser.addoption("--platform", default="redhat-8", action="store", help="Define which platform of images to run tests again (default: redhat-9)")
