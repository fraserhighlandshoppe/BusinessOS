---
title: "Practical Server Setup"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Practical_Server_Setup"
type: wiki
categories: FHS, Business
author: Fraser Highland Shoppe Wiki
---

[[Category: KSF Network]]
[[Category: Network Infrastructure]]
{{:Systemctl service files}}
==Network Checklist==
#Create a network documentation policy
#Network Topology Map
#Document Server Names, Roles, IP
#Change Log for each server (CMDB)
#Document Software versions and proof of licenses
#Document hardware components
#Document the Active Directory or equivalent
#Document the Backup strategy and tactics
#Label everything

[[Category: All Pages]]
[[Category: Business]]
[[Category: KSFP]]
[[Category: FHS]]
[[Category: MLFT]]
[[Category: Network]]
[[Category: Computers]]
[[Category: Software]]

==New Server setup steps==
 Newer versions of Fedora don't necessarily create a root user password.
 https://docs.fedoraproject.org/en-US/quick-docs/reset-root-password/
#Install base OS
##Install root user with standardized root/admin password
###We want to get to the point where we can use cobbler/koan and [[Ansible]] for the installs of OS, users, settings. 
###Kickstarts can be used with CD and Net installs as long as network card can be started
#add user kevin    -- NOTE: [[Freeipa]]
##Once ipa-client-install --mkhomedir is run not needed.  However need to test with root disabled below...
#disable ROOT login on console
##edit /etc/securetty - list only devices root allowed to login on
###Is this taken care of by [[ANSIBLE STIG]] hardening?
#disable ROOT login on SSH
##/etc/ssh/sshd_config    [[ANSIBLE STIG]]?
####PermitRootLogin yes -> no
#disable ROOT in PAM    [[ANSIBLE STIG]]?
##add a line like the following into the specific services that you want to deny...
###auth   required   /lib/security/pam_listfile.so   item=user sense=deny file=/etc/vsftpd.ftpusers onerr=succeed
#add user backups    -- NOTE: Home Dir by NFS?
##copy standard backup scripts into home dir
##modify as applicable scripts settings
##add crontab entries
#copy daemon-helper script (firewall)   -- NOTE: [[ANSIBLE]]
#copy modified /etc/services
#setup IPv6 in network scripts
#add box to dhcp (see Adding a machine to the LAN)  -- [[FreeIPA]]
#add box to dns (see Adding a machine to the LAN)   -- [[FreeIPA]]
#add box to ldap (see Adding a machine to the LAN)  -- [[FreeIPA]]
#install ocsinventory  -- NOTE: [[ANSIBLE]]
#install ossec  -- NOTE: [[ANSIBLE]]
#get PKI certificate (see Adding a machine to the LAN)  -- [[FreeIPA]]
#modify stock SSH config files
#Edit CRONTAB for backup scripts etc.-- NOTE: [[ANSIBLE]]
#create machine specific ROOT like user so we can disable root (next step)
#disable ROOT login so must use SUDO (Once server setup is completely done)-- NOTE: [[ANSIBLE]]
##set the root account's shell to /sbin/nologin in the /etc/passwd file.-- NOTE: [[ANSIBLE]]
===Granting LIMITED Root access===
#For SU add users into WHEEL group
## usermod -G wheel <username>
##Edit PAM to require wheel group for su
###auth  required /lib/security/$ISA/pam_wheel.so use_uid
===Using SUDO instead of SU or ROOT itself===
 FreeIPA does have some SUDO config stuff.
The sudo command allows for a high degree of flexibility. For instance, only users listed in the /etc/sudoers configuration file are allowed to use the sudo command and the command is executed in the user's shell, not a root shell. This means the root shell can be completely disabled, as shown in Section 4.4.1, “Allowing Root Access”.

The sudo command also provides a comprehensive audit trail. Each successful authentication is logged to the file /var/log/messages and the command issued along with the issuer's user name is logged to the file /var/log/secure.

Another advantage of the sudo command is that an administrator can allow different users access to specific commands based on their needs.
Administrators wanting to edit the sudo configuration file, /etc/sudoers, should use the visudo command.

To give someone full administrative privileges, type visudo and add a line similar to the following in the user privilege specification section:
 juan ALL=(ALL) ALL 

This example states that the user, juan, can use sudo from any host and execute any command.

The example below illustrates the granularity possible when configuring sudo:
 %users localhost=/sbin/shutdown -h now 

This example states that any user can issue the command /sbin/shutdown -h now as long as it is issued from the console.

The man page for sudoers has a detailed listing of options for this file.

===Securing Fedora===
 Ansible STIG hardening.
https://static.open-scap.org/ssg-guides/ssg-fedora-guide-default.html

https://jfearn.fedorapeople.org/fdocs/en-US/Fedora/20/html-single/Security_Guide/index.html

==Setting up a new Win8.1 Workstation==
*Turn off Windows Update.
*Turn off auto fetching of drivers
*turn off auto update of apps.
*enable Do Not Track
*enable SmartScreen.
*Bing search in Windows Search OFF
*App use info and pics OFF
*Ad ID OFF
*Location OFF
*Autoplay off
===Accounts===
*Local Accounts 
**admin - standard ksf Admin password.
**kevin
**kimberly (on FHS machines ''only'')
*Hotmail accounts
**marcia_walford@hotmail.com
**fraserhighlandshoppe@hotmail.com

===VPN===
*[[OpenVPN]]
*HE IPV6 tunneling.

===Apps===
*Firefox
*Thunderbird
*ossec
*kfw
*quickpar
*tightvnc
*pagent
====Virtualbox====
Why are we installing virtualbox?  What appliance?
#Install.
#import appliance
#do some initial setup
#do a snapshot.

===XAMPP===
Install XAMPP as a platform.  Comes with phpMyAdmin.
*add in extra "apps" (bitnami)
**mediawiki
**wordpress
**moodle
**suiteCRM (sugarCRM)
**owncloud
**prestashop
*add in extra web apps
**zencart
**vtiger 5.4 (not 6 - doesn't like to run on ANYTHING)
===non web apps===
**gvim
**gnucash
**cutewriter (pdf)
**googledrivesync (google drive)
**libreoffice
**OCSNG windows agent
**putty
**winscp
**xlite
**truecrypt
**gpg

==Adding a machine to the LAN==
 Adding a machine to IPA should create the Kerberos, LDAP, DNS, DHCP records and PKI key.
 If we are adding new Linux machines via [[Setting up Network Boot and Install|Net Install]]/Kickstart all of this should be able to be automated.
#Add machine definition to DNS forward and reverse zones (...ipa-client-install should do this)
#Add machine definition to DHCP (...ipa-client-install should do this)
#Add machine to Kerberos (...ipa-client-install should do this)
##kadmin -q "addprinc -randkey host/whitebox.ksfraser.com"
##kadmin -q "ktadd -k /var/kerberos/krb5kdc/kadm5.keytab host/enterprise.ksfraser.com"
#add machine to LDAP (...ipa-client-install should do this)
#generate machine PKI certificate (...ipa-client-install should do this)
#add machine to ossec
#Add machine Configuration to CIM ([[Puppet]] or [[Ansible]])

 [[Configuration Management Pages]]

 [[KSF Network Machine List]]

 [[Setting up Network Boot and Install]]

#Fix /etc/hosts
##don't have localhost or localdomain in there anywhere
#fix /etc/resolv.conf
##Make sure right domain and servers.  This should come from dhcp
#Get SSH keys
##cd ~/.ssh/
##scp root@ipa:/root/.ssh/i* .
#Add backup of ETC directory to git
##cd /etc
##git init
##git add -A
##git commit -m "Initial Commit `date '+%Y%m%d'`"
##git checkout -b `hostname`
##git remote add github git@github.com:/ksfraser/etc.git
##git push github `hostname`
##crontab -e
###1 2 * * * cd /etc; git add -A && git commit -a -m "Backup script `date`" &&  git push -v github `hostname`

==Network Services==
===Identification===
Username and Password
*Shared Keys
*Public Keys
Providers:
*PAM
*IPA
*Samba

===Authentication and Authorization=== 
*PAM
*IPA
*Samba

 Windows machines in an enterprise environment can have an AD.
 Home environments (licenses) don't.  However there is a GINA
 service that can replace the native authentication so that
 kerberos/ldap can be used.
 https://github.com/pgina/pgina

 https://github.com/MutonUfoAI/pgina
====Kerberos====
{{:Kerberos Pages}}

Kerberos is an authentication method which doesn't send passwords.  It uses encryption keys.

When a user logs in to their machine, they request a Ticket-Granting Ticket (TGT) from the Key Distribution Center (your main Kerberos server, or a slave server). The KDC finds the user in its database, then sends back a TGT encrypted using their key. That TGT is decrypted at the other end with the user's password. Therefore the password isn't sent over the network, increasing security.

After that, any kerberized service uses this TGT to ask for a service-specific ticket: the user doesn't need to enter their password again until the TGT expires (usually 10 hours), or is deleted. So, for example, if your entire system is Kerberos authenticated, you can log on once and then ssh to any system without having to re-authenticate.

The process works similarly for services or machines — except that a locally stored key is used instead of a password.

If you want to set up a slave kerberos server as well as the master, you can have multiple KDC lines (in krb5.conf). The KDC, as mentioned above, does the giving out of TGTs, and you can have as many as you like. However, you only have a single admin server, which acts as the master KDC.

#Install [[Kerberos]] (yum krb5-server krb5-workstation krb5-libs)
#Run kadmin.local — this only ever runs on the master server, and does not use Kerberos to authenticate to that server. 
##Before you have a Kerberos database, it's the only way to talk to the server! 
##After you have your admin user set up, you should use kadmin instead.

The commands to issue from the command line are:
#kdb5_util create -s
#kadmin.local -q "ktadd -k /etc/krb5kdc/kadm5.keytab kadmin/admin"
#kadmin.local -q "ktadd -k /etc/krb5kdc/kadm5.keytab kadmin/changepw"
#kadmin.local -q "addprinc krbadm@EXAMPLE.COM"
#kadmin.local -q "addprinc ldapadm@EXAMPLE.COM"
The first command creates your database, and the next two are needed to enable admin changes to happen. The final two commands create a Kerberos admin principle (krbadm) and an LDAP admin principal (ldapadm) — you'll be asked to provide a password.

 Using FreeIPA, it will do all of this for me.
 HOWEVER, FreeIPA apparantly doesn't use the default OOTB setup so the keytabs aren't where expected...
 /var/kerberos/krb5kdc/
 /var/kerberos/krb5/


**To allow other daemons to read the keytab and use kerberos
 setfacl -m u:apache:r /etc/krb5.keytab

SSH Can use Kerberos for authentication.  See [[SSH Integrations]]

 [[FreeIPA Setup]]
 [[Cobbler and Kerberos]]
 [[Kerberos and Login]]

====LDAP====
{{:LDAP Pages}}

 https://sites.google.com/site/wikirolanddelepper/directory-services (ldap/openldap/samba/ipa/)

 [[FreeIPA Setup]]
 [[Cobbler and LDAP]]

*LDAP (fedora-ds-base, fedora-ds-admin, fedora-idm-???, fedora-ds-dsgw)
**setup-ds-admin.pl (/usr/bin/)
**register-ds-admin.pl
**setup-ds-dsgw.pl
**etc files to [[OpenLDAP migration]] + conversion for FDS
**phpLdapAdmin
***yum install fedora-ds-base, fedora-ds-admin, fedora-ds-dsgw ldap-utils libpam-ldap libpam-smbpass libnss-ldap migrationtools phpLdapAdmin


*Radius

===LAN===
====Systemd-Networkd====
If wanting a fixed IP address on the box rather than DHCP assigned:
*create a file in /etc/systemd/network/
**match statement and config statements.
**https://wiki.debian.org/SystemdNetworkd
====DHCP====

{{:DHCP Pages}}

====DNS====
 See [[DNS Zone Files]]

 setting up bind (named)
 https://sites.google.com/site/wikirolanddelepper/postfix-tls/dns/dns---bind

 setting up bind master/slave and DDNS
 https://sites.google.com/site/wikirolanddelepper/postfix-tls/dns/dynamic-dns
 http://www.allgoodbits.org/articles/view/5
=====DDNS=====
 http://www.allgoodbits.org/articles/view/9

====BootP====
{{:BootP Pages}}

====Provisioning====
 See [[Setting up Network Boot and Install]]

===SSH===
{{:SSH Pages}}
====SSHFP====
Fingerprint in DNS
 https://ayesh.me/sshfp-verification
#Enable DNSSEC (optional)
#Modify ssh config
##Remove old/questionable key types
#Generate SSHFP records
##ssh-keygen -r SYSTEM.ksfraser.com
###If you have multiple key types, but want to limit SSHFP records to a certain set of keys ssh-keygen -r FQDN -f /etc/ssh/ssh_host_ecdsa_key.pub

=====/etc/ssh/sshd_config=====
#remove the lines starting with HostKey directive referring to non-Ed25519 keys. 
#Move the public and private keys to somewhere else so there is only one Ed25519 key pair and no other types in /etc/ssh directory.
#VerifyHostKeyDNS yes

===Proxy===
{{:Proxy Pages}}
====Squid====
 [[Advanced Proxy with privoxy tor squid]]
*yum install [[squid]]
**adjust config to include ACLs
**Apparantly OSSEC can be used to monitor the logs.
 Without SSL bumping the use of a proxy is greatly diminished...
====Privoxy====
 [[Advanced Proxy with privoxy tor squid]]
====TOR====
 [[Advanced Proxy with privoxy tor squid]]

===Printing===
===Fax===
===Scan===
====OCR====
===VoIP===
====Asterisk====

===Email===
sendmail/postfix/qmail

====spamassassin====

 https://sites.google.com/site/wikirolanddelepper/fuzzyocr - image spam filter for spamassassin

===File Storage (NFS/Samba/...)===
{{:NFS Pages}}

{{:Samba Pages}}
====Samba (CIFS)====
=====Win 8 Workstations=====
*sc.exe config lanmanworkstation depend= bowser/mrxsmb10/nsi
*sc.exe config mrxsmb20 start= disabled
====Network File Share (NFS)====
The exported file structure is in /etc/exports.

 File config is described in man exports.

 fc30 says that only files ending in .exports is exported.
 I have /etc/exports.d/music.exports

Once changing the file, run exportfs -ra OR restart nfs

*systemctl enable rpcbind
*systemctl enable nfs-server
*systemctl start rpcbind 
*systemctl start nfs-server 

On client
mount -t nfs mickey.ksfraser.com:/var/lib/tftpboot tftpboot
 Can add into /etc/fstab
 server:/mountpoint /dir nfs rw 0 0

Can check what mounts are available:
 showmount -e 192.168.1.10

rpcinfo -p <nfs server ip> displays list of all registered RPC programs. Verify that the needed services needed have the version being used (v3, v4, etc)

=====Diskless Booting=====
 http://www.faqs.org/docs/Linux-HOWTO/Network-boot-HOWTO.html#AEN219
The simplest is to export it no_root_squash and rw, but a perfect setup would export most of the root filesystem root_squash and ro, and have separate lines in the /etc/exports for directories which really require no_root_squash and/or rw.

===HTTPD===
yum install httpd

====PHP/PERL/Python====
yum install php perl python

===NNTP===
===MQ===
I used to have ApacheMQ installed but don't remember on what server.

===MQTT===
*[[mosquitto]] (currently on cpr1)
*rabbitMQ (currently on hplaptop2)

===Smart Home===
===Security===
====Network Monitoring====
====Host Monitoring====
====Anti-Virus====
====Vulnerability Scanning====
===Management===
*Puppet?
*GLPI
====Configuration Management====
*Puppet
*Chef
*[[Configuration Management with Ansible|Ansible]]

===Encryption===
*Disk
*file
*connection
===VPN===
===IPv6===


*Kerberos
*LDAP
*OSSEC
*PKI

[[Category:Business]]
[[Category:KSFP]]
[[Category:FH]]
[[Category:MLFT]]
[[Category:Network]]
[[Category:Computers]]
[[Category:Software]]

==Security==
 A good starting point is https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/4/html/Security_Guide/ch-intro.html

===cyber security layers===
====Data Security====
=====DLP=====
*OpenDLP (https://github.com/ezarko/opendlp)
=====Disk Encryption=====
*Bitlocker (Windows) (https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
*DiskCryptor (Windows/Linux) (https://diskcryptor.net/wiki/Main_Page)
*FileVault (MAC) (https://support.apple.com/en-us/HT204837)
*VeraCrypt (Windows, MAC, Linux) ( https://www.veracrypt.fr/en/Home.html )
=====File Encryption=====
*AES Crypt (https://www.aescrypt.com/)
*GNU Privacy Guard (https://www.gnupg.org/)
=====Email Encryption=====
*iSafeGuard (https://www.isafeguard.com/) Free personal use
=====Data in transit=====
*OpenSSL (https://www.openssl.org/)
*sTunnel (https://www.stunnel.org/)
=====Portable Drive Encryption=====
*Bitlocker to Go
*USB Safeguard (http://usbsafeguard.altervista.org/)
=====Data wiping=====
*CBL Data Shredder (http://www.cbldatarecovery.com/data-shredder/)
*KillDisk (https://www.killdisk.com/eraser.html)
*Eraser (https://eraser.heidi.ie/)
=====IDAM=====
*forgeRock OpenIDM/OpenAM (https://forgerock.github.io)
====Application Security====
=====Password Managers=====
*LastPass (https://www.lastpass.com)
*KeePass (https://keepass.info/)
=====WAF=====
*ModSecurity (Apache, IIS, and NGINX) (https://www.modsecurity.org/)
*WebNight (MS IIS Only) (https://www.aqtronix.com/?PageID=99)
*Shadow Daemon (https://shadowd.zecure.org)
=====SSO Access Control=====

====Endpoint/Host Security====
=====AntiVirus=====
*AVG Antivirus (https://www.avg.com/en-us/free-antivirus-download)
*Avast (https://www.avast.com/)
=====Patch Management=====
*WSUS (Microsoft Only)
*Itarian (https://www.itarian.com/patch-management/free-windows-patch-management-software.php)
=====File Integrity=====
*Tripwire open source (https://github.com/Tripwire/tripwire-open-source)
*OSSEC (https://www.ossec.net/)
=====End-point/Desktop FW=====
*ZoneAlarm (https://www.zonealarm.com/software/free-firewall/)
=====HIDS/HIPS=====
*Tripwire open source (https://github.com/Tripwire/tripwire-open-source)
*OSSEC (https://www.ossec.net/)
====Internal/Network Security====
=====Enterprise IDS/IPS=====
*Snort (https://snort.org)
*Surucata (https://suricata-ids.org/)
=====Web Proxy=====
*ZeroShell (https://zeroshell.org/)
*Haproxy (http://www.haproxy.org/)
=====NAC=====
*[[packetfence]] (https://packetfence.org/)

=====Wireless Security=====
*NetStumbler (http://www.netstumbler.com/)
*Kismet (https://www.kismetwireless.net/)
====Perimeter Security====
=====Firewall=====
*Pfsense (https://www.pfsense.org/)
*IPFire (https://www.ipfire.org/)
*OPNSense (https://opnsense.org/)
*SmoothWall (http://www.smoothwall.org/)

=====IDS/IPS=====
*Snort (https://snort.org)
*Surucata (https://suricata-ids.org/)
=====VPN=====
*ProtonVPN (https://protonvpn.com)
*Avira Phantom VPN (https://www.avira.com/en/avira-phantom-vpn)
*TunnelBear VPN (https://www.tunnelbear.com)
*AnchorFree Hotspot Shield VPN (https://www.hotspotshield.com/?vh=extfa8bf410-6c45-11e9-9037-77867bc1f2d6)
=====HoneyPot=====
*Honeyd (http://www.honeyd.org/)
=====Email Scanner=====
*MailScanner (https://www.mailscanner.info/)
*Apache SpamAssassin (https://spamassassin.apache.org/)
====Operations (Monitoring and Response)====
=====SIEM=====
*QRadar Community Edition (https://developer.ibm.com/qradar/ce/)
*AlienVault OSSIM (https://www.alienvault.com/products/ossim)
*Security Onion (https://securityonion.net/)
*ELK (https://www.elastic.co/elk-stack)
=====Monitoring=====
*Nagios (https://www.nagios.org/)
*OpenNMS (https://www.opennms.com/)
=====SOC/NOC=====

=====Incident Response=====
*Guide ( https://www.crest-approved.org/wp-content/uploads/2014/11/CSIR-Procurement-Guide.pdf )
*Policy plan ( https://phoenixnap.com/blog/cyber-security-incident-response-plan)
=====Security Dashboard=====
=====Scanning Tools=====
*Nessus Essentials ( https://www.tenable.com/products/nessus/nessus-essentials)
*OpenVAS ( https://tools.kali.org/vulnerability-analysis/openvas)
*Qualys free scan (https://freescan.qualys.com/freescan-front/)
*Burp Suite Community (https://portswigger.net/burp/communitydownload)
====Prevention (Policy Management)====
=====Security Policies=====
*https://blog.avast.com/cyber-protection-policy-template
=====Security Compliance=====
*https://www.cisecurity.org/blog/build-cybersecurity-compliance-plan-free-cis-resources/
=====Security Awareness Training=====
*https://www.eset.com/us/cybertraining/
=====Phishing Simulator=====
*GoPhish (https://getgophish.com/)
=====Penetration Testing=====
*Kali Linux ( https://www.kali.org)
*Parrot (https://www.parrotsec.org/)
*Commando [For Windows] ( https://www.fireeye.com/blog/threat-research/2019/08/commando-vm-customization-containers-kali.html)
====Other Services====
=====DNS=====
*Cloudflare (https://www.cloudflare.com/)
*NS1 (https://ns1.com)
*Quad9 (https://www.quad9.net/)
=====MFA/2FA=====
*Google Authenticator (https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en_AU)
*LastPass Authenticator (https://lastpass.com/auth/)
*Microsoft Authenticator (https://www.microsoft.com/en-us/account/authenticator)
=====Email Analyser=====
*Microsoft remote connectivity analyzer - Last tab "Message Analyzer" (https://testconnectivity.microsoft.com/ )
*MXToolBox Email Header Analyzer (https://mxtoolbox.com/EmailHeaders.aspx)
=====Log Management=====
*GrayLog ( https://www.graylog.org/)
*ELK (https://www.elastic.co/elk-stack)
*Fluentd (https://www.fluentd.org/)

===Software===
*tor (yum)
*privoxy (yum)
*IPSec (Included in the 2.6 kernels)
**[[openswan]] (yum) (for 2.4 kernels)
**KAME 'Racoon' http://lartc.org/howto/lartc.ipsec.automatic.keying.html
*Bastille (http://prdownloads.sourceforge.net/bastille-linux/Bastille-3.2.1-0.1.noarch.rpm?download)
**rpm -ivh Bastille-3.2.1-0.1.noarch.rpm
**requires Perl::TK and/or Perl::Curses for hardening mode whereas assessment mode generates html/txt reports.
**bastille --report or bastille -c (console) or bastille -x (Tk)

===Authentication and Authorization===

===Host Monitoring===
*Nagios (yum)
*icinga2 (nagios fork)
**[[Icinga Setup]]
*nagios host/service monitor (cvs + compile)
**Now precompiled.  https://www.nagios.com/products/
**Core
***http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-3.2.3.tar.gz
**Plugins
***http://prdownloads.sourceforge.net/sourceforge/nagiosplug/nagios-plugins-1.4.15.tar.gz
***http://exchange.nagios.org
**Front Ends
***http://www.nagios.org/download/frontends/
***http://exchange.nagios.org/directory/Addons/Frontends-%28GUIs-and-CLIs%29/Web-Interfaces/
**Add-Ons
***http://www.nagios.org/download/addons/
*OpenVAS
**https://github.com/greenbone/

===Network Monitoring===
*aircrack-ng(yum)
*ntop(yum)
*ngrep(yum)
**Grep on a networ stream
*etherape(yum) - graphical network traffic browser
*kismet(yum) - Wireless sniffing and monitoring
*gpsd (GPS daemon) (yum)
*dsniff (yum)
**Password sniffer on many unencrypted text based protocol
*argus (yum) - audit record generation and utilization system
**Activity report generator ..or some such.  Looks similar to tcpdump in usage.
*tcpdump (yum)
**RH related security hardening
*tcptrack 
*iftop 
*vnstat 
*nethogs 
*bmon 
*darkstat 
*iptraf 
*iperf3  
*cacti 
*rrdtool 
*monitorix 
*zabbix 
*speedtest-cli

*nbtscan (yum)
**Scans for Netbuie information
**nbtscan -v -s : 192.168.1.0/24 > nbt.txt
*nfsen project http://nfdump.sourceforge.net
**http://downloads.sourceforge.net/project/nfsen/stable/nfsen-1.3.5/nfsen-1.3.5.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fnfsen%2F&ts=1290800356&use_mirror=superb-sea2
**http://downloads.sourceforge.net/project/nfdump/stable/nfdump-1.6.2/nfdump-1.6.2.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fnfdump%2F&ts=1290800121&use_mirror=surfnet
*tcptrack http://www.rhythm.cx/~steve/devel/tcptrack/
*ipaudit
**Logs distinct connections between 2 machines based upon IP + Port.  Tracks flows, bytes.
**Can be used for DOS determination, bandwidth use, etc
*Passive Asset Detection Scans PADS
**http://downloads.sourceforge.net/project/passive/pads/pads-1.2/pads-1.2.tar.gz?r=http%3A%2F%2Fpassive.sourceforge.net%2Fdownload.php&ts=1290799800&use_mirror=softlayer
**http://downloads.sourceforge.net/project/passive/pads-archiver/pads-archiver-1.2/pads-archiver-1.2.tar.gz?r=http%3A%2F%2Fpassive.sourceforge.net%2Fdownload.php&ts=1290800045&use_mirror=iweb
*PRTG
**http://www.paessler.com/prtg
*OpenNMS
**https://github.com/OpenNMS/opennms
====Network Forensic Analysis Tool====
*NetworkMiner  (Windows/Linux) http://www.netresec.com

===Intrusion===
====Network====
Looking for/protecting against:
 *IP Spoofing
 *denial-of-service attacks
 *arp cache poisoning
 *DNS name corruption
 *man-in-the-middle attacks

*snort ''Network Intrusion Detection''(yum)
**snort.org
***scans NIC traffic
***QUICK Setup instructions - https://sites.google.com/site/wikirolanddelepper/snort
**BASE (web summary/reporting tool wget)
*[[packetfence]]
*NetReg
*aide ''File integrity check'' (yum)
*ossec ''Log monitoring''
**wget www.ossec.net/files/ossec-hids-2.0.tar.gz
**wget www.ossec.net/files/ossec-agent-win32-2.0.exe
**wget www.ossec.net/files/ui/ossec-wui-0.3.tar.gz
*BURP suite
**pen-test web proxy thingie
**http://portswigger.net/burp/burpsuite_v1.3.03.zip
[[Host Security Goals]]

[[iptables firewall]]

====Machine Based====
*Tripwire
**http://www.tripwire.org/
*Redhat Package Manager (rpm)
**rpm -V package_name.  The -V option verifies the files in the installed package called package_name
*SWATCH 
**http://sourceforge.net/projects/swatch/ — The Simple WATCHer (SWATCH) uses log files generated by syslog to alert administrators of anomalies based on user configuration files. SWATCH was designed to log any event that the user wants to add into the configuration file; however, it has been adopted widely as a host-based IDS.
*LIDS 
**http://www.lids.org/ — The Linux Intrusion Detection System (LIDS) is a kernel patch and administration tool that can also control file modification with access control lists (ACLs), and protect processes and files, even from the root user.

===AV/Trojan and Rootkit===
*Tripwire ''replaced by AIDE'' (yum)
*ClamAV ''Antivirus daemon for scanning (clamd)'' (yum)
**Edit /etc/clamd.conf (same options as /etc/clamd.d/clamd.milter)
***download virus definition file
**clamav-milter ''mail (sendmail) scanner tied to clamav'' (yum)
**clamdscan ''simplified clamscan.''
**clamscan ''file and directory AV scanner''
*amavisd-new (yum)
**scanmails program
**Requires edit of sendmail.cf
***For example:
***    Mlocal, P=/usr/bin/procmail, F=lsDFMAw5:/|@SPfhn, S=10/30, R=20/40,
***    T=DNS/RFC822/X-Unix,
***    A=procmail -Y -a $h -d $u
***changes to:
***    #Mlocal, P=/usr/bin/procmail, F=lsDFMAw5:/|@SPfhn, S=10/30, R=20/40,
***    # T=DNS/RFC822/X-Unix,
***    # A=procmail -Y -a $h -d $u
***    Mlocal, P=/usr/sbin/scanmails, F=lsDFMAw5:/|@SPfhn, S=10/30, R=20/40,
***    T=DNS/RFC822/X-Unix,
***    A=scanmails -Y -a $h -d $u
*freshclam ''virus definition update downloader'' (yum)

===Audit===
*COPS
*AAFID2
*TONIC ''Security Audits'' (IBM)
**checks password expiries, versions, etc
*Tiger ''Unix Security checks''(yum)
**checks users/paths/modules/programs/devices

===Vulnerability Scanners===
*nessus ''Network Security Scanner'' with plugins for scanning (yum) /openvas
**http://www.nessus.org/
*nikto ''http/cgi scanner''(yum)
**http://www.cirt.net/code/nikto.shtml
*Open Source Vulnerability Database OSVDB @ http://osvdb.org
**Provides a URL for further information http://www.osvdb.org/XXXX where XXXX is the vulnerability ID
**Provides a daily database dump.
*VLAD is a vulnerabilities scanner which checks for the SANS Top Ten list of common security issues (SNMP issues, file sharing issues, etc.)
**http://www.bindview.com/Support/Razor/Utilities/
*War Walking
====Basic Analysis and Security Engine====
http://base.secureideas.net/

 /mnt/2/var/www/html/base/

==Network Discovery and Inventory==
===ArpWatch===
Watches network addresses
*Inventory discovery
*Address spoofing
====ARP====
the command arp will list the interfaces that ARP knows about.

===Nedi===
yum install perl-Net-Telnet-Cisco perl-Algorithm-Diff perl-Net-Telnet perl-Net-SNMP net-snmp rrdtool php-snmp php-gd

wget http://downloads.sourceforge.net/project/nedi/nedi/w-rc4/nedi-1.0.w-rc4.tgz?use_mirror=hivelocity


(/mnt/2/development/nedi/nedi.pl)

===NetDoc===

project home page https://osl.uoregon.edu/redmine/projects/netdot

Source: https://netdot.uoregon.edu/pub/dists/netdot-0.9.10.tar.gz

wget --no-check-certificate https://netdot.uoregon.edu/pub/dists/netdot-0.9.10.tar.gz

tar xzvf netdot-0.9.10.tar.gz

cd netdot-0.9.10

make testdeps

make installdeps

setup apache conf file netdot_apache2_ldap.conf

cp etc/netdot.cron /etc/cron.d/netdot

import zone files with import_bind_zones.pl

Update various files (all can be done in one step)
*bin/exporter.pl -t Nagios,BIND,DHCPD   (bin/exporter.pl -t Nagios,Sysmon,Rancid,BIND,DHCPD)

cpan
*install Netdot::Client::REST

===OCS (Open Computer and Software) Inventory NG===
yum install ocsinventory

OR

wget http://launchpad.net/ocsinventory-server/stable-1.3/server-release-1.3.1/+download/OCSNG_UNIX_SERVER-1.3.1.tar.gz

wget http://launchpad.net/ocsinventory-windows-agent/trunk/win32-agent-release-4061/+download/OCSNG_WINDOWS_AGENT_4061.1.zip

wget http://launchpad.net/ocsinventory-unix-agent/stable/ocsinventory-unix-agent-1.1.2/+download/Ocsinventory-Agent-1.1.2.tar.gz



restart apache

http://servername/ocsreports/install.php 

mysql -uroot -prootsecret
*mysql> UPDATE mysql.user SET Password = PASSWORD('ocssecret') WHERE User = 'ocs';
*mysql> FLUSH PRIVILEGES;
*mysql> exit

vi /etc/httpd/conf.d/ocsinventory-server.conf file (arround line 31) :
*PerlSetVar OCS_DB_PWD ocssecret

vi /etc/ocsinventory/ocsinventory-reports/dbconfig.inc.php file :
*$_SESSION["PSWD_BASE"]="ocssecret"

mysql -uroot -proosecret
*mysql> CREATE USER 'glpi'@'%' IDENTIFIED BY 'glpisecret';
*mysql> GRANT USAGE ON *.* TO 'glpi'@'%' IDENTIFIED BY 'glpisecret';
*mysql> CREATE DATABASE IF NOT EXISTS `glpi` ;
*mysql> GRANT ALL PRIVILEGES ON `glpi`.* TO 'glpi'@'%';
*mysql> CREATE USER 'synchro'@'%' IDENTIFIED BY 'syncsecret';
*mysql> GRANT USAGE ON *.* TO 'synchro'@'%' IDENTIFIED BY 'syncsecret';
*mysql> GRANT SELECT ON `ocsweb`.* TO 'synchro'@'%';
*mysql> GRANT DELETE ON `ocsweb`.`deleted_equiv` TO 'synchro'@'%';
*mysql> GRANT UPDATE (`CHECKSUM`) ON `ocsweb`.`hardware` TO 'synchro'@'%';
*mysql> FLUSH PRIVILEGES;
*mysql> exit

===GLPI IT Asset Management===
yum install glpi

service httpd reload

http://servername/glpi/ 

yum install glpi-mass-ocs-import

==Encryption==
*GPG (yum)
**http://www.allgoodbits.org/articles/view/35
*Truecrypt
*Encrypted Swap
**http://linux.ioerror.us/2006/09/encrypting-your-swap-partition-on-fedora-core/
***swapoff -a
***create /etc/crypttab
***edit /etc/fstab
***cryptsetup -d /dev/random create swap /dev/VolGroup00/LogVol01
***mkswap /dev/mapper/swap
***swapon -a

==OS==
*Fedora Core 8, 
**base, 
**development, 
**webserver
**YUM cache /mnt/2/diskless/root/var/cache/yum (Net boot see /var/cache/yum)
**NFS export YUM cache to local hosts
*SSL Certificates
 see [[ssl certificates]]
 **openssl genrsa -des3 -out privkey.pem 2048
 **openssl req -new -key privkey.pem -out cert.csr
 ***Send csr to CA.
 **Private key and certificate placed in /etc/pki/tls/certs

Future OS Versions:
*Fedora 14 requires a minimum Pentium Pro 200 with 256M RAM and 9GB disk
===Logical Volumes===
Logical Volumes lets you dynamically change disk space allocated instead of requiring Partition Table changes.  Downside is management is more involved.

*vgs - display volume group information
*lvcreate - create the volume
*lvresize - change the space allocated
*xfs_growfs and resize2fs - change filesystem sizes in the volume
===OpenAFS filesystem===

===ZFS filesystem===
Installation on Fedora 10

First install the zfs-fuse package using the command [all commands from here on should be executed as the root user, unless otherwise mentioned]:

*yum install zfs-fuse

This installed zfs-fuse version 0.5 on my system that has Fedora 10.

Setting up ZFS
Before executing any commands, it should be verified that zfs-fuse daemon is running.

*pgrep zfs-fuse

If it’s not, issue the following code:

*service zfs-fuse start…

or directly run the script file as follows:

*/etc/init.d/zfs-fuse start

Managing ZFS

*zpool create K7 sda10
*zpool create -m /mnt/k7 K7 sda10
**zfs set mountpoint=/mnt/k7 K7
*zfs mount -a
**zfs mount K7
*zpool list
*zpool status

===Samba===
 [[Kerberos and Samba]]

Samba provides NetBIOS file and print sharing.

*/etc/samba/smb.conf
*service smb start
*service nmb start

firewall ports:
*dns
*ldap
*ldaps
*netbios-ssn
*netbios-dgm
*netbios-ns
*epmap
*kerberos
*microsoft-ds
*kpasswd
*mdns
*3268
*3269

smbcontrol all reload-config


====Printing====
Use CUPS.

*[printers]
**path = /var/spool/samba/
**printable = yes
**printing = CUPS|LPRNG|...

*[MyDemoPrinter]
**path = /var/spool/samba/
**browseable = yes
**printable = yes
**printer name = Printername_in_backend
**# Set the "printer name" parameter to the name of your
**# corresponding CUPS/LPD/... queue name

===CUPS===
#Install CUPS.
#Add firewall chain (631)
#configure printers.

====LPD====
*/etc/printcap
 PRINTERNAME:sd=/path/to/spool/directory:sh:mx=0:mc=0:rm=IP_or_DNS_Name
*printer spool directory
 checkpc -f
*restart
 service lpd restart
*test/status
 lpq -P PRINTERNAME

====History====
* lpadmin -p Samsung -E -v ipp://192.168.0.5/ -m everywhere
* lpadmin -p Samsung -E -v lpd://192.168.0.5/ -m everywhere
# vi /etc/cups/cupsd.conf
#systemctl restart cups
#dnf install cups hplip *hpijs* foomatic-filters foomaic-db-engine *foo2zjs* *libcups* *ghosts* *-ppd* *splix*
#vi /etc/samba/smb.conf
##enable CUPS printing
#systemctl restart smb nmb

===IPv6===

*dhcpv6
*tunnelbroker.net tunnel
**Add 2001:: /64 to DNS localnet ACL value
**Add 2001:470:20::2; as forwarder.
*Wrote test-ip6 shell script to test kernel, modules, ping, route, etc.
*radvd
**Edit /etc/radvd.conf
**edit /etc/sysctl.conf to include net.ipv6.conf.all.forwarding=1
**restart sysctl with sysctl -p
*Avahi
**Ensure 
 [server]
 use-ipv4=yes
 use-ipv6=yes
**List all mdns names with avahi-browse -r -a
*nsswitch.conf
**hosts: files mdns_minimal [NOTFOUND=return] dns mdns

===Netboot===
*[[tftpboot]] (yum)
Be aware that Cobbler overwrites the tftpboot, pxelinux.cfg directories when it is sync'd.
 See [[Cobbler Setup]]
 See [[Setting up Network Boot and Install]]
*config-system-netboot (yum)
**Asks for a NFS shared directory DISKLESSDIR.  This shared dir must have a root subdirectory.
**This creates a snapshot directory where machine specific configurations go under DISKLESSDIR
***The root subdir is the / directory of the machine you are cloning.
***rsync -a -e ssh --exclude='/sys/*' --exclude='/proc/*' CLIENTIP:/ DISKLESSDIR/root
****This clones users, passwords, etc.  Prime candidate for LDAP authentication.
**adds a linux-install subdir under /tftpboot.
***Has the kernel and initrd for booting diskless, NFS root.
***Need to change the default in pxelinux.cfg.  Default is boot from local hard drive, no mention of diskless.
***If you add a machine in the diskless wizard, a file is created.  Can cat that onto default, then change "default" from local.
These netboot machines need SELINUX to be permissive rather than enforcing.  Otherwise you get a kernel panic part way through.

http://www.faqs.org/docs/Linux-HOWTO/Network-boot-HOWTO.html#AEN537
====Linux Terminal Server project LTSP====
*[http://wtogami.livejournal.com/23648.html LTSP5 for Fedora]
*[https://www.usenix.org/techsessionssummary/linux-terminal-server-project-thin-clients-and-linux LTS thin clients]
*[https://sourceforge.net/projects/thinstation/files/6.1.0/ Thin Station on SF]

===Provisioning===
*[[cobbler]]
**Be aware that cobbler clobbers the tftp pxelinux.cfg directory.  Each time it is run it nukes ALL entries in there and replaces them with its own default and 01-MACADDR files.
 See [[Cobbler Setup]]
 See [[Setting up Network Boot and Install]]

===Network===
*[[dhcp]] (yum)
*DNS [[BIND Setup]] (yum)
**[[DNS Zone Files]]
====X11====
Ensure XDM is installed (yum)
*[[Configure XDM for remote access]] (XDMCP)
====SNMP====
*net-snmp-utils (yum)
**(snmpd and snmptrapd)
*mrtg (yum)
**perl-Net-SNMP
====LDAP====
*ldap (yum openldap)
====FUNC====
*[[func]]/funcd (yum install func)
**Network control processes
**func "*" check
**func "*" ping
**func "*" call <module> ....
**func "*.example.org" call yumcmd update
**func "*" call hardware info
**func "*" call --filteror "Fedora in os,AMD ini cpumodel,runlevel<4" service status "httpd" {'localhost.localdomain': 3}
**func "*" call fact list_fact_modules
**func "*" call fact list_fact_methods
**func "*" call fact show_fact_module "hardware"
**func "*" call fact show_fact_method "runlevel"
**func "*" call fact call_fact "runlevel"
**func '*' call iptables run "-L INPUT"
**func "*" call iptables policy
**func "*" call iptables dump
**func "*" call iptables drop_from 192.168.0.10
**func "*" call iptables.port drop_to 53 192.168.0.0/24 udp src
**func '*' call iptables policy OUTPUT DROP
**func '*' call iptables.port drop_from 80 192.168.0.0/24 udp
**func '*' call iptables.port reject_from 80 192.168.0.0/24 udp
**func '*' call iptables.port accept_from 80 192.168.0.0/24 udp
**func '*' call iptables.port drop_to 53 192.168.0.0/24 udp src
**func '*' call iptables.port reject_to 53 192.168.0.0/24 udp src
====CERTMASTER====
*certmaster
**Provides SSL certs on demand to applications through an API.
====Network IP Architecture====
<code>
#               subnet 192.168.1.0 netmask 255.255.255.0 {
#               #access points
#                       ####################################################
#                       #Provide addresses to unknown clients or not
#                       deny unknown-clients;
#                       #Provide addresses to known clients or not
#                       # for this keyword, the known client is any host declaration
#                       # in any scope.
#                       deny known-clients;
#                       ####################################################
#                       #allow bootp or not for this subnet
#                       deny bootp;
#                       deny dynamic bootp clients;
#                       ####################################################
#                       #where to get the boot file and the file's name
#                       #if next server not specified, defaults to DHCP server address
#                       next-server tftp.ap.silverdart.no-ip.org;
#                       #filename /pxefilename
#                       filename "/pxelinux.0";
#                       option root-path "nfs.ap.silverdart.no-ip.org:/tftpboot/root,v3,tcp,hard";
#                       #duplicates on MAC address can conflict when client identifier also matches
#                       # This isn't normal but will occur on dual boot machines
#                       # default is allow
#                       allow duplicates;
#                       #default-lease-time 600;
#                       ####################################################
#                       #Declines allow a client to indicate the address isn't valid for some reason
#                       # However, buggy clients could result in running through the pool,
#                       # thrashing DNS updates and causing old dhcp address allocations to be forgotten
#                       ignore declines;
#                       ####################################################
#                       #Client updates option is to tell the dhcp server whether
#                       # it should allow the client to update the dns server or not
#                       ignore client-updates;
#                       ####################################################
#                       # Allow or deny members of class
#                       deny members of "classname";
#                       ####################################################
#                       #Dynamic DNS updates
#                       #reversed IP address appended automagically
#                       ddns-rev-domainname "in-addr.arpa.";
#                       #perform DNS updates or not.  Valid in scopes
#                       ddns-updates            on;
#                       ddns-domainname "ap.silverdart.no-ip.org.";     #FQDN
#                       zone in-addr.arpa. {
#                               primary 192.168.1.14;
#                               key DHCP_UPDATER;
#                       }
#                       zone ap.silverdart.no-ip.org. {
#                               primary dns.ap.silverdart.no-ip.org;
#                               key DHCP_UPDATER;
#                       }
#                       server-identifier 192.168.1.14; #What IP address is responding.  Important on aliased subnets
#                       option domain-name "ap.silverdart.no-ip.org.";
#                       option domain-name-servers ns1.ap.silverdart.no-ip.org, ns2.ap.silverdart.no-ip.org;
#                       option routers 192.168.1.1, 192.168.1.2;
#                       range dynamic-bootp 192.168.1.101 192.168.1.200;
#                       #range 192.168.10.1 192.168.10.100;
        #     #option auto-proxy-config "http://wpad.ap.silverdart.no-ip.org/registerd.wpad.dat"
#               }
#               subnet 192.168.2.0 netmask 255.255.255.0 {
#               #tor networks           "tor"
#               }
#               subnet 192.168.3.0 netmask 255.255.255.0 {
#               #ROM devices            "rom"
#               }
#               subnet 192.168.4.0 netmask 255.255.255.0 {
#               #Internet accessible    "pub"
#               }
#               subnet 192.168.5.0 netmask 255.255.255.0 {
#               #private network        "pri"
#               }
#               subnet 192.168.6.0 netmask 255.255.255.0 {
#               #workstations           "work"
#               }
#               subnet 192.168.7.0 netmask 255.255.255.0 {
#               #Music/midi             "media"
#               }
#               subnet 192.168.8.0 netmask 255.255.255.0 {
#               #guest machines         "guest"
#               }
#               subnet 192.168.9.0 netmask 255.255.255.0 {
#               #application servers    "apps"
#               }
#               subnet 192.168.10.0 netmask 255.255.255.0 {
#               #unauthorized guests
#               }
                #Routers .1 - .9
                #servers .10 - .19
                #       .10     Primary DHCP DNS NTP
                #       .11     Secondary DHCP DNS NTP
                #       .12     Pop IMAP SMTP
                #       .13     Radius Security
                #       .14     NNTP
                #       .15     HTTP
                #       .16     Cobbler TFTP Puppet
                #       .17     Database
                #       .18     Proxies OpenVPN Squid Privoxy
                #       .19     Application Server
                # .21 - .29     Printers
                # .31 - .39
                # .41 - .49     VoIP
                # .51 - .59     IP Cams
                # .61 - .69     X-Terminals
                # .71 - .79     Desktops
                # .81 - .89     WIFI
                # .91 - .99     Laptops
                # .101 - .109   DLNA/UPnP Media Servers
                # .111 - .119   DLNA/UPnP Media Clients

</code>

===Package Deployment Management===
*[[GLPI]]
*[[puppet]] configuration management

Server Side
*Puppet Recipe Manager (not yet installed)
*rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/i386/epel-release-5-3.noarch.rpm
*yum install puppet-server
*yum install ruby-rdoc
*[[Puppet Config Files]]
*/usr/sbin/puppetmasterd --mkusers
**Add DNS/Hosts entries for the puppet server with CNAME puppet.
*service puppetmaster start
Test that it is working
*puppetd --server myserver.domain.com --waitforcert 60 --test
 info: No classes to store
 info: Caching catalog at /var/lib/puppet/localconfig.yaml
 notice: Starting catalog run
 info: Creating state file /var/lib/puppet/state/state.yaml
 notice: Finished catalog run in 0.78 seconds



Client Side
*rpm -Uvh http://download.fedora.redhat.com/pub/epel/5/i386/epel-release-5-3.noarch.rpm
*yum install puppet ruby-rdoc
*puppetd --verbose --server puppet.domain.com
 info: Creating a new certificate request for pclient.torridnetworks.com
 info: Creating a new SSL key at /var/lib/puppet/ssl/private_keys/puppetclient.domain.com.pem

Back on the Server
*puppetca --list
*puppetca --sign puppetclient.domain.com

Getting it all started
*chkconfig --add puppetmaster
*chkconfig --add puppet
*service puppetmaster start
*service puppet start

====puppet and ldap====
install ruby-ldap.
*test with ruby -rldap -e 'puts :installed'

Add the LDAP schema
*dn: cn=schema
*AttributeTypes: ( 1.1.3.10 NAME 'puppetclass' DESC 'Puppet Node Class' EQUALITY caseIgnoreIA5Match SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
*AttributeTypes: ( 1.1.3.9 NAME 'parentnode' DESC 'Puppet Parent Node' EQUALITY caseIgnoreIA5Match SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 )
*objectClass: ( 1.1.1.2 NAME 'puppetClient' DESC 'Puppet Client objectclass' SUP top AUXILIARY MAY ( puppetclass $ parentnode ))

update puppetmasterd.conf.  Not sure if we need the ldap or puppetmasterd section - depends on whose documentation you read.
*[ldap]
*ldapnodes = true
*ldapserver = ldapserver.example.com
*ldapbase = dc=example,dc=com
*[puppetmasterd]
*node_terminus = ldap
*ldapserver = ldap.silverdart.no-ip.org
*ldapbase = dc=silverdart,dc=no-ip,dc=org


Add some entries into LDAP
*Modify all existing host LDAP entries so they have objectClass: puppetClient, a puppetclass attribute (my initial ones were server and desktop, and a parentnode  attribute (I have baseserver and basedesktop).
*Create baseserver and basedesktop LDAP entries.

Node attributes
*dn: cn=basenode,ou=Hosts,dc=madstop,dc=com
*objectClass: device
*objectClass: ipHost
*objectClass: puppetClient
*objectClass: top
*cn: basenode
*environment: production
*ipHostNumber: 192.168.0.1
*description: The base node
*puppetClass: baseclass
*puppetVar: config_exim=true
*puppetVar: config_exim_trusted_users=lludwig,lak,joe
*#TestServer
*dn: cn=testserver,ou=Hosts,dc=madstop,dc=com
*objectClass: device
*objectClass: ipHost
*objectClass: puppetClient
*objectClass: top
*cn: testserver
*environment: testing
*ipHostNumber: 192.168.0.50
*description: My test server
*l: dc1
*puppetClass: testing
*puppetClass: solaris

===Backup Restore===
I originally was using tar files.  However, the collection of them is getting rather large.  And really, most files don't change any/much from day to day.
*GIT ([[Using GIT for Backup and Restore]])

==Project Management Tools==
*dotproject
*mediawiki (yum)
*eventum (mysql download)

==Business Management Tools==
===CRM===
*vtiger
**grant all to an ID on the destination db so that you don't have to share the root user/pw
**run the install wizard
**login as admin to setup remaining items
***outgoing smtp server (settings - settings - outgoing server) (Sends a test email on the save to the admin email addr)
***Create users
***Company Details (settings - communication templates - company details)
***Add Cdn Currency (Settings - currency)
***Add GST (Settings - Tax Calculations)
***Inventory: Terms and Conditions (Settings - Inventory Terms and Conditions) This details payment due dates, etc.
*SugarCRM
**similar to vTiger;  forked from same base software long ago.
**module builder seems to be more complete
**REST/SOAP
*Wordpress Plugins
**CiviCRM
**No BS
**UniCRM
**WP-CRM
**WP-CRM-SYSTEM

===ERP===
*openERP (was tinyerp.  (Yum tinyerp tinyerp-server))

===Accounting===
*FrontAccounting
===HRM===
*orangeHRM

===Online Shopping===
*ZenCart
*Wordpress + WooCommerce

===Computer Management===
See above for GLPI and OCS

==Database==
*mysqld (yum)
*mysql (yum)
**[[Mysql replica]]
*phpMyAdmin (yum)

==Development==
*php-soap (yum)
*tomcat
*tcl (yum)
===Source/Revision Control===
*mercurial (yum)
*git (yum)
===Bug and Ticket tracking===
*mantis (yum)
*eventum (mysql download) (preferred)
===Test Cases and Test Results===
*RTH Turbo (rth-turbo.googlecode.com) (RTH cloned Test Director.  This is a fork)
**create rth db
**import sql file
**update api/properties_inc.php 
***use the table name w/o caps since the SQL file didn't have caps.
***webserver
***ldapserver
****Add user to LDAP server
***login method
***javascript
***Turn on/off FCKEditor (requires javascript)
***Set debug options
***Set email options
**Make sure rth_file_upload is writable by the webserver to create new projects (chmod, chown apache, chcon)
**login as admin and change password
**Add users

==Virtualization==
*OpenVZ
*[http://virt-tools.org/ Virt-tools]
*Qemu
*XEN
*VMServer/VMPlayer
*Virtualbox
*[[Virtualization on F30]]

==Media Server==
*Mediatomb (yum)
**/etc/mediatomb.conf

==Zoneminder==
Sricam rtsp://1515866:m1l1ce@192.168.1.25/onvif1

*Merkury http://192.168.1.24/??   realm www-user@ppstrong   Ports 80, 6668
*minicam http://192.168.1.23/ucast/11 ??   realm IPCamera_Web  Ports 80

==Load Balancing via Virtual Server==

http://www.linuxforu.com/how-to/balancing-traffic-across-data-centres-using-lvs/

[[Virtual Server Load Balance Setup]]

==Other==
*graphviz (yum)
*sane (yum)
*mutt (yum)
*lynx (yum)
*squid (yum)
*tesseract (svn (google) )
*ocropus (wget (google) )
*noip client update (wget noip)

===Printing===
Fedora installs CUPS by default.  Using the built in web config server (localhost:631) you can add printers, etc

===Scanning===
<nowiki>
#!/bin/bash

# scan dimensions
X=215.9
Y=279.4

# source
source="ADF Duplex"

# temporary directory to store scanned pages
tmpdir=`mktemp -d`

# format of filenames to store
format=$tmpdir/out%04d.tiff

# scan pages
echo Scanning pages... >&2
scanimage --batch=$format --format=tiff --mode Lineart --resolution 300 --source "$source" -x $X -y $Y

# flip every second page, because it was upside-down on scan
echo Flipping back pages... >&2
for (( n = 2; $n <= 9999; n += 2 )); do
  filename=`printf $tmpdir/out%04d.tiff $n`
  if [ ! -f $filename ]; then break; fi
  convert -flip $filename $filename.flipped.tiff
  convert -flop $filename.flipped.tiff $filename
  rm $filename.flipped.tiff
done

# get name of file to output to (stdout if not specified)
outfile=$1
if [ -z $outfile ]; then outfile=-; fi

# assemble into a single output file
tiffcp -c g4 $tmpdir/*.tiff $outfile

# remove temporary directory and all of its contents
rm -rf $tmpdir

</nowiki>


SANE or xsane or saned
*configure /etc/sane.d/escl.conf for network attached scanners.
**configure /etc/sane.d/* for the appropriate USB/serial printers.
scanimage -L will list detected scanners

xsane will launch a gui in X

 IF a program has the scanner open (e.g. xsane) then scanimage will NOT find the scanner as it won't respond to queries.

==Hosted Server Infrastructure==
===ksfraser.com===
====ags====
only tgz files.
====andyapp====
*mediawiki
*webtrees
*wordpress (media database)
====bagpipes====
*campaigns
*comments
*custportal
*feeds
*images
*lessons
*mediawiki-1.10.4
*music
*piping...
*wiki
*wordpress
*wp-content
*wp-includes
*wp-json
====leadership====
*Static site hosted locally and then wget mirrored!
====lists====
*was a phplist install.  Hacked, and not used, so tar'd and removed.
====mediawiki====
*hacked pages.  don't remember when last used.  tar'd and removed.
*database is being backed up by backup-db script.
====railroad====
*Static site hosted locally and then wget mirrored!
====realestate====
*wordpress site, but not currently being used.
*eventum site.
====travel====
*Currently a wordpress site, but to be hosted locally and wget'd
===fhs-laptop1===
====bagpipes_wiki====
====bugzilla4====
====devel====
*dotproject
*kallimachos
*mautik
*wiki
=====fhs=====
*dotproject
*frontaccounting
*itop
*limesurvey
*mautik
*orangehrm
*phplist
*POS
*seopanel
*vtigercrm
*weberp
*wiki
*wordpress
*zencart
====fhs====
*dotproject
*frontaccounting
*itop
*limesurvey
*mautik
*orangehrm
*phplist
*POS
*vtigercrm
*weberp
*wiki
*wordpress
====finance====
mediawiki setup
====finance_local====
mediawiki setup
====kallimachos====
legacy code + wordpress
====ksf====
These are sites being mirrored to PROD
=====bagpipes=====
=====finance=====
=====leadership=====
=====railroad=====
=====realestate=====
====leadership====
Looks to be the static output from ksf/leadership
====mautik====
====mlf====
Marcia's travel blog
===fhsws001===
====acpt====
====ags====
====asset_management====
====asterisk====
====dashboard====
====defiant====
====devel====
====fhs====
====finance====
====fitness====
====fraserwiki====
====gettingthingsdone====
====kallimachos====
====ksf====
====ldap====
====maintain====
====pipeband====
====pipingquotes====
====prod====
====propertymanagement====
====realestate====
====skel-app====
====smart-restaurant====
====vtiger====
====web2project====
====webdav====
====webdot====
====webtrees====
====wfg====
====wiki====
====xampp====

==Smart Home==
===OpenHAB===
*Server component
**Local (http://hplaptop2.ksfraser.com:8080/)
**Cloud (https://myopenhab.org/account)
*Smart Phone/Tablet component
*Connects to various devices

===OpenTracks===
*Lets you push on MQTT a location message.  
**Could be used for presence.  
**Could be used for "scenes" (scripts) through OpenHAB
===RabbitMQ===
*Message Queue server
**MQTT
===Asterisk===
*Connection to Honeywell Lynx system through ATA and AlarmReceiver