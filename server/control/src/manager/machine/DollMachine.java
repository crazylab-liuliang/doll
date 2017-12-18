package manager.machine;

import java.util.concurrent.ConcurrentHashMap;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import io.netty.channel.ChannelHandlerContext;

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
		machines.clear();
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
	
	public static DollMachine getByName(String name) {
		if(machines.size()>0){
			ConcurrentHashMap.Entry<Integer, DollMachine> entry = machines.entrySet().iterator().next();
			return entry.getValue();
		}
		
		return null;
	}
	
	// ×óÒÆ×¦×Ó
	public void on_control(protocol.message msg) {
		msg.send(mChannelCtx);
	}
	
	public void on_controll(String type, String value) {
		protocol.machine_control msg = new protocol.machine_control();
		msg.type = Integer.parseInt(type);
		msg.op = Integer.parseInt(value);
		msg.send(mChannelCtx);
	}
}
