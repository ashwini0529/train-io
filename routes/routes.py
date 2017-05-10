
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/log/data",
			dataController.logData
		),
		(
			r"/logs/show",
			dataController.showData
		)
]
					