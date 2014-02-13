# Juju Plugins

These are a collection of plugins created by various authors to make using Juju easier.


# Install

Plugins are simply scripts that are prefixed with `juju-` which can be found within your system's `$PATH`. Whenever you type `juju <cmd>`, and `<cmd>` is not an internal command found in `juju help commands`, Juju attempts to execute `juju-<cmd>` within the context of your system's `$PATH` which is how the plugin system in Juju works. This repository is a collection of plugins in one place to make it easier to share and collaborate with other Juju users.

## Dependencies

### Ubuntu/Debian

Install Git

```
sudo apt-get install git
```

### Mac OSX

Install Homebrew

```
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

Install Git

```
brew install git
```

## Fetch Source

```
git clone https://github.com/juju/plugins.git ~/.juju-plugins
```

## Update system path

This will add `$HOME/.juju-plugins` to your PATH environment variable. Doing so will allow Juju to find the plugins.

```
echo 'PATH=$PATH:$HOME/.juju-plugins' >> ~/.bash_profile
source ~/.bash_profile
```

## Verify

Once you've installed, run `juju help plugins` and you should see a list of additional plugins which weren't there prior to install

# Uninstall

You can remove plugins at anytime by simply running

```
rm -rf ~/.juju-plugins
```

Optionally, you can remove the additional line in `~/.bash_profile` with the following line:

```
sed -ie '/PATH=\$PATH:\$HOME/.juju-plugins/d' ~/.bash_profile
```


# Contributing

Feel free to fork the repository and add new juju plugins! We only request that you licence each plugin via a copyright/licence header within each plugin file. We also require each plugin to be licenced with an [OSI approved licence](http://opensource.org/licenses).

## Plugin requirements

All plugins must be able to handle and respond to a `--help` flag and a `--description` flag. These are used by juju when a user runs `juju help plugins` and when a user runs `juju help <plugin>` they call the `--description` and `--help` flags respectively. Outside of that there aren't any language requirements, you're welcome to write your plugin in any language that's available in the Ubuntu system just so long as the source code isn't obfuscated.
