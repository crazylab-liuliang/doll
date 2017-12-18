package protocol;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;

import io.netty.channel.ChannelHandlerContext;

public class machine_control extends message {

	public int type = 0;
	public int op = 0;

	@Override
	public int id(){
		 return 19;
	}

	@Override
	public int length(){
		 return 8 ;
	}

	@Override
	public void send(ChannelHandlerContext ctx){
		ByteBuf byteBuffer = Unpooled.buffer(8+length());
		byteBuffer.writeInt(id());
		byteBuffer.writeInt(length());
		byteBuffer.writeInt(type);
		byteBuffer.writeInt(op);
		byteBuffer.writeByte(64);
		byteBuffer.writeByte(64);
		ctx.writeAndFlush( byteBuffer);
	}

	@Override
	public void parse_data(ByteBuf byteBuffer){
		type = byteBuffer.readInt();
		op = byteBuffer.readInt();
	}
}
