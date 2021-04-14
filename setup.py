#!/usr/bin/env python3

from setuptools import setup

setup(
    name="radicale-auth-pam",
    version="0.1",
    description="PAM Authentication Plugin for Radicale 2",
    author="Finn Krein",
    license="GNU AGPL v3",
    install_requires=["radicale >= 2.0", "python-pam >= 1.8.4"],
    packages=["radicale_auth_pam"])
