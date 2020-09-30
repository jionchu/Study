# Chapter 1. Introduction

### overview
- 인터넷과 프로토콜
- **network edge**: hosts, access net, physical media
- **network core**: packet/circuit switching, Internet structure
- performance: **loss**, **delay**, **throughput**
- security
- protocol layers, service models
- history

## 1.1 인터넷이란 무엇인가?
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

## 1.4 delay, loss, throughput in networks

왜 delay와 loss가 발생하는가?
- packet이 router buffer에 도착하는 속도가 output link의 capacity보다 빠르면 packet이 queue된 상태에서 차례를 기다리면서 delay가 발생함
- buffer에 사용가능한(available) 자리가 없으면 도착한 packet들은 **loss**됨
  - lost packet은 이전 노드 혹은 source end system에서 다시 전송할 수도 있음

### 1) 네트워크에서 발생하는 delay 종류
- ***processing delay*** : 라우터가 packet header를 처리하여 packet의 다음 목적지를 결정하는 데 걸리는 시간
  - bit error 확인
  - output link 결정
  - 일반적으로 msec 단위 → 속도가 빨라서 상관 없음
  - ① routing table lookup
  - ② switching from input port to output port
- ***queueing delay*** : 먼저 들어온 packet이 처리되는 동안 대기하는 시간
  - output link에서 transmission되기를 기다리는 시간
  - router의 congestion level (=traffic intensity)에 달려있음
- ***transmission delay*** : packet의 모든 bit들을 링크로 내보내는 시간 (케이블의 성능과 관련)
  - L: packet length (bits)
  - R: link bandwidth (bps)
  - transmission delay = **L/R**
- ***propagation delay*** : 신호가 목적지까지 도달하는 시간
  - d: length of physical link
  - s: propagation speed
  - propagation delay = **d/s**

### 2) 전체 delay
![nodal delay](https://latex.codecogs.com/gif.latex?d_{nodal}=d_{proc}+d_{queue}+d_{trans}+d_{prop})

### 3) 실제 인터넷 delay & route
traceroute 프로그램
- 네트워크 경로 추적
- 지정된 호스트에 도달할 때까지 통과하는 경로 정보와 경로에서의 지연시간을 추적
- packet 3개 전송
- gaia.cs.umass.edu to www.eurecom.fr

### 4) Throughput
sender와 receiver 사이에 전달되는 단위 시간당 비트 양 (bits/time unit)
- **instantaneous**: 특정 시점에서의 rate
- **average**: 장기간에 걸친 rate

#### 4-1) bottleneck link
- end-end throughput을 제한하는 end-end path의 link
- throughput이 가장 작은 link를 의미함
- 서버, 라우터, 클라이언트 하나씩 연결되어 있는 경우 (서버-라우터 링크의 throughput: Rs, 라우터-클라이언트 링크의 throughput: Rc)
  - Rs < Rc → bottleneck: Rs
  - Rs > Rc → bottleneck: Rc

#### 4-2) 인터넷 시나리오
- 주로 transmission rate에 영향을 받음
- 서버 10대, 라우터 2개, 클라이언트 10대가 연결되어 있는 경우 (라우터-라우터 링크의 throughput: R)
- 연결별(서버1대-클라이언트1대) end-end throughput: min(Rc,Rs,R/10)
- transmission rate이 높은 링크는 ***intervening traffic***에 의해 bottleneck link가 될 수 있음

## 1.5 protocol layers, service models

네트워크는 다양한 요소들로 복잡하게 구성되어 있음
- host
- router
- link of various media
- application
- protocol
- hardware, software

네트워크를 어떻게 구조화할 수 있을까?

### 1) air travel의 구성
- ticket (purchase/complain) (***layer 5***)
- baggage (check/claim) (***layer 4***)
- gates (load/unload) (***layer 3***)
- runway takeoff/landing (***layer 2***)
- airplane routing (***layer 1***)

→ **layer**: 각 layer는 service를 구현함
- ***internal-layer actions***를 통해
- 아래 layer에서 제공하는 서비스에 의존함

### 2) layer를 나눈 이유
복잡한 시스템을 다루기 위해
- 모듈화를 하면 시스템을 유지하고 업데이트하기 쉬움

### 3) 5-layer Internet protocol stack
- ***application***
  - supporting network applications
  - msg
  - FTP(file transfer), SMTP(email), HTTP(web)
- ***transport***
  - data transfer 처리
  - segment
  - TCP, UDP
- ***network***
  - routing of datagrams from source to destination
  - packet, datagram
  - IP, routing protocols (OSFP, RIP, BGP)
- ***link***
  - data transfer between neighboring network elements
  - frame
  - Ethernet, 802.11 (WiFi), PPP
- ***physical***
  - bits "on the wire"

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
\- xDSL(Digital Subscriber Line)은 구리전화선을 이용하여 인터넷 연결을 제공한다. : 참  
\- ADLS 사용자는 전화국에서 가까울수록 사용 데이터용량이 더 크다. : 거짓 (속도가 빨라짐)  
\- HFC 기술은 케이블 TV 서비스가 제공되는 지역에서만 가능하다. : 참  
\- Packet switching과 circuit switching은 인터넷의 edge network에서 사용되는 기술이다. : 거짓 (Core network에서 사용하는 기술)  
\- 라우터는 routing과 forwarding을 수행한다. 이 중 어떤 포트로 수신된 패킷을 또 다른 포트로 switching하는 행위는 routing에 해당한다. : 거짓 (forwarding)  
\- Packet switching 라우터에서 발생하는 queueing delay는 라우터의 input buffer에서 발생한다. : 거짓 (output buffer에서 발생) 
\- 2020년 현재 서울의 대부분 가정집은 ADSL 기술을 사용하여 인터넷에 접속하고 있다. : 거짓 (VDSL, FTTH 기술 사용) 
9. 집까지 fiber optic 케이블을  설치하여 residual access network 속도를 높인 기술을 무엇이라고 하는가?  
\- FTTH
10. Packet switching에서 resource(link BW) reservation을 하지 않기때문에 발생하는 delay는?  
\- Queueing delay 
11. Circuit switching에는 있으나 packet switching에는 없는 delay는?  
\- Call set-up delay
12. L-bit packet을 R bps 링크에 전송할때 transmission delay는?  
\- L/R sec
13. Packet switching을 지원하는 network 디바이스 (라우터)의 기본동작은 store-and-forward이다. Store를 하는 이유는? (즉, 라우터가 L bit가 모두 들어올때까지 기다린 후 처리하는 이유는?)  
\- packet switching에서는 한 packet 단위로 움직이기 때문에 하나의 packet이 전부 들어올 때까지 기다려야 함
14. Packet switching에서 message를 보내고자하는 호스트가 그 message를 작은 크기를 packet으로 나눠전송하는 이유 두가지는 무엇인가?  
\- parallel delivery가 가능하여 edge-edge delay를 줄일 수 있음  
\- shared media에서 multiplexing을 통해 여러 user간의 메시지를 동시에 전송할 수 있음
15. Sending host와 receving host 사이에 두개의 라우터가 있다고 하자. (총 3개의 링크) 각 링크의 bandwidth는 모두 R bps이다. 이때 L-bit packet 하나의 end-to-end delay는 몇초 인가? (하나의 packet만 전송된다고 가정하며 transmission delay만 고려.)  
\- 3*L/R