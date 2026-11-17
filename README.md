# Home Security Lab

A virtual lab I built to practise Linux administration, networking and ethical hacking on systems I own.

## What's inside
| Machine | Operating system | Role |
|---|---|---|
| web01 | Ubuntu Server 26.04 LTS | Web server: nginx, Docker, OWASP Juice Shop |
| kali | Kali Linux | Attack and admin workstation |
| meta (optional) | Metasploitable 2 | Deliberately vulnerable target |

All machines sit on an isolated VirtualBox NAT Network (10.10.20.0/24). See [docs/network.md](docs/network.md).

## Skills shown
- Virtualisation and network design
- Linux server administration and hardening (ufw, SSH keys, fail2ban)
- Network discovery and service enumeration (Nmap, Nikto)
- Web application testing against the OWASP Top 10 (Juice Shop)
- Python scripting for automation
- Technical reporting

## Key findings
| # | Finding | Risk | Fix |
|---|---|---|---|
| 1 | Example: SSH accepted password logins | Medium | Key-only SSH, verified with a re-scan |

Full report: [reports/web01-assessment.md](reports/web01-assessment.md)

## Repository layout
- `docs/` lab design, setup notes and screenshots
- `scans/` Nmap and Nikto output (lab addresses only)
- `hardening/` checklist and configuration changes
- `reports/` assessment report
- `cases/` case studies of realistic practice tickets
- `scripts/` Python tools

## Ethics
Every test here was run only against virtual machines I own, on an isolated network.

## What I learned
Write three to five honest sentences here.
