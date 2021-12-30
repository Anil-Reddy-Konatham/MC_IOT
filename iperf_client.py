import subprocess
from time import ctime
import re


def start_client_iperf():

    process = subprocess.Popen('iperf -c 10.1.206.83 -i 1 -u -b 200K -t 300 -p 7001', shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

    while 1:
        nextline = (process.stdout.readline().decode()).strip()
        str1 = "{} {} : Client".format(ctime()[4:-5].replace('  ', '_'), nextline)
        print (str1)
        #print(nextline)

        try:
            req_str = re.search("](.*) sec", nextline)
            result = eval(req_str.group(1).strip())
            if result > 1 or result < -1:  # "1" Has to be changed according to interval value
               # with open(ctime()[4:-5].replace('  ', '_') + "Client logs.csv", "a+") as f:
                #    f.write("Date & time     [ ID]   Interval       Transfer     Bandwidth      Jitter   Lost/Total Datagrams" + '\r\n')
                 #   f.write(str1 + '\r\n')
                break
        except:
            pass


start_client_iperf()
