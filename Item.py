from itemAssetsList import itemAssetsList

class Item:
	def __init__(self, name="Grass Block", nb=1):
		self.name = name

		self.nb = nb

		if name in itemAssetsList:
			self.icon = itemAssetsList[name]
		else:
			raise FileNotFoundError("Icon not found with the name given")

	def list():
		list = []
		for item in itemAssetsList:
			list.append(Item(item))
		return list

	def nameList():
		return [*itemAssetsList]