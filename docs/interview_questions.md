# 🎤 Firewall Interview Questions & Answers

This document covers key firewall concepts and sample answers to common cybersecurity interview questions.

---

### 1. **What is a firewall?**
A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined rules. It acts as a barrier between trusted and untrusted networks.

---

### 2. **How does a firewall work?**
Firewalls inspect packets and apply rules to determine whether to allow or block traffic. They can filter based on IP address, port, protocol, or application-level data.

---

### 3. **What is the difference between stateful and stateless firewalls?**
- **Stateful:** Tracks the state of active connections and makes decisions based on context.
- **Stateless:** Evaluates each packet independently without regard to connection state.

---

### 4. **Where are firewalls used?**
Firewalls are used in:
- Personal computers
- Enterprise networks
- Cloud environments
- Routers and gateways

---

### 5. **How does UFW simplify firewall management?**
UFW (Uncomplicated Firewall) provides a user-friendly interface for managing iptables rules on Linux. It uses simple commands like `ufw allow 22` to configure rules.

---

### 6. **What are common firewall rules?**
- Allow or deny traffic on specific ports
- Restrict access by IP address
- Limit protocols (TCP/UDP)
- Log and monitor traffic

---

### 7. **What is network traffic filtering?**
It’s the process of controlling data flow based on rules that define which packets are allowed or blocked. It helps prevent unauthorized access and data exfiltration.

---

### 8. **What is NAT in firewalls?**
Network Address Translation (NAT) allows multiple devices on a private network to share a single public IP. Firewalls often use NAT to route traffic securely between networks.

---
