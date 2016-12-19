


This is my python tornado template frame

if you config port or setting ,please write config

and Multiple projects,please mkdir to server,if you projects have html ,you must in project mkdir template

but static must frame "static", and alias "/static". example"/static/1.jpg"


-----------------------------------------------


run.py is Start the file.
1.`~tornado.tcpserver.TCPServer.listen`:simple single-process:


    server = HTTPServer(application)
    server.listen(8888)
    IOLoop.current().start()

2.`~tornado.tcpserver.TCPServer.bind`/`~tornado.tcpserver.TCPServer.start`:
    simple multi-process:

    server = HTTPServer(application)
    server.bind(8888)
    server.start(0) #Forks multiple sub-process
    IOLoop.current().start()

    when using this interface , an `.IOLoop` must *not* be passed to the `HTTPServer ` constructor.
    `~.TCPServer.start` will always start the server on the default singleton `.IOLoop`.

3. `~tornado.tcpserver.TCPServer.add_sockets`: advanced multi-process:

    sockets = tornado.netutil.bind_sockets(8888)
    tornado.process.fork_processes(5)
    server = HTTPServer(application)
    server.add_sockets(sockets)
    tornado.ioloop.IOLoop.instance().start()

stop :[root@host-10-10-0-4 ~]# lsof -i:8888 |awk '{print $2}' | xargs kill -9

```china
其实无论是多线程还是多进程，根据你的需求来决定的，看你的cpu处理的队列速度。还有其他硬件资源来算的
你知道cpu同一时间只能干一件事情，也就是一个进程的一个线程跑，各种上下文切换，中断

cpu 是靠时间片工作的，cpu是时间维度，内存是空间维度
cpu 的滴答，滴答的时候所有进程都会抢占cpu使用权
而内核就像一个监控的资源分配者，哪个进程优先要使用cpu哪个就先挂起
内核是维护这个结构表的
tor里面进程的nice☞即使进程的优先级，系统自己是1-99，而99-149谁的越低cpu切换的时候i就先搞谁
而多进程，频繁切换上下文也会浪费cpu资源。
```


----------------------------------------------------

里面封装了日志模块，但是需要注意的是，需要根据网络问题进行使用。否则影响代码效率

