from pysimplesoap.client import SoapClient

__author__ = 'solomon'

client = SoapClient(
    location="http://localhost:8000/")


class ClassProduction:
    def __init__(self):
        pass

    def testf(self, t):
        return client.testf(t=t)

    @staticmethod
    def create(key, val):
        return client.CreateRecord(key=key, val=val)

    def read(self, key):
        return client.ReadRecord(key=key)

    def update(self, key, val):
        return client.UpdateRecord(key=key, val=val)

    def delete(self, key):
        return client.DeleteRecord(key=key)

    def show_commands(self):
        print "Input number of command to execute"
        print "1. Create"
        print "2. Read"
        print "3. Update"
        print "4. Delete"
        print "5. Exit"
        print

    def _key(self):
        return [raw_input('Key: ')]

    def _key_and_val(self):
        key = self._key()
        key.append(raw_input('Value: '))
        return key

    def test_connection(self):
        result = self.testf(5).MultResult
        return int(result)

    def start_dialog(self):
        while True:
            print
            self.show_commands()
            response = "No response"

            try:
                operation = int(raw_input("Number: "))
            except ValueError:
                print("Invalid number")
                continue

            if 1 == operation or 3 == operation:
                inp = self._key_and_val()

                if 1 == operation:
                    response = self.create(inp[0], inp[1])
                if 3 == operation:
                    response = self.update(inp[0], inp[1])

            elif 2 == operation or 4 == operation:
                inp = self._key()

                if 2 == operation:
                    response = self.read(inp[0])
                if 4 == operation:
                    response = self.delete(inp[0])

            elif 5 == operation:
                break

            else:
                print "Invalid number"
                continue

            print response.Result

if __name__ == '__main__':
    clientClass = ClassProduction()
    clientClass.start_dialog()
