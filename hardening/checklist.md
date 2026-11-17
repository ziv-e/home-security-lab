# web01 hardening checklist

| Control | How | Done | Evidence |
|---|---|---|---|
| Fully updated | sudo apt update && sudo apt full-upgrade -y | [ ] | |
| Firewall denies by default | sudo ufw default deny incoming | [ ] | sudo ufw status verbose |
| Only needed ports open | ufw rules for 22 (lab only) and 80 | [ ] | Nmap before and after |
| Key-only SSH | /etc/ssh/sshd_config.d/00-hardening.conf | [ ] | Password login refused |
| No root login over SSH | PermitRootLogin no | [ ] | |
| Brute-force protection | fail2ban running | [ ] | sudo fail2ban-client status sshd |
| Automatic security updates | unattended-upgrades enabled | [ ] | systemctl status unattended-upgrades |
| Clean snapshot taken | VirtualBox snapshot | [ ] | |
