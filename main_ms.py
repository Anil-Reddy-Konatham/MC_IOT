from SerialModule import ConnectingSerialPort as Cs
# from iperf_client import start_client_iperf
from iperf_serv import start_server_iperf


class MsAutomation(Cs):
    def __init__(self):
        Cs.__init__(self)
        pass

    def control_test(self):
        Cs.serial_write('show ms phyconfig')
        Cs.threading.Thread(a.serial_read()).start()
        # start_client_iperf()
        start_server_iperf()


a = MsAutomation()
a.control_test()

#a.serial_write('show bs phyconfig')
#threading.Thread(a.serial_read()).start()
#start_client_iperf()