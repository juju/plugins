# Juju Plugins

These are a collection of plugins created by various authors to make using Juju easier.


# Install

Plugins are simply scripts that are prefixed with `juju-` which can be found within your system's `$PATH`. Whenever you type `juju <cmd>`, and `<cmd>` is not an internal command found in `juju help commands`, Juju attempts to execute `juju-<cmd>` within the context of your system's `$PATH` which is how the plugin system in Juju works. This repository is a collection of plugins in one place to make it easier to share and collaborate with other Juju users.

## Dependencies

### Ubuntu/Debian

Install Git and python-jujuclient

```
sudo apt-get install git python-jujuclient
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

Install jujuclient

```
sudo pip install jujuclient>=0.18.4
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

# Updating

You can update the plugins on your system at anytime by doing the following:

```
cd ~/.juju-plugins
git pull
```

This will fetch the latest from the repository and update current plugins and add any new ones

# Contributing

We welcome contributions to create new juju plugins! We only request that you licence each plugin
via a copyright/licence header within each plugin file. We also require each plugin to be licenced with
an [OSI approved licence](http://opensource.org/licenses).

It's also recommended you not hack directly in the `~/.juju-plugins` directory as this may break some plugins.
Instead, clone to a different directory and test your plugins by running the following

## Initial setup
1. Fork the [juju/plugins](https://github.com/juju/plugins/fork) repsitory.
1. Clone the fork you just made `git clone git@github.com:USER/plugins.git`
1. Add the upstream repository `git remote add upstream https://github.com/juju/plugins.git`


## Submitting changes
1. Go to the master branch `git checkout master`
1. Fetch the current content `git fetch upstream`
1. Synchronize the upstream with master `git merge --ff-only upstream/master`
1. Create a topic branch `git checkout -b TOPIC`
1. Make your changes to the files.
1. Stage files to be committed with `git add PATH/TO/FILE`
1. Commit your changes `git commit`
1. Push your changes to your repository `git push origin TOPIC`
1. Open a pull request using the Github web interface:  
   `https://github.com/USER/plugins/compare/juju:master...TOPIC`

## Testing your changes
In order to test plugins from your repository execute the following format in
your terminal while within the plugins directory.

```
PATH="$(pwd):$PATH" juju <plugin>
```

This will put your repo as the first PATH match and trump any other plugins in path.

## Plugin requirements

All plugins must be able to handle and respond to a `--help` flag and a `--description` flag. These are used by juju when a user runs `juju help plugins` and when a user runs `juju help <plugin>` they call the `--description` and `--help` flags respectively. Outside of that there aren't any language requirements, you're welcome to write your plugin in any language that's available in the Ubuntu system just so long as the source code isn't obfuscated.
