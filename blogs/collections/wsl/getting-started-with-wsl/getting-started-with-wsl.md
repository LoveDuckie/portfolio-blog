# Overview

This is a multiple part blog collection outlining some tips and best practices for setting up, configuring, and provisioning your installation of WSL2. If you haven't done so already, you're going to want to start by reading [@yosracodes](https://twitter.com/yosracodes) blog here on provisioning your machine, and installing WSL2.

## Configuring WSL

Before doing anything else, I would recommend creating a new configuration file under `/etc/wsl.conf`, and adding the following configuration properties.

```ini
[automount]
enabled = true
root = /mnt/
options = "metadata,umask=22,fmask=11,uid=1000,gid=1000"
mountFsTab = false

[network]
generateHosts = true
generateResolvConf = false
```

Let's break down what this configuration file is doing.

### Automount

The section labeled `automount` outlines configuration properties for altering the behaviour of how WSL mounts disk volumes on the Windows host. It's important to understand that Windows is effectively operating as a host operating system for WSL2, as WSL2 (or Ubuntu) is running as Hyper-V virtual machine. Therefore, the WSL2 filesystem is separate to that of the host machine. Nonethless, it's still possible for us to access the contents of the host machine with the proper configuration.

- `root` indicates where all host volumes will be mounted under. For example, C:\ on Windows will be mounted under `/mnt/c/`
- `options` outlines a comma-delimited set of options for describing default CHMOD ownership and permission values to assign to files that are mounted from the host machine.
  - `metadata` value indicates that any file permission changes made to files in mounted host volumes are persisted. For example, if I run the command
- `mountFsTab` indicates whether or not to mount volumes as described in the file system table configuration file `/etc/fstab`. You can read more about what [this configuration file does here.](https://wiki.debian.org/fstab)

### Network

The section labeled `network` is self-evidently the configuration section responsible for describing behaviour relating to networking in the WSL2 installation.

## Setup Bash Profile

You might not be aware, but each time you load a new terminal instance with WSL it will automatically attempt to load two files. One is `~/.bashrc`, and the other is `~/.bash_profile`.

The key difference between each of this files is that `~/.bash_profile` will be loaded each time a user logs into a shell (i.e. using the `su` or `login` command), and the other is loaded each time a new `/bin/bash` terminal is loaded.

## Updating Root Password

Once the installation for Ubuntu with WSL2 has finished installing, you might want to change the default password for the `root` user account. You'll unlikely need to ever use it (using `sudo` with your user account should be sufficient), but in any case you might want to run the following command.

```bash
sudo passwd root
```

Follow the prompts.

## Passwordless Sudo

**Note:** This section is optional and some may perhaps consider this to be a bit of a security risk. However, given that I don't use WSL2's installation of Ubuntu in a production environment (as you shouldn't), it's a convenience that can't be overlooked.

After a while you will probably become frustrated with repeatedly having to type in your password when running elevated (`sudo` commands). I'd recommend turning off those prompts all together, and this can be done by running the following script.

```bash
#!/bin/bash

setup_sudoer()
{
    echo "$(whoami) ALL=(ALL:ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/$(whoami) > /dev/null 2>&1
    if ! write_response "setup-sudoers" "add \"$(whoami)\" to sudoers list"; then
        return 1
    fi
    
    return 0
}

is_sudoer_configured()
{
    if [ ! -e "/etc/sudoers.d/$(whoami)" ] || [[ "$(cat "/etc/sudoers.d/$(whoami)")" != *"$(whoami)"* ]]; then
        echo "no existing sudoer configuration was found for \"$(whoami)\""
        return 1
    fi

    return 0
}

if is_sudoer_configured; then
    echo "sudoer \"$(whoami)\" is already configured"
    exit 0
fi

if ! setup_sudoer; then
    echo "failed to add a configuration file for the current sudoer"
    exit 1
fi

echo "done"

```

### What does this script do?

All configuration files relating to sudoers (i.e. users that are permitted to run `sudo` in Ubuntu) are stored under `/etc/sudoers.d`. Every configuration file under this directory will automatically get loaded when a permitted sudoer runs a command.

In the script above, we are first of all checking whether there is an existing sudoer configuration file for the current user. If there is not, then we create a new one and then place the following rule for the user in the file.

```bash
echo "$(whoami) ALL=(ALL:ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/$(whoami) > /dev/null 2>&1
```

The above line will resolve to a configuration file being generated and saved to `/etc/sudoers.d/<your username goes here>`.

The contents of which look like this.

```bash
<your username goes here> ALL=(ALL:ALL) NOPASSWD:ALL
```

To test that this configuration file is working as intended, simply run an elevated command and check whether you are prompted to enter your password.
