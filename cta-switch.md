# Switch [cta-switch.md]

Network device that forwards traffic based on data link address. Uses special
circuits for direct hardware acceleration to gain high throughput.

Additional routing functionality can be enabled if it is a multilayer switch.
Other features, such as Power over Ethernet (PoE), are also available in
particular switches.

Switches also come in low config variants, called "unmanaged switches". These
are generally plug and play, and have fixed and few configuration options. This
renders it impossible to install features like VLANs to an unmanaged switch.
Additionally, unmanaged switches commonly lack management protocol capabilities,
such as SNMP. The idea is to act as a cheap, easy, and dirty way to connect many
systems together.

Unlike unmanaged switches, managed switches have the ability to monitor traffic
and support VLAN to set certain interfaces to different IP subnets. These
switches have many other invaluable features like traffic prioritization,
redundancy, spanning tree protocol (STP), port mirroring for packet analysis,
and traffic monitoring via external management services, such as SNMP. Managed
switches are generally meant for large businesses, where there are far more
connected systems and a greater need for speed.

---

## Akin
[Router](cta-router.md)
