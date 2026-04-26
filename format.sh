#!/bin/bash

autopep8 --in-place --recursive py-*
flake8 py-*