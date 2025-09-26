# 🎤 Firewall Interview Questions & Answers

This document covers key firewall concepts and sample answers to common cybersecurity interview questions.

---

### 1. **What is a firewall?**
A firewall is a network security device or software that monitors and controls incoming and outgoing traffic based on predefined rules. It acts as a barrier between trusted and untrusted networks.

---

### 2. **Difference between stateful and stateless firewalls?**
- **Stateful firewalls** track the state of active connections and make decisions based on context.
- **Stateless firewalls** treat each packet independently, without regard to connection state.

---

### 3. **What are inbound and outbound rules?**
- **Inbound rules** control traffic coming into the system.
- **Outbound rules** control traffic leaving the system.
These rules help define which ports and services are accessible in each direction.

---

### 4. **How does UFW simplify firewall management?**
UFW (Uncomplicated Firewall) provides a simplified command-line interface for managing iptables on Linux. It abstracts complex rule syntax into easy commands like `ufw allow 22`.

---

### 5. **Why block port 23 (Telnet)?**
Telnet transmits data in plaintext, making it vulnerable to interception and exploitation. Blocking port 23 helps prevent insecure remote access and enforces better security practices.

---

### 6. **What are common firewall mistakes?**
- Leaving unnecessary ports open
- Misconfiguring rules (e.g., overly permissive)
- Forgetting to test rule behavior
- Not logging or monitoring traffic
- Ignoring outbound traffic filtering

---

### 7. **How does a firewall improve network security?**
Firewalls enforce access control, prevent unauthorized connections, and reduce attack surface by filtering traffic. They’re essential for segmenting networks and protecting sensitive systems.

---

### 8. **What is NAT in firewalls?**
Network Address Translation (NAT) allows multiple devices on a private network to share a single public IP. Firewalls often use NAT to route traffic securely and hide internal IPs.

---
