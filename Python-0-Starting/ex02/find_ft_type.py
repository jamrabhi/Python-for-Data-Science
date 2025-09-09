def all_thing_is_obj(object: any) -> int:
	if isinstance(object, (list, tuple, set, dict)):
		print(f"{object} {type(object)}")
	elif isinstance(object, str):
		print(f"{object} is in the kitchen : {type(object)}")
	else:
		print("Type not found")
		return 42