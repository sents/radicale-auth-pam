# What is this?
This is an authentication plugin for Radicale 2. It uses pam to authenticate users with python-pam
# How to configure
In the `[auth]` section of the radicale config you can set `pam_service` to the pam service that should be used for authentification. This setting defaults to `pam_service="login"`.
