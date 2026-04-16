from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel


class CustomTopo(Topo):

    def build(self):

        # Create Switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        # Create Hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        # Connect Hosts to Switch 1
        self.addLink(h1, s1)
        self.addLink(h2, s1)

        # Connect Hosts to Switch 2
        self.addLink(h3, s2)
        self.addLink(h4, s2)

        # Connect Switches
        self.addLink(s1, s2)


def run():

    topo = CustomTopo()

    net = Mininet(
        topo=topo,
        controller=RemoteController,
        link=TCLink
    )

    net.start()

    print("Network Started")
    print("Testing connectivity")
    net.pingAll()

    CLI(net)

    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    run()
