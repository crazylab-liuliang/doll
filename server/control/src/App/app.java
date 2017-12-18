package App;

import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import net.socket.SocketServer;
import quartz.JobMgr;

import org.apache.logging.log4j.Logger;
import net.http.HttpServer;
import org.apache.logging.log4j.LogManager;

public class app {
	// ����һ����̬��־����
	private static final Logger logger = LogManager.getLogger("doll");
	private static ExecutorService updateService = null;
	private static long	 				currentTime = 0;
	private static long	 				lastTime = 0;
	private static long					saveToDBTime = 0;
	private static boolean			isUpdate = true;
	
	public static void main(String[] args){
		logger.info("--------------");
		logger.info("|Start server|");
		logger.info("--------------");
		
		// ������ֹ����
		KillHandler killHandler = new KillHandler();
		killHandler.registerSignal("TERM");
		
		// �½��̳߳�
		int nThreads = Math.max( 1, Runtime.getRuntime().availableProcessors()-1);
		updateService = Executors.newFixedThreadPool(nThreads);	
		
		// ������ʱ����
		JobMgr.getInstance().startJobs();
		
		// ��������
		SocketServer server = SocketServer.getInstance();
		server.start();
		
		// http ����
		HttpServer httpServer = HttpServer.getInstance();
		httpServer.start();
		
		// ��ѭ��
		lastTime =  System.currentTimeMillis();
		while(true){
				currentTime = System.currentTimeMillis();
				long delta = currentTime - lastTime;
				lastTime = currentTime;
				
				if (isUpdate) {
					mainLoop( delta);
				}
		}
	}
	
	public static Logger logger() {
		return logger;
	}
	
	public static void stopUpdate(){
		isUpdate = false;
	}
	
	public static void waitExecutatServiceTerminated() {
		updateService.shutdown();
		
		while(!updateService.isTerminated()) {
			try {
				Thread.sleep(100);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void sleep(long delta) {
		// ��Ϣ
		if(delta < 100) {
			try {
				Thread.sleep(100-delta);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void mainLoop(long delta)
	{					
			// �����������
					
			// ��Ϣ
			sleep(delta);
	}
}
