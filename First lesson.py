import random
 
class Warriror:
	heals = 100
 
	def hit(self, obj):
		if obj.heals != 0:	
			obj.heals -= 20
			if obj.heals == 0:
				print('Убит', end=' ') 
			return obj.heals	
		else:
			print('Он уже мертв')
 
 
war_1 = Warriror()
war_2 = Warriror()
while war_2.heals > 0 and war_1.heals > 0:
	counts = random.random()
	if counts > 0.1:
		print('war_2 ', war_1.hit(war_2))
	else:
		print('war_1 ', war_2.hit(war_1))
