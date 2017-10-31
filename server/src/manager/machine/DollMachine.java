package manager.machine;

import java.util.concurrent.ConcurrentHashMap;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import io.netty.channel.ChannelHandlerContext;
import manager.player.Player;

// ����
public class DollMachine {
	private static final Logger logger = LogManager.getLogger("doll machine");
	public static ConcurrentHashMap<Integer, DollMachine>   machines = new ConcurrentHashMap<Integer, DollMachine>();
	public ChannelHandlerContext 		   					mChannelCtx = null;
	private String											name;			// ����
		
	public DollMachine(ChannelHandlerContext channelCtx) {	
		mChannelCtx = channelCtx;
	}
	
	public static DollMachine get(ChannelHandlerContext ctx) {
		int ctxID = ctx.hashCode();
		if( machines.containsKey(ctxID)) {
			return machines.get(ctxID);
		}
		else {
			DollMachine machine = new DollMachine(ctx);		
			
			return machine;
		}		
	}
	
	// ʹ�����������¼
	public void login() {
		logger.info("doll machine login");
		
		move_left();
	}
	
	// ����צ��
	public void move_left() {
		protocol.machine_move_left msg = new protocol.machine_move_left();
		mChannelCtx.write(msg.data());
	}
	
	// ����צ��
	public void move_right() {
		
	}
	
	// ����צ��
	public void move_forward() {
		
	}
	
	// ����צ��
	public void move_back() {
		
	}
	
	public void catch_doll(){
		
	}
}
