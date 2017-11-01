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
		machines.put(mChannelCtx.hashCode(), this);
		
		logger.info("doll machine login");
	}
	
	// test
	public static DollMachine getOne() {
		if(machines.size()>0){
			ConcurrentHashMap.Entry<Integer, DollMachine> entry = machines.entrySet().iterator().next();
			return entry.getValue();
		}
		
		return null;
	}
	
	// ����צ��
	public void move_left() {
		protocol.machine_move_left msg = new protocol.machine_move_left();
		msg.send(mChannelCtx);
		
		System.out.println("---move left, move left");
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
