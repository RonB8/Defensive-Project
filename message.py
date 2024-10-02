class Request:
    def __init__(self, packet):
        self.client_ID = packet[:16].decode()
        self.version = int.from_bytes(packet[16:17], byteorder='big')
        self.code = int.from_bytes(packet[17:19], byteorder='big')
        self.payload_size = int.from_bytes(packet[19:23], byteorder='big')
        self.payload = packet[23:].decode()


class Response:
    packet = []

    def __init__(self, version, code, payload_size, payload):
        self.packet.append(version)

        self.packet.append(code >> 8)
        self.packet.append(code & 0xFF)

        self.packet.append((payload_size >> 24) & 0xFF)
        self.packet.append((payload_size >> 16) & 0xFF)
        self.packet.append((payload_size >> 8) & 0xFF)
        self.packet.append(payload_size & 0xFF)

        self.packet += payload

        self.packet = bytearray(self.packet)


class Payload:
    def __init__(self, payload, code):
        self.__payload = payload
        self.__code = code

    def name(self):
        return self.__payload[:255].decode()

    def public_key(self):
        return self.__payload[255: 415].decode()

    def content_size(self):
        # if self.__code == VALID_FILE_ACCEPTED:
        #     return self.__payload[16: 20].decode()

        return self.__payload[:4].decode()

    def orig_file_size(self):
        return self.__payload[4: 8].decode()

    def packet_number(self):
        return self.__payload[8: 10].decode()

    def total_packet(self):
        return self.__payload[10: 12].decode()

    def file_name(self):
        if self.__code == SEND_FILE:
            return self.__payload[12: 267].decode()

        # if self.__code == VALID_FILE_ACCEPTED:
        #     return self.__payload[20: 275].decode()

        return self.__payload[: 255].decode()

    def message_content(self):
        return self.__payload[267:].decode()







REGISTRY = 825
SEND_PUBLIC_KEY = 826
LOGIN = 827
SEND_FILE = 828
VALID_CRC = 900
INVALID_CRC = 901
INVALID_CRC_FINITE = 902

SUCCESSFUL_REGISTRATION = 1600
FAILED_REGISTRATION = 1601
PUBLIC_KEY_RECEIVED = 1602
VALID_FILE_ACCEPTED = 1603
MESSAGE_RECEIVED = 1604
LOGIN_ACCEPT = 1605
LOGIN_REJECT = 1606
GENERIC_ERROR = 1607


