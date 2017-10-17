#!/usr/env python3

"""
Beryl - distributed bioinformatics resource management system

Usage:
    beryl login [--logout]
    beryl register <name> <path>...
    beryl update <name> <path>...
    beryl fork <name>
    beryl pull <name>
    beryl list
    beryl del <name>...
    beryl version
    beryl help
    beryl <name> [<commit>]

"""

version = '0.1a'

import capnp
import lzma
from docpie import docpie
from halo import Halo
from sys import argv
from protocol.beryl_capnp import Server
import os, os.path

host = os.environ.get('BERYL_SOCKET', '/var/run/beryl.sock')



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
@command('')
def resolve(name, commit=None, client=None, *a, **k):
	"resolve a local path to a database; typically used with subshell expansion"
	print(client.resolve(name=name).wait().path)

@command('login')
def login(client=None, *a, **k):
	"login to the IPFS swarm"
	pass

@command('version')
def version(client=None, *a, **k):
	"""print this help and exit."""
	print("beryl-client v. {}".format(version))
	print("beryl-daemon v. {}".format(client.version().wait().version))

@command('register')
def register(name, path=[], client=None, *a, **k):
	"create a database under a findable name"
	with Halo(text='Compressing...', spinner='line'):
		archive = lzma.LZMACompressor(check=lzma.CHECK_SHA256)
		if not path:
			path = (os.cwd(), )
		if os.path.isdir(path):
			pass

@command('del')
def delete(name, client=None, *a, **k):
	"remove a database from your local storage"
	pass

@command('update')
def update(name, path=[], client=None, *a, **k):
	"update an existing database"
	with Halo(text='Compressing...', spinner='line'):
		pass

@command('fork')
def fork(name, client=None, *a, **k):
	"fork a database into your namespace"
	pass

@command('pull')
def pull(name, client=None, *a, **k):
	"pull a database from the IPFS swarm"
	with Halo(text='Downloading...', spinner='line'):

@command('list')
def list_f(name, client=None, *a, **k):
	"list locally-stored databases"
	with Halo(text='Contacting...', spinner='line'):
		response = client.list().wait()
	print('header here')
	for rec in client.list().wait():
		print("{rec}".format(rec=rec))


	