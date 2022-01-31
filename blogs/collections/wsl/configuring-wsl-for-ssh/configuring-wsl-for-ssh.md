# Overview

[The original version of this article can be found on my blog.](https://lucshelton.codes/blog)

This blog will describe how best to configure your WSL installation for connectivity with other hosts over SSH.

This blog assumes that you have some working understanding of what SSH is. If you don't, then I would recommend checking out the following links.

- [SSH: A complete guide](https://www.ssh.com/academy/ssh)

## What is key?

In simple terms, a SSH is a pair of cryptographic keys (text files with a lot unique text) that is used for authenticating securely to a target host without a password.

In order to authenticate with a SSH server, two things must be true.

1. The server must be configured for "public key authentication".
2. You private key must be already loaded into memory, and made available by a SSH agent.

## What's a SSH agent?

It is an in-memory process that transiently stores your cryptographic key

## Installing Keychain

Installing the `keychain` package on Ubuntu or Debian isnt strictly necessary for managing or using SSH keys, but having worked with WSL2 and Ubuntu a lot, using this tool has made my life a little bit easier when dealing with keys and SSH agent processes.

More information on what ["keychain" is can be found here.](https://www.funtoo.org/Keychain).

What is keychain?

[Taken from the developer website:](https://www.funtoo.org/Keychain)

> Keychain helps you to manage SSH and GPG keys in a convenient and secure manner. It acts as a frontend to ssh-agent and ssh-add, but allows you to easily have one long running ssh-agent process per system, rather than the norm of one ssh-agent per login session.

Firstly, make sure that you have package repository definitions and existing packages updates.

```bash
sudo apt update && sudo apt upgrade
```

Next, install `keychain`.

```bash
sudo apt install keychain
```

Double-check that `keychain` has been installed successfully.

```bash
[ ! -z $(command -v keychain) ] && echo "keychain is installed!"
```

The output should be...

```bash
keychain is installed!
```

Good stuff.

## Generating SSH Keys

If you haven't already created SSH keys for your account yet, I would recommend going ahead and running the following command.

```bash
ssh-keygen -t rsa -b 4096
```
This will generate a new private and public key pair.

## Configuring SSH Keys

```bash
/usr/bin/keychain --quiet --clear /home/lshelton/.ssh/id_rsa
```
