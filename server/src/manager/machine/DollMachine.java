package manager.machine;

import java.util.concurrent.ConcurrentHashMap;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import io.netty.channel.ChannelHandlerContext;
import manager.player.Player;

// »úÆ÷
public class DollMachine {
	private static final Logger logger = LogManager.getLogger("doll machine");
	public static ConcurrentHashMap<Integer, DollMachine>   machines = new ConcurrentHashMap<Integer, DollMachine>();
	public ChannelHandlerContext 		   					mChannelCtx = null;
	private String											name;			// Ãû³Æ
		
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
	
	// Ê¹ÓÃÓÊÏäÃÜÂëµÇÂ¼
	public void login() {
		logger.info("doll machine login");
		
		move_left();
	}
	
	// ×óÒÆ×¦×Ó
	public void move_left() {
		protocol.machine_move_left msg = new protocol.machine_move_left();
		mChannelCtx.write(msg.data());
	}
	
	// ×óÒÆ×¦×Ó
	public void move_right() {
		
	}
	
	// ×óÒÆ×¦×Ó
	public void move_forward() {
		
	}
	
	// ×óÒÆ×¦×Ó
	public void move_back() {
		
	}
	
	public void catch_doll(){
		
	}
}
