---
title: "Ssl certificates"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Ssl_certificates"
type: wiki
categories: FHS
author: Fraser Highland Shoppe Wiki
---

 https://letsencrypt.org/docs/

==SSL Certs on Gaddady==
===ZeroSSL===
https://zerossl.com/free-ssl/#crt
#Run script
##Log into GoDaddy as step 2 of script is upload a file
##Run script.
###Generate Account Key and CSR
####Download
###Upload file to webroot/.well-known/acme-challenge/
###Verify
###Download .crt and .key
###Upload to Godaddy (Update Cert)
####Select Domain.  Autofill by domain (to get CA Bundle)
####The Key goes in in entirety.
####The Cert is the FIRST CERT ONLY.

===le64.exe===
le64.exe --key fhs_account.key --email "sales@fraserhighlandshoppe.ca" 
--csr fhs.csr 
--csr-key fhs.key 
--crt fhs.crt 
--domains  "shop.fraserhighlandshoppe.ca" 
--generate-missing 
--live

#upload the resulting "http proof" file
#Install the cert same as in ZeroSSL
 
===ACME===
 This worked until Godaddy removed shell access AND CRON.
Works with cPanel (not classic) hosting

*tar xzvf acme.sh-master.tar.gz
*cd acme.sh-master
*. ./acme.sh --install
===Issue/Renew AGS SSL certs===
*exit and relog in
*acme.sh --issue -d airdriescots.ca -d airdriescots.com -w /home/aspd1c/public_html
*acme.sh --deploy -d airdriescots.ca -d airdriescots.com --deploy-hook cpanel_uapi
For auto updates, create a script called by crontab
 #!/bin/bash
 acme.sh --renew -d airdriescots.ca -d airdriescots.com --force
 acme.sh  --deploy  -d airdriescots.ca -d airdriescots.com  --deploy-hook cpanel_uapi

[[Category: SSL]]
[[Category: GoDaddy]]
[[Category: KSFP]]
[[Category: Airdrie Scots]]
[[Category: AGS]]
[[Category: FHS]]

===Issue/Renew shop.fhs SSL certs===
from purpleburly home dir.   
 ssh purpleburly@fraserhighlandshoppe.ca  has keyfile.
*. ./.acme.sh/acme.sh --issue -d shop.fraserhighlandshoppe.ca -w public_html/shop.fraserhighlandshoppe.ca
*. ./.acme.sh/acme.sh --deploy -d shop.fraserhighlandshoppe.ca --deploy-hook cpanel_uapi
For auto updates, create a script called by crontab
 #!/bin/bash

====Deploy through CPanel====
*zerossl.com
#Create cert
##Enter shop.fraserhighlandshoppe.ca, www.shop.fraserhighlandshoppe.ca
##Next
##Download CSR (RHS)
##Next (Generates Account Key)
##Download Account Key (LHS)
##Next
##Download Verification files
#Upload to .well-known/acme-challenge
##in public_html/shop.fraserhighlandshoppe.ca/.well-known/acme-challenge
##Upload verification files
#Next on zerossl - verifies ownership
##Download Certificates
#Upload in CPanel
##Cert 
###2 certs - second is CA bundle
##Key

==PHP Utils==
https://github.com/jpawlowski/acme_proxy.php

https://github.com/acmephp/acmephp

https://github.com/skoerfgen/ACMECert

https://github.com/kouk1/php-acme-client