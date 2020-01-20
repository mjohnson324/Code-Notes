# A Brief Guide to how the Internet Works

* Connection Hierarchy:
  * Physical
    * Data Link (mac address)
      * Network (routing tech)
        * Transport (protocols)
          * Session (one open-close round)
* Computers connect to an IP and port #

## Infrastructure

* **LAN**- Local Access Network (home)
* **WAN**- Wide Access Network (ISP router, neighborhood, town, city, etc.)
* **DNS**- Domain Name System. Assigns names to IP addresses and stores them in a tree structure with levels as follows:

1. .com/gov/etc.
2. name (google, amazon, etc.)
3. sub-domain

* Content Distribution Network- Infrastructure that lets your site be loaded from the closest possible location to the end-user.

## Understanding Requests

**What happens when you navigate to google.com?**

1. Browser checks its own DNS cache for a corresponding IP address, then your OS’ DNS cache, then (most likely) checks the default router's DNS cache, then ISP / configured DNS server until it gets an answer.
2. Browser builds HTTP GET string with `http://url` as the requested URL
3. Browser sends request over the network (if asked how that works, mention the Border Gateway Protocol and say you don’t know how it works)
4. (Possible interaction with proxy server / load balancer / CDN / etc.)
5. Server parses request string and routes it using Regex on the request path
6. Application layer assembles a response, possibly via a connection to a DB server
7. Response goes back over the network
8. Browser parses the response
9. Browser checks the headers, in particular the status code.
10. Browser goes down each HTML element and either paints the DOM or executes the tag
11. The browser builds a new GET request for each CSS or JS tag, goes through the same steps as above, and runs the code before proceeding.

* [Short answer](https://jiangchengl.wordpress.com/2015/08/20/what-happens-when-you-type-www-example-com-in-the-browser-address-and-enter-press-button/)
* [Medium answer](http://igoro.com/archive/what-really-happens-when-you-navigate-to-a-url/comment-page-4/)
* [Long answer](https://github.com/alex/what-happens-when)

## RESTful Architecture

**ReST**- Representational State Transfer. A stateless communication standard for the web permitting independent client and server implementation. Separates data storage and UI concerns.

**Key Parts:**

1. HTTP Verb describing the desired operation
   * Verbs: Post, Get, Put/Patch, Delete (maps to CRUD)
2. Header, Path, optional message body

## Frontend Design

* **Progressive Web Application**- Webs which tailor code based on user resources
  * These apps require less loading time and can work offline
* **Service Worker**: A browser middleman to reduce dependency on connections
  * Enables caching of site data to work offline

## Protocols

* **IP**- Internet Protocol
  * Sends data packets via a header and payload
  * Additional headers for other protocols placed in payload
* **UDP**-
  * Header: (port and checksum) directs data to a program and verifies it
  * **TCP**-
    * TCP ensures data integrity and permits speed optimizations for multi-packet requests such as video
    * About 1/2 the speed of UDP
* **HTTP**- Hyper Text Transfer Protocol
  * Content length of HTTP Header = # octets, != # characters
* **SSH**- Secure Socket Shell- Secure remote access protocol

Image Summary:

Layer

Application HTTP Format data request and response
Transport TCP Deliver data between client and server
Internet IP Address client and server
Link Ethernet Map request to physical network
