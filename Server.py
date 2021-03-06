from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer
import redis

__author__ = 'solomon'

success = "Success!"

def testf(t):
    return t * t


def create(key, val):
    if not r.exists(key):
        r.set(key, val)
        return success
    return "Fail! " + key + " : " + r.get(key)


def read(key):
    if r.exists(key):
        return key + " : " + r.get(key)
    return "Fail! Record with key \"" + key + "\" was not found!"


def update(key, val):
    if r.exists(key):
        r.set(key, val)
        return success
    return "Fail! Record with key \"" + key + "\" was not found!"


def delete(key):
    if r.exists(key):
        r.delete(key)
        return success
    return "Fail! Record with key \"" + key + "\" was not found!"


r = redis.StrictRedis(host='localhost', port=6379)

if __name__ == '__main__':
    dispatcher = SoapDispatcher(
        'di-di-dispatcher',
        location="http://localhost:8008/")

    dispatcher.register_function("testf", testf, returns={'MultResult': int}, args={'t': int})

    dispatcher.register_function("CreateRecord", create, returns={'Result': int}, args={"key": str, "val": str})
    dispatcher.register_function("ReadRecord", read, returns={'Result': int}, args={"key": str})
    dispatcher.register_function("UpdateRecord", update, returns={'Result': int}, args={"key": str, "val": str})
    dispatcher.register_function("DeleteRecord", delete, returns={'Result': int}, args={"key": str})

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SOAPHandler)
    httpd.dispatcher = dispatcher
    httpd.serve_forever()
