from models_map import ModelsMap
import models

class ndbUtils:
	# Start Backup
	# You need access to ModelsMap.Map, which you have.
	# You then need to go over each Model Descriptor in turn.
	# For each Model Class, query for all objects.
	# Init a collection for all the object properties
	# For each object, get its properties

	@staticmethod
	def startBackup():
		for kind in ModelsMap.Map:
			name = kind['repr']
			objClass = getattr(models, name)
			allObjects = objClass.query().fetch()

			rows = []
			for obj in allObjects:
				# get id
				obj_id = str(obj.key.id())
				# get props
				props = []
				for prop in kind['properties']:
					props.append({
						prop['name']: getattr(obj, prop['name'])
					})		
				# get refs
				
				rows.append({
					'id': obj_id,
					'props': props
				})

			print rows
				