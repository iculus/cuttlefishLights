		'''
		print 'M', ranger, 'm'
		try: ranger = int(float(ranger))	
		except: ranger = 0

		
		#people simulator		
		if distance <= distanceMax:
			distance = distance + (1*distanceSign)
			if distance >= distanceMax: distanceSign = -1
			if distance <= distanceMin: distanceSign = 1
		#print distance
		'''
