extends Node2D

func _ready():
	set_process(true)
	
func _process(delta):
	if !has_node("/root/global"):
		var global = load("res://global/global.gd").new()
		global.set_name("global")
		get_tree().get_root().add_child(global)
	
func show( type):
	if type=="ranking":
		pass
	elif type=="main":
		pass

