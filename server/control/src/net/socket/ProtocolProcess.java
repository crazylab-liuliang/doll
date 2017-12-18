package net.socket;

import io.netty.channel.ChannelHandlerContext;
import manager.machine.DollMachine;

interface ProtocolProcess {
	public void on_accept(protocol.message proto, ChannelHandlerContext ctx);
	
	public static void bind() {
		SocketServerHandler.bind(new protocol.machine_control(), new machine_control_cmd_process());	
		SocketServerHandler.bind(new protocol.machine_login(), new machine_login_process());
	}
}


class machine_control_cmd_process implements ProtocolProcess{
	@Override
	public void on_accept(protocol.message proto, ChannelHandlerContext ctx) {		
		
		//Player player = Player.get(ctx);
		//player.machine_control(proto);
	}
}


class machine_login_process implements ProtocolProcess{
	@Override
	public void on_accept(protocol.message proto, ChannelHandlerContext ctx) {
		protocol.machine_login msg = (protocol.machine_login)proto;
		
		DollMachine machine = DollMachine.get(ctx);
		machine.login();
	}
}