---
title: "Host Security Goals"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Host_Security_Goals"
type: wiki
categories: FHS, Business
author: Fraser Highland Shoppe Wiki
---

*Testing for appropriate permissions upon :
**		 /etc/logrotate.d/
**		 /etc/init.d/
**		 /tmp 
**		 /var/spool/mail/
**		 /var/tmp
**		 /var/spool/cron
**		 /etc/{ cron.d cron.daily cron.weekly cron.monthly }
*Testing for empty password, and duplicate UIDs.
*Testing for weak passwords.  (Only really weak attempts for example, password == username - more sophistication I'd leave to john/crack).
*Flagging users who've never logged in.
*Flagging users with writable files in their home area:
**		   .profile
**		   .bashrc
**		   .bash_profile
**		   .vimrc
**		   .exrc
**		   .emacs
**		   .gdbrc
**		   .forward
**		   ... etc.
*Testing for writable .ssh directories, and readable private keys.
*Testing for .rhosts, and .shosts files.
*Any changes in setuid files since the last invokation.
*Changes in filesystems/mounts.
*Testing for a filesystem above 95% fullness.

==Website Security==
*Use Google Search Console.  You will get alerts if your site changes.  Use an email address not attached to your domain in case they have redirected your MX records.
*Install security plugins for Wordpress etc.
*Update plugins and themes.
*Remove unused plugins.
*Scan user list
*Change passwords if unauthorized users appear.
*Backup the site. 
*Backup the database
*check DB users.
*Don't use the same password for 2 different sites/accounts
*Use static sites where you don't need dynamic generated pages.
===Symptoms===
*Links, photos, users you didn't add
*Not getting emails on your domain
*Sent emails not getting through
*Traffic dries up as Google and Facebook notice your site has been hacked.

===Harden Apache===
*ServerSignature Off
*ServerTokens Prod
*FileETag None
====Daemon user====
Make sure that apache has its own user/group not shared with any other daemon
*User apache
*Group apache
====outside the webroot====
Don't serve outside the '''webroot'''
*<Directory />
*  Order Deny,Allow
*  Deny from all
*  Options None
*  AllowOverride None
*</Directory>
*<Directory /'''webroot'''>
*  Order Allow,Deny
*  Allow from all
*</Directory>
====Directory Browsing====
Turn off
*Options -Indexes
====Server Side Includes====
*Options -Includes
====CGI Execution====
*Options -ExecCGI
====Symlinks====
*Options -FollowSymLinks
====Multiple Options====
*Options None
instead of
*Options -ExecCGI -FollowSymLinks -Indexes ...
====htaccess====
This is done in a Directory tag but with the AllowOverride directive. Set it to None.

*AllowOverride None

If you require Overrides ensure that they cannot be downloaded, and/or change the name to something other than .htaccess. For example we could change it to .httpdoverride, and block all files that start with .ht from being downloaded as follows:

*AccessFileName .httpdoverride
*<Files ~ "^\.ht">
*    Order allow,deny
*    Deny from all
*    Satisfy All
*</Files>
====Run mod_evasive====
====Run mod_security====
mod_security is an Apache module written by Ivan Risticwith which you can do the following:
*Simple filtering
*Regular Expression based filtering
*URL Encoding Validation
*Unicode Encoding Validation
*Auditing
*Null byte attack prevention
*Upload memory limits
*Server identity masking
*Built in Chroot support
*And more
====Disable unnecessary modules====
Apache comes with several modules installed. Learn what each module you enabled does. 
*grep LoadModule httpd.conf

Here are some modules that are typically enabled but often not needed: 
*mod_imap, 
*mod_include, 
*mod_info, 
*mod_userdir, 
*mod_status, 
*mod_cgi, 
*mod_autoindex. 

====Config File access====
*chown -R root:root /usr/local/apache
*chmod -R o-rwx /usr/local/apache
Need to use appropriate directory of course...
====DOS====
*Timeout 45
*LimitRequestBody 1048576   (filesize)
*LimitRequestFields, 
*LimitRequestFieldSize and 
*LimitRequestLine.
*LimitXMLRequestBody 10485760

*KeepAlive=on
*KeepAliveTimeout
*MaxKeepAliveRequests
*MaxRequestWorkers
*RequestReadTimeout

====Hardware Resource Limits====
*MaxClients 
*MaxSpareServers, 
*MaxRequestsPerChild, 
*ThreadsPerChild, 
*ServerLimit, and 
*MaxSpareThreads
====Restrict access by IP====
*Order Deny,Allow
*Deny from all
*Allow from 176.16.0.0/16
Or by IP:
*Order Deny,Allow
*Deny from all
*Allow from 127.0.0.1
====Block Access====
<Directory "/">
Require all denied
</Directory>
====Allow specific users====
<Directory "/.../public_html">
Require all granted
</Directory>

===Harden PHP===
http://php.net/manual/en/security.php

===Chroot===
chroot allows you to run a program in its own isolated jail. This prevents a break in on one service from being able to effect anything else on the server.

It can be fairly tricky to set this up using chroot due to library dependencies. I mentioned above that the mod_security module has built in chroot support. It makes the process as simple as adding a mod_security directive to your configuration:

SecChrootDir /chroot/apache

There are however some caveats however, so check out the docs for more info.

===Least Privilege Principle===
each application or user should only be able to access the resources that are necessary for its legitimate purpose and nothing more. 
*give people the access they require, for as long as they require to do their job, no more and no less. 

===Defense in Depth===
There is no single solution capable of addressing all your security concerns. Instead, use a layered approach of complementary security solutions each designed to address each others shortfalls. With multiple layers of security, if one fails you may still stop the attack, or at the very least be able to detect it early and recover quickly.
*employing a firewall to help mitigate external attacks, 
*employing a security scanner in the event something is successful, 
*leveraging multiple authentication controls, 
**2 factor authentication
*integration of a key manager. Each are security controls designed to directly address a threat. 

===Controls===
*Limit access: Reduce the number of people who have administrative access to your WordPress site to a minimum. You should also reduce the number of possible entry points to a minimum. You can do this by only installing web applications that you need and use. Remove any unused plugins and themes. These follows the principle of least privilege and provides administrative and logical controls to help preserve confidentiality, availability and integrity.
*Functional Isolation: Your system should be configured to minimize the amount of damage that can be done in the event that it is compromised. Where possible, avoid having a large number of diverse web applications on a single hosting account. Logical separation of applications into separate accounts with their own access will confine a compromise to that one account and reduce damage.
*Backups: Maintain reliable backups. You should occasionally verify the integrity of backups to make sure that you can restore your website if it is damaged. Have a plan to recover your website if it is compromised and document this plan. A good guide can be found WordPress Backups
*Database Security
**Different users for different apps/databases
*Stay Up-to-Date: Do your best to stay up-to-date with your WordPress installation, including plugins and themes. You should put an administrative control in place that requires a check, with some frequency, that status of your site and it's extensible components.
*Trusted Sources: Do not get plugins/themes from sources that are not trusted. (Trusted sources include the WordPress.org plugin directory.) Googling for a free version of a premium plugin is a recipe for disaster. Malicious people and organizations distribute what is known as 'nulled' plugins and themes which contain malicious code that will extend the premium plugin, but bundle it with malware that will allow them to hack your site. Do not use nulled plugins on your site.
*Security Updates and News: Security vulnerabilities is something that affects all software, WordPress is no different. To stay current, we recommend subscribing to the vulnerability database maintained by WPVulnDB.com. You can also stay ahead of the latest trends following WordPress's own Security tag.
*SFTP versus FTP

==Firewall==
===Host Firewall===
This is a machine based firewall, which opens or closes ports so that only authorized machines/networks can get at ports (applications) on the server.
===Server Firewall===
In this case, the server application itself limits which computers/networks can connect.  An example is apache .htaccess rules allowing only from the 192.* local subnet.
===Application firewall===
Applications can detect suspicious behaviour.  There is a number of Wordpress plugins that will monitor for file changes, or repeated login attempts, etc.

====Monitoring Malicious Activity====

Most WordPress security plugins and security products provide a wide array of monitoring and alerting options. These include alerts on:
*Brute force login attacks and login attempts
*Login attempts and successful login
*IP blocking

When configuring alerting it is important to have a high signal-to-noise ratio. In other words, you should only get alerts that are important to you and that you will do something about.

==Monitoring==
===Free Online Scanners===
Remote scanners look at a website as a user or search engine would.
*VirusTotal
*Sitecheck
*Unmaskparasites
*Redleg AW-Snap
These can be automated by using plugins as well, examples:
*Quttera Web Malware Scanner
*iThemes Security
===Application Scanners===
Application scanners look at the files locally on the server. For WordPress, this is achieved by security plugins.
*Wordfence
*Sucuri Security
*VaultPress
If you're running a server, you might consider:
*ClamAV
===Reputation Monitors===
Reputation monitors are services provided by established brands like Google, Bing, etc... that have a vested interest in your website displaying unaltered data.
*Google Search Console
*Bing Webmaster Tools
*Norton Webmaster Tools
*Yandex Webmaster Tools

These tools is that they are free, they have a vested interest in your site being clean, and will notify you 24 - 48 hours in advance before blocking your site.
===Uptime / Availability Monitoring===
Services like UptimeRobot and Pingdom monitor website availability. They send you an alert via email, SMS or mobile application if your website goes down. You can monitor your site from multiple locations.

===File Integrity Monitoring===
Monitoring filesystem changes can give you early warning of an intrusion. There are a number of WordPress plugins that will look at the application and help you identify if the integrity of files have changed.
*Wordfence
*Sucuri Security

It is important for you to understand what a plugin does and what it will be accessing. You should read the plugin documentation, check it's reputation by reading reviews and check the plugin support forums for any known problems before granting a plugin access to your system by installing it.
Security through Obscurity

Security through obscurity can be a valuable layer in a multi-layered Defense in Depth security strategy, but it should not be the only strategy you use to protect your site.

There are areas in WordPress where obscuring information might help with security.
==Logging==
Your hosting provider will usually provide web server logging for 24 hours. Not all hosts enable by default, please consider logging for a minimum of 7 days. You may need to enable this feature or request that they enable logging for you.

There are plugins that can help you with this logging even if your host cannot. Examples:
*Wordfence
*Sucuri Security

Logs provide an audit trail of requests that occurred on your website. If your website is hacked, it allows you or a forensic analyst to determine how your website was compromised.
Advanced Considerations

These recommendations are for the more advanced users that manage their own Dedicated and Virtual Private servers.

==Monitoring Traffic==

If you have SSH access to your web server, you can access a command line shell on your server and view your logs as they update in real-time with the following command: tail -f /location/to/log/file. This gives you the ability to monitor your raw traffic in real-time at no additional cost.

If you would like to learn how to perform log file analysis to identify attacks, you can start by reading the Log Analysis for Web Attacks: A Beginner’s Guide.

You can also monitor your website traffic in real-time using the real-time view from Google Analytics or Piwik.
==Server Integrity Monitoring==

Similar to the File integrity monitoring recommendation above, it's recommended you consider a similar approach for your web server.

A couple of system that helps streamline this process includes:
*OSSEC HIDS
*Watcher

A few tools that help include:
*diff
*Git
*inotify
*incron



[[Category: Infrastructure]]
[[Category: FHS]]
[[Category: KSFP]]
[[Category: MLFT]]
[[Category: Business]]
[[Category: Information Technology]]