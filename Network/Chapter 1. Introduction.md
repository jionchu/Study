# Chapter 1. Introduction

### overview
- what's the Internet?
- what's a protocol?
- **network edge**: hosts, access net, physical media
- **network core**: packet/circuit switching, Internet structure
- performance: **loss**, **delay**, **throughput**

## 1.1 what is the Internet?
### 1) "nuts and bolts" view
- 수많은 연결된 컴퓨팅 장치들
  - hosts = end systems (PC: client host / server: server host)
  - running network apps (L5)
- **communication links**
  - fiber, copper, radio, satellite (다양한 종류의 link를 타고 이동함)
  - **transmission rate**: *bandwidth* (=capacity)
    - bit를 signal로 바꾸는 속도
    - link에서 가장 중요한 property
- **packet switches**: forward packets (chunks of data)
  - **routers** and **switches**
- **Internet**: *"network of networks"* (소유자가 다른 네트워크들끼리 연결되어 있음)
- **protocols** control sending, receiving of message
  - TCP(L4), IP(L3), HTTP(L5), Skype, 802.11
- **Internet standards**
  - RFC: Request for comments
  - IETF: Internet Engineering Task Force

### 2) a servie view
- **infrastructure** that provides services to applications
  - Web, VoIP, email, games, e-commerce, social nets, ...
- provides **programming interface** to apps
  - hooks that allow sending and receiving app programs to "connet" to Internet
  - provides service options, analogous to **postal service** (at L3, core NW)

### 3) What's a protocol?
**protocols** define **format**, **order** of messages sent and received among network entities, and **actions** taken on message transmission, receipt

#### human protocols
- "what's the time?"
- "I have a question"
- Introductions

#### network protocols:
- machines rather than humans
- all communication activity in Internet governed by protocols

## 1.2 network edge
- end systems, access networks, links

### 1) A closer look at network structure
- **network adge**
  - hosts: clients, servers
  - servers often in data centers
- **access networks**, physical media
  - wired, wireless communication links
- **network core**
  - interconnected routers
  - network of networks

### 2) Access networks and physical media
Q: How to connect end systems to edge router?
- residential access nets
- institutional access networks (=home network) (school, company)
- mobile access networks

keep in mind
- bandwidth (bits per second) of access networks
- shared or dedicated

## Quiz
1. 네트워크 성능을 측정하는 세 가지 파라미터는?  
\- loss, delay, throughput
2. Communication link의 용량을 의미하는 transmission rate의 단위는?  
\- bps(bits per second)
3. Access network이란 인터넷 호스트(client,server)를 core network의 edge 라우터로 연결해주는 네트워크를 말한다. 대표적인 access network 3가지는?  
\- mobile network, home network, institutional network
4. ISP stands for what?  
\- Internet Service Provider
5. 프로토콜을 정의하시오.  
\- format, order of messages sent and received among network entities, and actions taken on message transmission, receipt
6. 인터넷관련 프로토콜을 정의하는 기관은?
그 기관에서 만들어진 문서이름을 무엇이라고하나?  
\- IETF / RFC
7. "서버호스트는 core network 라우터에 직접 연결되어있다." true? false?  
\- false. access network router를 통해 연결되어 있음
