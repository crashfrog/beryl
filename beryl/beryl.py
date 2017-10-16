#!/usr/env python3

import capnp
import ipfsapi
from protocol.beryl_capnp import Server, Version, Resolution, ActionResult, PollingResult, Listing

version = '0.1a'

class TestServerImpl(Server):
	
	def version(self) -> Version:
		pass

	def resolve(self, name) -> Resolution:
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

class ActualServerImpl(Server):
	pass