package protocol;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;

import io.netty.channel.ChannelHandlerContext;

public class login_by_osid extends message {

	public String osid = "";

	@Override
	public int id(){
		 return 17;
	}

	@Override
	public int length(){
		 return 4 +osid.length();
	}

	@Override
	public void send(ChannelHandlerContext ctx){
		ByteBuf byteBuffer = Unpooled.buffer(8+length());
		byteBuffer.writeInt(id());
		byteBuffer.writeInt(length());
		write_string(byteBuffer, osid);
		byteBuffer.writeByte(64);
		byteBuffer.writeByte(64);
		ctx.writeAndFlush( byteBuffer);
	}

	@Override
	public void parse_data(ByteBuf byteBuffer){
		osid = read_string(byteBuffer);
	}
}
