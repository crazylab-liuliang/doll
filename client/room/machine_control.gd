extends Control

func _ready():
	pass

func _on_forward_button_down():
	get_node("/root/network").send_machine_control(1,1)

func _on_forward_button_up():
	get_node("/root/network").send_machine_control(1,0)

func _on_back_button_down():
	get_node("/root/network").send_machine_control(2,1)

func _on_back_button_up():
	get_node("/root/network").send_machine_control(2,0)

func _on_left_button_down():
	get_node("/root/network").send_machine_control(3,1)

func _on_left_button_up():
	get_node("/root/network").send_machine_control(3,0)

func _on_right_button_down():
	get_node("/root/network").send_machine_control(4,1)

func _on_right_button_up():
	get_node("/root/network").send_machine_control(4,0)

func _on_start_pressed():
	get_node("/root/network").send_machine_control(0,0)

func _on_take_pressed():
	get_node("/root/network").send_machine_control(5,0)
