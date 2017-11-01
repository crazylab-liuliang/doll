extends Control

func _ready():
	pass

func _on_forward_pressed():
	get_node("/root/network").send_machine_control(1)

func _on_back_pressed():
	get_node("/root/network").send_machine_control(2)
	
func _on_left_pressed():
	get_node("/root/network").send_machine_control(3)

func _on_right_pressed():
	get_node("/root/network").send_machine_control(4)
