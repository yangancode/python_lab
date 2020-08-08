# coding: utf-8
# @date: 2019-12-01

"""
创建多进程的四种方式
"""


# 第一种方式
# 只在Unix系统中有效，Windows系统中无效
# fork函数调用一次，返回两次：在父进程中返回值为子进程id，在子进程中返回值为0
def create_process_by_fork():
    import os
    pid = os.fork()

    if pid == 0:
        print('执行子进程，父进程id: {0}，子进程id: {1}'.format(os.getpid(), os.getppid()))
    else:
        print('执行父进程，父进程id: {0}，子进程id: {1}'.format(pid, os.getpid()))


def worker():
    import os, time
    time.sleep(2)
    print('子进程开始执行，父进程id: {0}，子进程id: {1}'.format(os.getppid(), os.getpid()))


# 第二种方式
def create_process_by_process():
    from multiprocessing import Process
    print('主进程开始执行')
    processes = []
    for i in range(2):
        p = Process(target=worker, name='worker' + str(i), args=())
        processes.append(p)

    # 开启进程
    for i in range(2):
        processes[i].start()

    # 阻塞进程，等待进程执行完毕
    for i in range(2):
        processes[i].join(timeout=0.1)

    # 关闭进程
    for i in range(2):
        processes[i].terminate()

    print('end')


# 第三种方式
from multiprocessing import Process


class MyProcess(Process):
    # 继承Process类的方法
    def __init__(self):
        Process.__init__(self)

    # 重写run方法
    def run(self) -> None:
        import os, time
        time.sleep(2)
        print('子进程开始执行，父进程id: {0}，子进程id: {1}'.format(os.getppid(), os.getpid()))


def create_process_by_custom():
    print('主进程开始...')
    my_process = MyProcess()
    my_process.start()
    my_process.join()
    print('主进程结束...')


# 第四种
def task(task_id):
    import os, time
    time.sleep(2)
    print('子进程开始执行，父进程id: {0}，子进程id: {1}，任务id：{2}'.format(os.getppid(), os.getpid(), task_id))
    return os.getpid()


def create_process_by_pool():
    from multiprocessing import Pool
    print('主进程开始...')
    pool = Pool(3)  # 开启3个进程
    for i in range(9):
        # 同步方式
        # pool.apply(task, args=(i,))
        # 异步方式
        pool.apply_async(task, args=(i, ))

    # 继续补充新的进程
    for i in range(10, 13):
        pool.apply_async(task, args=(i, ))
    pool.close()
    pool.join()
    pool.terminate()
    print('主进程结束...')


# RUN = 0
# CLOSE = 1
# TERMINATE = 2


# class Pool(object):
#     def __init__(self, processes=None,):
#         if processes is None:
#             processes = os.cpu_count() or 1
#         if processes < 1:
#             raise ValueError("Number of processes must be at least 1")
#         self._processes = processes
#
#         # 初始化三个处理器
#         self._worker_handler = threading.Thread()
#         self._task_handler = threading.Thread()
#         self._result_handler = threading.Thread()
#
#         # 关闭进程池资源的方法
#         self._terminate = util.Finalize(self, self._terminate_pool, args=(xxx, ))
#
#     # apply 本质调用了 apply_async
#     def apply(self, func, args=(), kwds={}):
#         '''
#         Equivalent of `func(*args, **kwds)`.
#         Pool must be running.
#         '''
#         return self.apply_async(func, args, kwds).get()
#
#     # apply_async 其实就是将任务添加进队列中
#     def apply_async(self, func, args=(), kwds={}, callback=None,
#             error_callback=None):
#         '''
#         Asynchronous version of `apply()` method.
#         '''
#         if self._state != RUN:
#             raise ValueError("Pool not running")
#         result = ApplyResult(self._cache, callback, error_callback)
#         self._taskqueue.put(([(result._job, 0, func, args, kwds)], None))
#         return result
#
#     # 判断进程池的状态是否正在运行，如果是就关闭，如果处于关闭状态就不能继续添加任务了
#     def close(self):
#         util.debug('closing pool')
#         if self._state == RUN:
#             self._state = CLOSE
#             self._worker_handler._state = CLOSE
#
#     # 修改状态，关闭资源
#     def terminate(self):
#         util.debug('terminating pool')
#         self._state = TERMINATE
#         self._worker_handler._state = TERMINATE
#         self._terminate()
#
#     # 注意这里状态的判断，调用join前状态必须处于 CLOSE 或 TERMINATE
#     def join(self):
#         util.debug('joining pool')
#         if self._state == RUN:
#             raise ValueError("Pool is still running")
#         elif self._state not in (CLOSE, TERMINATE):
#             raise ValueError("In unknown state")
#         self._worker_handler.join()
#         self._task_handler.join()
#         self._result_handler.join()
#         for p in self._pool:
#             p.join()


# 第五种
from concurrent.futures import ProcessPoolExecutor


def create_process_by_future():
    # 不填则默认为cpu的个数
    p = ProcessPoolExecutor(3)
    task_list = []

    for i in range(9):
        # submit()方法返回的是一个future实例，要得到结果需要用obj.result()
        obj = p.submit(task, i)
        task_list.append(obj)
        # 判定某个任务是否完成
        print(obj.done())

    # 相当于 multiprocessing 的 close + join
    p.shutdown()
    # 打印结果
    print([obj.result() for obj in task_list])


if __name__ == '__main__':
    import time
    start = time.time()
    # create_process_by_fork()
    # create_process_by_process()
    # create_process_by_custom()
    # create_process_by_pool()
    create_process_by_future()
    print('cost', time.time() - start)


