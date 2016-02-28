import orm,asyncio
from models import User,Blog,Comment

def test(loop):
    yield from orm.create_pool(loop = loop,user='www-data',password='password',db='awesome')
    u=User(name='test5',email='test5@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()
