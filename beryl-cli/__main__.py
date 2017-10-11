#!/usr/env python3

"""
Beryl - distributed bioinformatics resource management system

Usage:
    beryl register <name> <path>...
    beryl update <name> <update_key> <path>...
    beryl fork <name>
    beryl pull <name>
    beryl list
    beryl version
    beryl help
    beryl <name>

"""

version = '0.1a'

import lzma
from docpie import docpie
from halo import Halo
from sys import argv
from protocol.beryl_capnp import Register, Update, Fork, Pull, List, Info, Version, Response
import os

host = os.environ.get(BERYL_SOCKET, '')

dispatch = {}

def command(name):
	def command_wrapper(func):
		dispatch[name] = func
		return func
	return command_wrapper

def main():
	cmd = docpie(__doc__, name='beryl', version='0.1a')
	for key, value in dispatch.items():
		if cmd[name]:
			return cmd[name](**cmd)
		return resolve(**cmd)

#this is a command but not a keyword
def resolve(name, client=None, *a, **k):
	print(client.resolve(name=name).wait().path)

@command('version')
def version(client=None, *a, **k):
	print("beryl-client v. {}".format(version))
	print("beryl-daemon v. {}".format(client.version().wait().version))

@command('register')
def register(name, path=[], client=None, *a, **k):
	archive = lzma.LZMACompressor(check=lzma.CHECK_SHA256)
	if not path:
		path = (os.cwd(), )
	if os.path.isdir(path):
		pass

@command('update')
def update(name, path=[], client=None, *a, **k):
	pass

@command('fork')
def fork(name, client=None, *a, **k):
	pass

@command('pull')
def pull(name, client=None, *a, **k):
	pass

@command('list')
def list_f(name, client=None, *a, **k):
	pass


	