from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.dpid

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][packet.src] = event.port

    if packet.dst.is_multicast:
        log.info("Broadcast packet detected - controlling broadcast")
        return

    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]

        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.actions.append(of.ofp_action_output(port=out_port))
        msg.data = event.ofp
        event.connection.send(msg)

    else:
        msg = of.ofp_packet_out()
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        msg.data = event.ofp
        event.connection.send(msg)

def launch():
    def start_switch(event):
        log.info("Broadcast Control Controller Running...")
        event.connection.addListeners(_handle_PacketIn)

    core.openflow.addListenerByName("ConnectionUp", start_switch)