import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()

from os import environ as env

bind = '{}:{}'.format(env.get('HOST','0.0.0.0'),env.get('PORT',5000))
