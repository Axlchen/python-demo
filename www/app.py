#!/usr/bin/pyhon3
# -*- coding:utf-8 -*-

__author__ = 'axlchen'

import logging
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b'<h1>Axlchen</h1>')

@asyncio.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('serverstarted at http://127.0.0.1:9000...')
    return srv

# loop=asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

@asyncio.coroutine
def create_pool(pool,**kw):
    logging.info('create database connection pool')
    global __pool
    __pool=yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port','3306'),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )

@asyncio.coroutine
def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cur=yield from conn.cursor(aiomysql.DictCursor)


























