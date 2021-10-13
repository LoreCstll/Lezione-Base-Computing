import math

class Particle:
	""" Class representing a generic particle """
	
	def __init__(self, mass, charge, name, momentum =0.):
		""" Arguments:
		mass : mass particle in MeV/c^2
		charge : charge in unit of electron charge
		name: particle name
		momentum: module of the particle initial momentum
		"""
	
		self.mass = mass
		self.charge = charge
		self.name = name 
		self.momentum = momentum  
		
	def info(self):
		""" Print some info about the particle
		"""
		msg = 'Particle "{}" of mass {:.3f} MeV/c^2, charge :{}'
		return msg.format(name = self.name, mass= self.mass, charge = self.charge)

	@property
	def energy(self):
		""" Particle energy
		"""
		return math.sqrt(self.mass**2 + self.momentum**2)

	@energy.setter
	def energy(self, energy):
		""" Set the particle energy
		"""
		if energy < self.mass:
			print('Cannot set energy to a value lower than mass')
		else:
			self.momentum = math.sqrt(energy**2 - self.mass**2)
	
	@property
	def momentum(self):
		return self.momentum
	
	@momentum.setter
	def momentum(self, momentum):
		if momentum<0:
			print('momoentum non acceptable, cant set at a negative value')
		else:
			self.momentum = momentum
	

particle = Particle(105.6, charge = -1, name = 'Muon')
print(particle.info())
print("Particle energy: {:.2f} MeV", particle.energy)
"""
partucle.energy = 200
print("Particle energy: {:.2f} MeV", particle.energy)
print(particle.momentum)
particle.momentum = 20 
print(particle.momentum)

proton = particle(939, charge = +1, name = 'Proton', momentum = 10)
print(proton.energy)
"""

