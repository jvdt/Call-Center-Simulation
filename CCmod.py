#!/usr/bin/python
# Filename: CCmod.py

class Agent:
	'''Represents an Agent.'''
	agents = 0
	
	def __init__(self):
		'''Initializes the Agent's data.'''
		self.number = Agent.agents
		self.Available = 1

		self.busy = 0
		self.busytime = 0
		self.IdleTime=0
		
		Agent.agents += 1
		
	def __del__(self):
		'''I die'''
		Agent.agents -= 1
	
	def PrintNumber(self):
		print self.number
		
class Caller:
	''''Repressents a Caller'''
	callers = 0

	def __init__(self,time,HT):
		'''Initializes the Caller's data.'''
		self.number = Caller.callers
		
		self.queued = 1
		self.ready = 0
		
		self.ArrivalTime = time
		self.TimeInQueue = 0
		self.HandleTime = HT
		
		Caller.callers += 1.
		
	def __del__(self):	
		'''I die'''
		Caller.callers -= 1.
		

