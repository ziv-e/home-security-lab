# Lab journal

Notes I wrote while working through this project, step by step.

## Step 1: Check your computer
*2026-11-17*

Host computer: 13th Gen Intel(R) Core(TM) i5-1350P (1.90 GHz), 16 GB RAM, 275 GB free disk. Virtualization was already on.

## Step 2: Design the network on paper
*2026-11-17*

Lab plan: LabNet 10.10.20.0/24 (VirtualBox NAT Network, static addresses) with web01 10.10.20.5 (Ubuntu Server) and kali 10.10.20.50 (Kali Linux)[, plus meta 10.10.20.10 (Metasploitable 2)]. Rules of engagement: I will only scan and test machines inside LabNet that I created myself.

## Step 3: Install VirtualBox
*2026-11-17*

Installed VirtualBox 7.2.22 on Windows (Intel Silicon). Problems: none.

Evidence: `docs/img/03-virtualbox-version.png`

## Step 4: Create the isolated LabNet network
*2026-11-17*

Lab plan: LabNet 10.10.20.0/24 (VirtualBox NAT Network, static addresses) with web01 10.10.20.5 (Ubuntu Server) and kali 10.10.20.50 (Kali Linux)[, plus meta 10.10.20.10 (Metasploitable 2)]. Rules of engagement: I will only scan and test machines inside LabNet that I created myself.

Evidence: `docs/img/04-labnet.png`

## Step 5: Download Ubuntu Server and check it
*2026-11-17*

Downloaded ubuntu-26.04.1-live-server-amd64. Its SHA-256 begins CC8A95CDE20F and matched the official SHA256SUMS.

Evidence: `docs/img/05-ubuntu-hash.png`

## Step 6: Create the web01 VM
*2026-11-17*

Created web01: 2 CPUs, 2048 MB RAM, 25 GB disk, Adapter 1 on NAT Network LabNet.

Evidence: `docs/img/06-web01-settings.png`

## Step 7: Install Ubuntu Server
*2026-11-17*

Installed Ubuntu Server 25.04 as web01 with OpenSSH server and the static address 10.10.20.5/24 (gateway 10.10.20.1). It took about 15 minutes. Problems: none.

Evidence: `docs/img/07-ubuntu-install.png`

## Step 8: Update and install the services
*2026-11-17*

web01 IP: 10.10.20.5 (static). Installed nginx 1.28.3, Docker, ufw and fail2ban. Services nginx, docker and fail2ban are active. curl to localhost returned [status].

Evidence: `docs/img/08-web01-services.png`

## Step 9: Run a deliberately vulnerable web app
*2026-11-17*

Started OWASP Juice Shop in Docker (container juice-shop, port 3000). Note for the report: ports published by Docker bypass ufw.

Evidence: `docs/img/09-juice-shop-running.png`

## Step 10: Take a snapshot
*2026-11-17*

Took snapshot clean-install of web01 on 11/17/2026 12:17 SET, before any testing.

Evidence: `docs/img/10-snapshot.png`

## Step 11: Download and add Kali Linux
*2026-11-17*

Downloaded kali-linux-2026.3-virtualbox-amd64. Its SHA-256 matched the value on kali.org.

Evidence: `docs/img/11-kali-hash.png`

## Step 12: Connect Kali to LabNet and secure the login
*2026-11-17*

Set up kali with 4096 MB RAM on LabNet with the static address 10.10.20.50. The default password was changed on first login. (No passwords are recorded in this journal.)

## Step 13: Update Kali and find your target
*2026-11-17*

$ cat ~/home-security-lab/scans/00-first-sweep.txt
Starting Nmap 7.99 ( https://nmap.org ) at 2026-11-17 12:49 -0500
Nmap scan report for 10.10.20.1
Host is up (0.00045s latency).
MAC Address: 52:54:00:12:35:00 (QEMU virtual NIC)
Nmap scan report for 10.10.20.5
Host is up (0.0012s latency).
MAC Address: 08:00:27:23:01:54 (Oracle VirtualBox virtual NIC)
Nmap scan report for 10.10.20.50
Host is up.
Nmap done: 256 IP addresses (3 hosts up) scanned in 4.26 seconds

The first sweep found 3 hosts on LabNet. web01 is 10.10.20.5 and I added it to /etc/hosts on kali. ping web01 works.

Evidence: `scans/00-first-sweep.txt`

## Step 14: Optional: add Metasploitable 2
*2026-11-17*

Added Metasploitable 2 as meta (static 10.10.20.10) on LabNet only, never bridged.

Evidence: `docs/img/14-meta-network.png`

## Step 15: Scan and enumerate
*2026-11-17*

Full TCP scan of web01 found 3 open ports: 22/tcp openSSH 10.2p1, 80/tcp HTTP nginx 1.28.3, 3000/tcp ppp?. Nikto reported 15 items; the most important was [999997] /robots.txt: Entry '/ftp/' is returned a non-forbidden or redirect HTTP code (). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
. Surprising: 

1. The "Catastrophic" Dotfiles Are Completely Fake

• What looks alarming: Nikto flags /.htpasswd, /.bash_history, /.mysql_history, and /.psql_history—normally a worst-case scenario indicating a server's root filesystem is exposed to the internet.
• Why it's surprising: None of those files exist on the server. Because OWASP Juice Shop is a client-side Angular app, its server uses a fallback route that returns a 200 OK status with the main index.html page for almost any unknown URL. Nikto only checks the HTTP status code, so it gets fooled into thinking the entire server home directory is exposed.

2. The Server Crashed or Dropped the Scanner (20 errors reached)

• What happened: Nikto abruptly aborted at 60% completion after hitting its error limit (can't connect (timeout): Transport endpoint is not connected).
• Why it's surprising: Many automated scanners fail silently or get blocked by a Web Application Firewall (WAF). Here, the lightweight Node.js server either became overwhelmed by Nikto's rapid-fire requests or actively reset the connections, meaning 40% of the server's endpoints were never even tested.

3. The x-recruiting: /#/jobs Header

• What happened: The server returns a custom HTTP response header pointing to /#/jobs.
• Why it's surprising: Most developers try to hide server details, whereas this application deliberately leaves breadcrumbs in the headers—a classic Capture The Flag (CTF) design trait that immediately reveals both a hidden page and the app's Angular hash-routing structure (/#/).

4. robots.txt Acting as an Attacker's Roadmap

• What happened: Instead of hiding /ftp/, placing it in robots.txt handed the most sensitive directory directly to the scanner.
• Why it's surprising: In real-world audits, administrators often mistakenly treat robots.txt as a security control to "hide" sensitive folders from Google, forgetting that robots.txt is publicly readable and is the very first file penetration testers check.

Evidence: `scans/01 to 03`

## Step 19: Create and secure your GitHub account
*2026-11-17*

GitHub profile: https://github.com/ziv-e. Two-factor authentication: enabled. Commits use my private noreply email 84551481+ziv-e@users.noreply.github.com.

## Step 20: Set up Git on Kali
*2026-11-17*

Git 2.53.0 set up on kali with user.name ziv-e and my GitHub noreply email 84551481+ziv-e@users.noreply.github.com.

## Step 21: Connect to GitHub with an SSH key
*2026-11-17*

Created a separate ed25519 key for GitHub 256 SHA256:G3yezICcxRS7k678tz6TUQPce/uTmnhGj4j+h+pP+zA github-kali (ED25519)
 and added it to my account. ssh -T confirmed authentication as ziv-e.

## Step 22: Create the repository on GitHub
*2026-11-17*

Created the public repository https://github.com/ziv-e/home-security-lab.

## Step 23: Organise the project folder
*2026-11-17*

Organised the project into docs, scans, scripts, hardening and reports, with my lab journal in docs/lab-journal.md.

