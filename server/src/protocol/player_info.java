package protocol;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;

import io.netty.channel.ChannelHandlerContext;

public class player_info extends message {

	public long player = 0;
	public String name = "";

	@Override
	public int id(){
		 return 24;
	}

	@Override
	public int length(){
		 return 12 +name.length();
	}

	@Override
	public void send(ChannelHandlerContext ctx){
		ByteBuf byteBuffer = Unpooled.buffer(8+length());
		byteBuffer.writeInt(id());
		byteBuffer.writeInt(length());
		byteBuffer.writeLong(player);
		write_string(byteBuffer, name);
		byteBuffer.writeByte(64);
		byteBuffer.writeByte(64);
		ctx.writeAndFlush( byteBuffer);
	}

	@Override
	public void parse_data(ByteBuf byteBuffer){
		player = byteBuffer.readLong();
		name = read_string(byteBuffer);
	}
}
