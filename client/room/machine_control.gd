extends Control

func _ready():
	pass

func _on_left_pressed():
	get_node("/root/network").send_machine_move_left()
