import subprocess
from time import ctime
import re
import datetime
def start_server_iperf():

    process = subprocess.Popen('iperf -s -i 1 -u -p 7001', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while 1:
        nextline = (process.stdout.readline().decode()).strip()
        str1 = "{} {} : Server".format(ctime()[4:-5].replace('  ', '_'), nextline)
        str_ip_d = str1.split()
        #print(nextline)
        print (str1)

        try:
            req_str = re.search("](.*) sec", nextline)
            result = eval(req_str.group(1).strip())
            if result > 1 or result < -1:
                with open("DL logs.csv", "a+") as f:
                    header_string = "{},{},{},{}".format("Date&Time", "Interval", "Bandwidth", "Lost/Total Datagrams")
                    result_string = "{},{},{},{}".format(ctime()[4:-5].replace('  ', '_'), nextline[7:21], nextline[35:50], nextline[61:])
                    # f.write("Date & time     [ ID]   Interval       Transfer     Bandwidth      Jitter   Lost/Total Datagrams" + '\r\n')
                    if header_string not in open("DL logs.csv").read():
                        f.write(header_string + '\r\n')
                    f.write(result_string + '\r\n')
                    # f.write(str1 + '\r\n')
                    break
        except:
            pass


# [0:1], [2][5:6][9:10][14:16]
# Dec 20 04:27:18 [  3]  0.0-106.6 sec  1.88 MBytes   148 Kbits/sec  116.916 ms 2915/ 4257 (68%) : Server
# Dec 20 04:45:34 [  3] 118.0-120.0 sec  37.3 KBytes   153 Kbits/sec  144.467 ms  145/  171 (85%) : Server
# Dec 20 04:45:36 [  3]  0.0-122.0 sec  2.15 MBytes   148 Kbits/sec  152.937 ms 6025/ 7561 (80%) : Server
# Dec 20 04:59:50 [  3]  0.0-174.8 sec  3.09 MBytes   148 Kbits/sec  94.331 ms 9965/12168 (82%) : Server
# [  3]  0.0-82.2 sec  1.45 MBytes   148 Kbits/sec  142.674 ms 3165/ 4201 (75%)
start_server_iperf()
