#  https://stepik.org/lesson/709885/step/1?unit=710450


class Data:
    def __init__(self, data: str, ip: str):
        self.data = data
        self.ip = ip


class Server:
    _ip_counter = 1

    def __init__(self):
        self.ip = Server._ip_counter
        Server._ip_counter += 1
        self.buffer = []
        self.router = None

    def send_data(self, data: Data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        received_data = self.buffer.copy()
        self.buffer.clear()
        return received_data

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server: Server):
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server: Server):
        serv_connect = self.servers.pop(server.ip, False)
        if serv_connect:
            serv_connect.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
