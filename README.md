Towards a framework for Network-based Malware detection
=
December 2014



Authors
===========
- Abimael Carrasquillo Ayala 
| `abimael.carrasquillo@upr.edu`
| Computer Science DepartmentUniversity of Puerto Rico - Río Piedras
- Advisor: José Ortiz-Ubarri
  | `cheo@hpcf.upr.edu`
  | Computer Science Department
  | University of Puerto Rico - Río Piedras


Abstract
===========
Malware on mobiles devices, has been the major threat on mobile devices.
Android operating system has been the most vulnerable and attacked in
comparison with the other mobile plataforms. On this work we present a a
Network-based Malware Detection System to provide situational awareness
of mobile devices connected through a VPN network.

Description
===========

Mobile devices play an important role in todays life and also does
malware protection. Since the major threat on Android operating system
is malware and adware infection via Android markets @TI11 and
Alternative markets @YZ12, there is a need to develop better
next-generation anti-mobile-malware solutions @YZ12. There are two
aproaches to mobile malware detection:

-   **Host-based malware detection**: The host-based uses the limited
    resources of the mobile devices and is prone to drain the battery
    power of the mobile devices.

-   **Network-based malware detection**: The network-based malware
    detection delegates the analysis of the network behavior to a
    back-end server to detect malware based on the traffic generated by
    the mobile device, but is unable to detect malware that does not
    generate network traffic @AS11.

The framework proposed here follows the Network-based model, combining
network flows analysis and signature-based traffic analysis of a virtual
private network (VPN). Similar to the approach proposed by Parrizas et
al. in @AP13 we utilize Snort @Snort. For the network flows analysis,
the framework uses NetFlow, a network protocol developed by Cisco
@Netflow for traffic monitoring. One NetFlow is a record representing an
unidirectional sequence of packets that contains information on the
source Internet Protocol address (IP), the destination IP, the source
port, destination port, the sum of the payload size of the packets, a
timestamp, among others. A NetFlow generator will run on the VPN server
to collect aggregated information of the network traffic. The collected
data will be analyzed to detect network anomalous behavior, per mobile
device, and will be represented in charts for situational awareness and
visualization analytics.

Methodology
===========

To create the framework we need to follow the next methodology:

1.  Configure mobile devices to connect to the VPN.

2.  Install and configure Snort IDS to monitor the VPN server virtual
    interface with signatures for malware detection.

3.  Install and configure a NetFlow generator (flow probe) to generate
    NetFlow data of the VPN.

4.  Collect the NetFlow data for analysis.

5.  Analyze the NetFlow data and the IDS alerts per mobile device.

6.  Generate charts per mobile devices for situational awareness and
    visualization analytics.

7.  Implement the framework interface to provide the users with their
    mobile device alarms and charts.

This Fall 2014 we added the capacity to push notifications in the mobile
devices, such that the user is alerted with the alarms generated by the
framework, instead of relying on the user to access the framework
interface to check for the alarms.

Future Work
===========

We would compare the performance of the system in relation to the other
Host Based and Network Based products used to detect malware. We will
Finally we will study different algorithms for anomalous network traffic
analysis and study its performance.

Conclusion
==========

In the current stage of the work we have implemented the signature-based
part of the framework with its user interface. We are also generating
NetFlow traffic charts for each mobile device registered in the VPN and
presenting them in the user interface. The framework provides instant
push-notifications about the alarms generated by the user mobile device.

Acknowledgement
===============

I have taken efforts in this project. However, it would not have been
possible without the kind support and help of many individuals. I would
like to extend my sincere thanks to all of them. I would also like to
acknowledge with much appreciation to Albert E. Maldonado and Eric
Santos, ex-student and student from the UPR-R who have helped on
developing the project and people who have willingly helped me out with
their abilities. Also, this work is supported by the scholarship
Academics and Training for the Advancement of Cybersecurity Knowledge in
Puerto Rico (ATACK-PR) suported by the National Science Foundation under
Grant No. DUE-1438838.

<span>1</span>

T. Isohara, K. Takemori, and Ayumu Kubota, “Kernel-based Behavior
Analysis for Android Malware Detection”, In Proceedings of the 2011
Seventh International Conference on Computational Intelligence and
Security(CIS ’11), IEEE Computer Society, Washington, DC, USA,
1011-1015,DOI=10.1109/CIS.2011.226
<http://dx.doi.org/10.1109/CIS.2011.226>

Yajin Zhou, Xu xian Jiang.“Dissecting Android Malware: Characterization
and Evolution”. Proceedings of the 33rd IEEE Symposium on Security and
Privacy (Oakland 2012). San Francisco, CA, May 2012.
<http://www.csc.ncsu.edu/faculty/jiang/pubs/OAKLAND12.pdf>

A. Shabtai, U. Kanonov, Y. Elovici, C. Glezer, and Y. Weiss. “Andromaly:
a behavioral malware detection framework for android devices”, Journal
of Intelligent Information Systems, 2011, 10.1007/s10844-010-0148-x

A. Parrizas, and D. Adriyanto, “Monitoring network traffic for Android
devices”, January-16-2013, retrieved from: <http://goo.gl/5IyaCB>

Source Fire, Inc. , Snort, Web page: <http://www.snort.org/>

D. Kerr and B. Bruins, “Network flow switching and flow data export”,
June 5 2001, US Patent 6,243,667

Presentations
=============

1.  “Poster: Towards a framework for Network-based Malware detection
    System”, 35th IEEE Symposium on Security and Privacy, San José
    California, May 18, 2014.
