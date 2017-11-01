extends Control

func _on_play_pressed():
	get_node("/root/global").set_scene("res://room/room.tscn")