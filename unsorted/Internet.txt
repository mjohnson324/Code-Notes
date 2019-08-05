-Began in '89 w/CERN

Suppression List- emails you wish to exclude from future email services (CAN-SPAM act of 2003)
Content Distribution Network- Infrastructure that lets your site be loaded from the closest possible location to the end-user.
LAN- Local Access Network (home)
WAN- Wide Access Network (ISP router, neighborhood, town, city, etc.)
Character Set Encoding- Characters + Their binary representation
	-Unicode has no encoding
	-ASCII is legal UTF-8

Protocols:
	HTTP-
	RESTful-
	SSL- Secure Sockets Layer (encrypted server-browser links, deprecated)
	SSH- Secure Socket Shell- Secure remote access protocol

-Content length of HTTP Header = # octets, != # characters
-IP is used to send data packets (header + payload)
-Additional headers applied to payload:
	UDP directs data to a program and verifies it
	UDP header = port + checksum (does not include repair/re-request)
	TCP ensures data integrity and permits speed optimizations for multi-packet requests such as video
		-But TCP is slower than UDP (1/2 speed)

Connection Hierarchy: Physical > Data Link (mac address) > Network (routing tech) > Transport (protocols) > Session (one open-close round)
-Computers connect to an IP and port #
-DNS assigns names to IP addresses and stores them in tree
	1st: .com/gov/etc.
	2nd: name (google, amazon, etc.)
	3rd: sub-domain

Progressive Web Application- Webs which tailor code based on user resources
	-These apps require less loading time and can work offline
Service Worker: A browser middleman to reduce dependency on connections
	-Enables caching of site data to work offline
