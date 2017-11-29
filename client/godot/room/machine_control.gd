extends Control

var is_mirror = true
var button_idxs = []

func _ready():
	if is_mirror:
		button_idxs = [2,1,4,3]
	else:
		button_idxs = [1,2,3,4]

func _on_forward_button_down():
	get_node("/root/network").send_machine_control(button_idxs[0],1)

func _on_forward_button_up():
	get_node("/root/network").send_machine_control(button_idxs[0],0)

func _on_back_button_down():
	get_node("/root/network").send_machine_control(button_idxs[1],1)

func _on_back_button_up():
	get_node("/root/network").send_machine_control(button_idxs[1],0)

func _on_left_button_down():
	get_node("/root/network").send_machine_control(button_idxs[2],1)

func _on_left_button_up():
	get_node("/root/network").send_machine_control(button_idxs[2],0)

func _on_right_button_down():
	get_node("/root/network").send_machine_control(button_idxs[3],1)

func _on_right_button_up():
	get_node("/root/network").send_machine_control(button_idxs[3],0)

func _on_start_pressed():
	get_node("/root/network").send_machine_control(0,0)

func _on_take_pressed():
	get_node("/root/network").send_machine_control(5,0)
