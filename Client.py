from pysimplesoap.client import SoapClient

__author__ = 'solomon'

client = SoapClient(
    location="http://localhost:8000/")


def testf(t):
    return client.testf(t=t)


def create(key, val):
    return client.CreateRecord(key=key, val=val)


def read(key):
    return client.ReadRecord(key=key)


def update(key, val):
    return client.UpdateRecord(key=key, val=val)


def delete(key):
    return client.DeleteRecord(key=key)


def show_commands():
    print "Input number of command to execute"
    print "1. Create"
    print "2. Read"
    print "3. Update"
    print "4. Delete"
    print "5. Exit"
    print


def _key():
    return [raw_input('Key: ')]


def _key_and_val():
    key = _key()
    key.append(raw_input('Value: '))
    return key


result = testf(5).MultResult
print int(result)

while True:
    print
    show_commands()
    response = "No response"

    try:
        operation = int(raw_input("Number: "))
    except ValueError:
        print("Invalid number")
        continue

    if 1 == operation or 3 == operation:
        inp = _key_and_val()

        if 1 == operation:
            response = create(inp[0], inp[1])
        if 3 == operation:
            response = update(inp[0], inp[1])

    elif 2 == operation or 4 == operation:
        inp = _key()

        if 2 == operation:
            response = read(inp[0])
        if 4 == operation:
            response = delete(inp[0])

    elif 5 == operation:
        break

    else:
        print "Invalid number"
        continue

    print response.Result
