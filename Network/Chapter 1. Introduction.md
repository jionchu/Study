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

## 1.3 network core
- packet switching, circuit switching, network structure

### 1) packet switching
host가 application-layer의 메시지를 packet으로 나눈다.
- 각 packet은 full link capacity로 전송된다. (packet switching의 장점)

#### packet switching의 두 가지 key function
- **routing**: packet이 이동할 source-destination route를 결정한다.
- **forwarding**: packet이 input router에서 output router로 이동하는 것

destination address는 packet의 header에 들어있음

#### store-and-forward
다음 link로 전송되기 전에 모든 packet이 router에 도착해야 함 → end-end delay가 발생함

**end-end delay** = 2L/R (propagation delay를 0으로 가정했을 때)

### 2) circuit switching
- dedicated resources: no sharing
- 전통적인 telephone network에서 사용함

### 3) Packet switching vs Circuit switching
- No Call set-up, simpler / Call set-up
- full link rate
- Packet delay or loss 발생 / Guaranteed service
- Queueing delay / Call set-up delay (통신 시작하기 전)
- Packet switching에서 더 많은 사용자가 네트워크를 사용할 수 있음
- Intermittent, bursty data에 좋음 / guaranteed bandwidth를 필요로 하는 application에 좋음

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
8. 다음 각 문장의 참/거짓을 가리시오.
\- xDSL(Digital Subscriber Line)은 구리전화선을 이용하여 인터넷 연결을 제공한다.  
\- ADLS 사용자는 전화국에서 가까울수록 사용 데이터용량이 더 크다.  
\- HFC 기술은 케이블 TV 서비스가 제공되는 지역에서만 가능하다.  
\- Packet switching과 circuit switching은 인터넷의 edge network에서 사용되는 기술이다.  
\- 라우터는 routing과 forwarding을 수행한다. 이 중 어떤 포트로 수신된 패킷을 또 다른 포트로 switching하는 행위는 routing에 해당한다.  
\- Packet switching 라우터에서 발생하는 queueing delay는 라우터의 input buffer에서 발생한다. 
\- 2020년 현재 서울의 대부분 가정집은 ADSL 기술을 사용하여 인터넷에 접속하고 있다. 
9. 집까지 fiber optic 케이블을  설치하여 residual access network 속도를 높인 기술을 무엇이라고 하는가?  
10. Packet switching에서 resource(link BW) reservation을 하지 않기때문에 발생하는 delay는?   
11. Circuit switching에는 있으나 packet switching에는 없는 delay는? 
12. L-bit packet을 R bps 링크에 전송할때 transmission delay는? 
13. Packet switching을 지원하는 network 디바이스 (라우터)의 기본동작은 store-and-forward이다.  Store를 하는 이유는? (즉, 라우터가 L bit가 모두 들어올때까지 기다린 후 처리하는 이유는?)  
14. Packet switching에서 message를 보내고자하는 호스트가 그 message를 작은 크기를 packet으로 나눠전송하는 이유 두가지는 무엇인가?  
15. Sending host와 receving host 사이에 두개의 라우터가 있다고 하자. (총 3개의 링크) 각 링크의 bandwidth는 모두 R bps이다. 이때 L-bit packet 하나의 end-to-end delay는 몇초 인가? (하나의 packet만 전송된다고 가정하며 transmission delay만 고려.)  