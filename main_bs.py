from SerialModule import ConnectingSerialPort as Cs
# from iperf_serv import start_server_iperf
from iperf_client import start_client_iperf

class BsAutomation(Cs):
    def __init__(self):
        Cs.__init__(self)
        pass

    def control_test(self):
        Cs.serial_write('show bs phyconfig')
        Cs.threading.Thread(a.serial_read()).start()
        # start_server_iperf()
        start_client_iperf()


a = BsAutomation()
a.control_test()

#a.serial_write('show bs phyconfig')
#threading.Thread(a.serial_read()).start()
#start_server_iperf()
