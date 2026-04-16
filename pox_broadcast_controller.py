from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet
from pox.lib.addresses import EthAddr
import time

log = core.getLogger()

mac_to_port = {}
broadcast_count = {}

BROADCAST_LIMIT = 10

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.connection.dpid

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][packet.src] = event.port

    # Broadcast detection
    if packet.dst == EthAddr("ff:ff:ff:ff:ff:ff"):
        
        
        now = time.time()

        if dpid not in broadcast_count:
            broadcast_count[dpid] = []

        broadcast_count[dpid].append(now)

        broadcast_count[dpid] = [
            t for t in broadcast_count[dpid]
            if now - t < 1
        ]

        if len(broadcast_count[dpid]) > BROADCAST_LIMIT:
            log.warning("Broadcast Storm Detected")

            msg = of.ofp_flow_mod()
            msg.priority = 10
            msg.match.dl_dst = EthAddr("ff:ff:ff:ff:ff:ff")

            event.connection.send(msg)
            return

        # selective forwarding
        for port in event.connection.ports:
            if port != event.port:
                msg = of.ofp_packet_out()
                msg.data = event.ofp
                msg.actions.append(of.ofp_action_output(port=port))
                event.connection.send(msg)

    else:
        # unicast forwarding
        if packet.dst in mac_to_port[dpid]:
            port = mac_to_port[dpid][packet.dst]

            msg = of.ofp_flow_mod()
            msg.match.dl_dst = packet.dst
            msg.actions.append(of.ofp_action_output(port=port))

            event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("POX Broadcast Controller Running")
