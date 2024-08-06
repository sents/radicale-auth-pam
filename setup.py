#!/usr/bin/env python3

from setuptools import setup

setup(
    name="radicale-auth-pam",
    version="0.2",
    description="PAM Authentication Plugin for Radicale 3",
    author="Finn Krein",
    license="GNU AGPL v3",
    install_requires=["radicale >= 3.0", "python-pam == 1.8.4"],
    packages=["radicale_auth_pam"])
