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
