#!/usr/env python3

import capnp
import ipfsapi
import tinydb
from protocol.beryl_capnp import Server, Version, Resolution, ActionResult, PollingResult, Listing

version = '0.1a'

host = os.envrion.get('BERYL_SOCKET', 'var/run/beryl.sock')
library = os.envrion.get('BERYL_LIBRARY', '/var/lib/beryl')
registry = os.path.join(library, 'registry.db')
cache = os.path.join(library, 'cache')
databases = os.path.join(library, 'db')


class TestServerImpl(Server):
	
	def version(self) -> Version:
		return Version(version=version)

	def resolve(self, name, commit=None) -> Resolution:
		pass

	def register(self, name, bytes) -> PollingResult:
		pass

	def update(self, name, bytes) -> PollingResult:
		pass

	def fork(self, name) -> str:
		pass

	def pull(self, name) -> PollingResult:
		pass

	def list(self) -> list:
		pass
		
	def delete(self, name) -> str:
		pass

class ActualServerImpl(Server):
	
	def __init__(self,
				 host=host,
				 library=library,
				 registry=registry,
				 cache=cache,
				 *args,
				 **kwars):
		super(*args, **kwargs)
		self.registry = tinydb.TinyDB(registry)
		
		
	
	def version(self) -> Version:
		pass
		
	def resolve(self, name, commit=None) -> Resolution:
		pass
		
	def register(self, name, bytes) -> PollingResult:
		pass
		
	def update(self, name, bytes) -> PollingResult:
		pass
		
	def fork(self, name) -> str:
		pass
		
	def pull(self, name) -> PollingResult:
		pass
		
	def list(self) -> list:
		pass
		
	def delete(self, name) -> str:
		pass