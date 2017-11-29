package protocol;

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;

import io.netty.channel.ChannelHandlerContext;

public class battle_player_shoot_result extends message {

	public int player1_blood = 0;
	public int player0_blood = 0;

	@Override
	public int id(){
		 return 9;
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
		byteBuffer.writeInt(player1_blood);
		byteBuffer.writeInt(player0_blood);
		byteBuffer.writeByte(64);
		byteBuffer.writeByte(64);
		ctx.writeAndFlush( byteBuffer);
	}

	@Override
	public void parse_data(ByteBuf byteBuffer){
		player1_blood = byteBuffer.readInt();
		player0_blood = byteBuffer.readInt();
	}
}
