'''
Ethernet learning switch in Python.
Note that this file currently has the code to implement a "hub"
in it, not a learning switch.  (I.e., it's currently a switch
that doesn't learn.)
'''
from switchyard.lib.userlib import *

BROADCAST = EthrAddr('FF:FF:FF:FF:FF')

def main(net):
    my_interfaces = net.interfaces() 
    mymacs = [intf.ethaddr for intf in my_interfaces]
    #mymacs are addresses for this learning switch
    #need data structure (array? dictionary? class + object?) for addresses + ports for learning table
    #macsize = 5

    while True:
        try:
            timestamp,input_port,packet = net.recv_packet()
        except NoPackets:
            continue
        except Shutdown:
            return

        log_debug ("In {} received packet {} on {}".format(net.name, packet, input_port))
        if packet[0].dst in mymacs:
            log_debug ("Packet intended for me")
            #I presume we keep this

        #add else if to check if address is in the learning table, if so, send out on that port
        #elif packet[0].dst in array:
            #IDK where we send it yet. Check out send_packet function below.
        
        else:
            for intf in my_interfaces:
                if input_port != intf.name:
                    log_debug ("Flooding packet {} to {}".format(packet, intf.name))
                    net.send_packet(intf.name, packet)
        
        #now determine if the learning table needs to be updated
        #if the sending address is not already in the table
            #if array >= 5 (or dictionary size, etc)
                #pop first position
            #add new address
        #update port for address (whether we added or it was already in there)

    net.shutdown()

