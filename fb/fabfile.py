from fabric.api import env,run

env.hosts = ['ubuntu@192.168.0.103','127.0.0.1']


def uptime():
	run('uptime')
