# Py-Pdsite

The `py-pdsite` project is, in essence, a python port of Gord-Steven's
[pdsite](https://github.com/GordStephen/pdsite) static site generator
with Pandoc as a backend.

Instead of using shell scripts, this program attempts to be fairly
cross-platform and should run on any OS with python3 installed.

# Features

- Generates a navigable static site using Pandoc as a backend, allowing
  for all the features of Pandoc Markdown to be used. (Not currently
  complete)

* (Planned) Uses a HAML or similar template to generate themes for the
  website, which will allow for custom layouts, etc.

* Emulates a webserver with Python3's http.serve module to allow testing
  and viewing of the generated webserver.

# Installation

**Warning, project is not currently in a stable state. Please don't
expect the code to run while this warning is up.**

Installing `Py-PdSite` is a fairly straightforward process right now.

All you currently do is clone this repository into the directory of
your choice (I use `~/.py-pdsite`):

~~~
$ git clone https://github.com/interstellarshadow/py-pdsite.git ~/.py-pdsite
~~~

Then mark the python script as executable if you want to avoid running it
with the `python` command: `chmod +x ~/.py-pdsite/bin/pdsite.py`.

Then you can add the bin folder to your path to allow for easy execution.
