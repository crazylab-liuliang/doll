extends Control

func _on_play_pressed():
	get_node("/root/sound").play_sound("button_press")
	get_node("/root/global").set_scene("res://game_single/game_single.tscn")

func _on_vs_pressed():
	get_node("/root/global").set_scene("res://game_single_vs/game_single_vs.tscn")