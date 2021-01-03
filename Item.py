from itemAssetsList import itemAssetsList

class Item:
	""" A class to represant an item

	Attributes
	----------
	name : str = "Grass Block"
		The name of the item
	nb : int = 1
		The number of items
	icon : str
		The icon of the item

	Methods
	-------
	__init__(self, name="Grass Block", nb=1)
		Constructs all the necessary attributes for the Item object

		Parameters
		----------
		name : str = "Grass Block"
			Define the attribute name
		nb : int = 1
			Define the attribute nb

	list()
		Return the list of the items

		Returns
     	-------
		list of items : list

	nameList()
		Return the list of the item names

		Returns
     	-------
		list of item names : list
	 """

	def __init__(self, name="Grass Block", nb=1):
		self.name = name

		self.nb = nb

		if name in itemAssetsList:
			self.icon = itemAssetsList[name]
		else:
			raise FileNotFoundError("Icon not found with the name given")

	def list():
		""" Return the list of the items """
		list = []
		for item in itemAssetsList:
			list.append(Item(item))
		return list

	def nameList():
		return [*itemAssetsList]