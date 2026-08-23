---
title: "Mautic and Wordpress Integration"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Mautic_and_Wordpress_Integration"
type: wiki
categories: FHS, Marketing
author: Fraser Highland Shoppe Wiki
---

==Upload Plugin to Wordpress==
#upload WP-Mautic plugin
#configure mautic URL
##in the SETTINGs menu
==Generate Content in Mautik==
#Wordpress can have Forms or dynamic content
##Forms come out of components - forms
##dynamic content comes out of campaign 
###mautic type="focus" id="1"
###mautic type="content" slot="slot_name"
####Replace the “slot_name” with the slot name you’d like to load. This corresponds to the slot name you defined when building your campaign and adding the “Request Dynamic Content” contact decision.
###mautic type="video" gate-time="#" form-id="#" src="URL"


[[Category: All Pages]]
[[Category: Wordpress]]
[[Category: Mautik]]
[[Category: Marketing]]
[[Category: WFG]]
[[Category: FHS]]