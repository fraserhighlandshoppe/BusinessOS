---
title: "KSFII Business Continuity DR Test Plan"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=KSFII_Business_Continuity_DR_Test_Plan"
type: wiki
categories: FHS, Business
author: Fraser Highland Shoppe Wiki
---


 {{:KSFII Pages}}
[[Category: KSFII]]

 Also See [[Continuity Planning]]

This document is our TEST PLAN for ensuring that the [[KSFII Business Continuity Plan]] is sufficient.
==Continuity Plan==
 Business Continuity Planning - what will stop us from operating our business?

Our firm’s policy is to respond to a Significant Business Disruption (SBD) by 
#safeguarding employees’ lives
#safeguarding firm property including the firm’s books and records
#making a financial and operational assessment
#quickly recovering and resuming operations
#allowing our customers to transact business. 
In the event that we determine we are unable to continue our business, we will assure customers prompt access to their funds and securities.

Our plan anticipates internal and external SBD. Internal SBDs affect only our firm’s ability to communicate and do business, such as a fire in our building. 


===Prerequisits===
*Reference to legal documents that support plan
*Checklist/process
*Funding
*Partner
*Disaster Preparedness
*Emergency Response
*Business Recovery

===Communication===
[[KSFII Emergency Contact List‎]]

Incoming channels: [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1138]
====EMERGENCY CONTACT====
Our Emergency Contact is Kevin Fraser
*kevin@ksfraser.com
*587-600-1654 (o)
*587-830-1654 (c)
*403-912-1654 (f)
*http://protect.ksfraser.ca
====Internal====
This plan is to be distributed to every department and employee.

As part of the plan, employees need to know:
*who to notify in case of a disaster
*What IMMEDIATE ACTIONS need to be taken
**Protect Life
**Protect Property

Each step of the plan needs to be described in plain language.
*Each step needs to be assigned to someone

====External====
=====Clients=====
Certain risks pertain to clients.  They should be confident that we have a plan in place addressing those risks.

We will provide a copy of our BCP to clients upon request.  The version for clients can be printed out of the CRM in the Accounts, Contacts and Contracts modules.
[http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1158]

=====Providers/Suppliers=====
=====Employee Next of Kin=====
Certain portions of this Plan should be made available to Employee NoK upon request or upon need.
[http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1173]

===Business Description===

===Office Locations===
NA for plan
====Alternative Physical Location(s) of Employees====
In the event of an SBD, we will move our staff from affected office(s) to the closest of our unaffected office location(s). 

If none of our other office locations is available to receive those staff, we will move them to 242 Kings Heights Dr SE, Airdrie, T4A 0E8. Its main telephone number is 587-600-0013.
 [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1178]

===Customers’ Access to Funds and Securities===
Our firm does not maintain custody of customers’ policies.  They are maintained with our carrier partners. 

In the event of an internal or external SBD

*TEST - Notification to Customers of Outage - Website  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1283]
*TEST - Notification to Customers of Outage - IVR  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1288]
*TEST - Notification to Customers of Outage - Mailing List/Email  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1293]
*TEST - Notification to Customers of Outage - RoboDialer  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1298]

===Data Back-Up and Recovery (Hard Copy and Electronic)===

 See [[Using GIT for Backup and Restore]]
 Document [[Project Requirements Domains]]

*DATA Backup and Recovery [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1183]
*DATA Backup and Recovery - HARDCOPY [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1188]
*DATA Backup and Recovery - ELECTRONIC [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1193]
*DATA Backup and Recovery - ELECTRONIC - MYSQL [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1198]
*DATA Backup and Recovery - ELECTRONIC - CUSTOMER FILES (EncFS) [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1203]
*DATA Backup and Recovery - ELECTRONIC - WEBSERVER INTERNAL [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1208]
*DATA Backup and Recovery - ELECTRONIC - WEBSERVER EXTERNAL [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1213]
*DATA Backup and Recovery - ELECTRONIC - WEBSERVER INTERNAL - WIKI [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1218]
*DATA Backup and Recovery - ELECTRONIC - WEBSERVER INTERNAL - CRM [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1223]
*DATA Backup and Recovery - ELECTRONIC - NON SECURED FILES [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1228]

===Financial and Operational Assessments===
In the event of an SBD, we will immediately identify what means will permit us to communicate with our customers, employees, critical business constituents, critical banks, critical counter-parties and regulators.

Although the effects of an SBD will determine the means of alternative communication, the communications options we will employ will include our website, telephone voice mail, and secure email. In addition, we will retrieve our key activity records as described in the section above, Data Back-Up and Recovery (Hard Copy and Electronic).

===Mission Critical Systems===
*DATA Backup and Recovery - ELECTRONIC - MYSQL  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1198]
*DATA Backup and Recovery - ELECTRONIC - CUSTOMER FILES (EncFS)  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1203]
*DATA Backup and Recovery - ELECTRONIC - WEBSERVER INTERNAL  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1208]
**DATA Backup and Recovery - ELECTRONIC - WEBSERVER INTERNAL - WIKI  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1218]
**DATA Backup and Recovery - ELECTRONIC - WEBSERVER INTERNAL - CRM  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1223]
*DATA Backup and Recovery - ELECTRONIC - WEBSERVER EXTERNAL  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1213]
*DATA Backup and Recovery - ELECTRONIC - NON SECURED FILES   [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1228]
*DATA Backup and Recovery   [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1183]
*TEST Internet Access  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1233]
**TEST Internet Access - EMAIL [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1238]
**TEST Internet Access - HUB FINANCIAL (Internet in general) [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1243]

===Alternate Communications Between the Firm and Customers, Employees, and Regulators===
Currently our firm receives application and servicing requests from customers via in-person meetings.

During an SBD, either internal or external, we will continue to take applications and service requests through any method that is available and reliable. In addition, as communications permit, we will inform our customers when communications become available to tell them what alternatives they have to send their orders to us.

*TEST - Alternative Coimmunications Methods - ZOOM  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1253]
*TEST - Alternative Coimmunications Methods - ROBODIAL  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1258]
*TEST - Alternative Communications Methods - MAILING LIST  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1263]
*TEST - Alternative Coimmunications Methods - EMAIL  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1268]
*TEST - Alternative Coimmunications Methods - WEBSITE BANNER/POPUP  [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1273]

===Critical Business Constituents, Banks, and Counter-Parties===
NA

===Regulatory Reporting===
Our firm is subject to regulation by: 
*Alberta Insurance Council
*FINTRACK

In the event of an SBD, we will check with the provincial regulators to determine which means of filing are still available to us. In the event that we cannot contact our regulators, we will continue to file required reports using the communication means available to us.
===Disclosure of Business Continuity Plan===
*BCP available for Clients upon Request [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1158]
*TEST - Employee access to DR Plan [http://fhsws002.ksfraser.com/infra/software-devel/mantis/view.php?id=1168]

===Succession Plan===
 This section of the plan is for the transition of Kevin as the owner/founder to exiting the business.
 *How will the business operate if Kevin isn't here?

===Contingency Planning===
 This section of the plan is for Disaster Recovery type planning.

<TABLE FRAME=VOID CELLSPACING=0 COLS=10 RULES=NONE BORDER=0>
	<COLGROUP><COL WIDTH=49><COL WIDTH=283><COL WIDTH=339><COL WIDTH=67><COL WIDTH=173><COL WIDTH=141><COL WIDTH=68><COL WIDTH=67><COL WIDTH=67><COL WIDTH=67></COLGROUP>
	<TBODY>
		<TR>
			<TD WIDTH=49 HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD WIDTH=283 ALIGN=RIGHT><B>Project ID:</B></TD>
			<TD STYLE="border-bottom: 1px solid #000000" WIDTH=339 ALIGN=LEFT VALIGN=TOP SDNUM="4105;0;@"><BR></TD>
			<TD STYLE="border-bottom: 1px solid #000000" WIDTH=67 ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-bottom: 1px solid #000000" WIDTH=173 ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD WIDTH=141 ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD WIDTH=68 ALIGN=CENTER><BR></TD>
			<TD WIDTH=67 ALIGN=LEFT><BR></TD>
			<TD WIDTH=67 ALIGN=LEFT><BR></TD>
			<TD WIDTH=67 ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=RIGHT><B>Project Name:</B></TD>
			<TD STYLE="border-bottom: 1px solid #000000" ALIGN=LEFT VALIGN=TOP SDNUM="4105;0;@"><BR></TD>
			<TD STYLE="border-bottom: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-bottom: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=RIGHT><B>Project Manager:</B></TD>
			<TD STYLE="border-bottom: 1px solid #000000" ALIGN=LEFT VALIGN=TOP SDNUM="4105;0;@"><BR></TD>
			<TD STYLE="border-bottom: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-bottom: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=63 ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Risk No.</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Summary</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Consequences</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Exposure<BR>(VH/H/ M/L)</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Risk Containment Approach</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Actions</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Risk Status</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Owner</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Date Last Updated</B></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER BGCOLOR="#C0C0C0"><B>Date Closed</B></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Rain</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP>Damage of Assets</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Insurance</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP SDNUM="4105;0;DD-MMM"><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP SDNUM="4105;0;DD-MMM"><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=34 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Rain</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP>Damage of Client Files</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Carry files in weather resistant case</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP SDNUM="4105;0;DD-MMM"><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP SDNUM="4105;0;DD-MMM"><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=34 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Rain</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP>Damage of IT Assets</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Carry files in weather resistant case</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP SDNUM="4105;0;DD-MMM"><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP SDNUM="4105;0;DD-MMM"><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Hail</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP>Damage of Assets</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Insurance</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Heat</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP>Damage of Assets</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Insurance</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Heat</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Injury of Staff </TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Air Conditioning</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Weather &ndash; Heat</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP>Poor operations of IT Assets</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Minimuze Exposure</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP>Natural Disasters &ndash; Flood</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
		</TR>
		<TR>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT>Natural Disasters &ndash; Earthquack</TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=CENTER VALIGN=TOP><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT><BR></TD>
			<TD STYLE="border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000" ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Natural Disasters &ndash; Hurricane/Tornado</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Natural Disasters &ndash; Snow</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Loss of Electricity</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Loss of Electricity</TD>
			<TD ALIGN=CENTER>Damage to IT systems</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Loss of Heat</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Hardware Loss &ndash; Desk</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Hardware Loss &ndash; Server</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Hardware Loss &ndash; Laptop</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Fire</TD>
			<TD ALIGN=CENTER>Property Damaged</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Fire</TD>
			<TD ALIGN=CENTER>Property Destroyed</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Property Damaged</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Insurance</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Property Damaged</TD>
			<TD ALIGN=CENTER>Unable to use primary location</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Conduct Business offsite</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Property Destroyed</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Insurance</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Property Destroyed</TD>
			<TD ALIGN=CENTER>Unable to use primary location</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Conduct Business offsite</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Property Destroyed</TD>
			<TD ALIGN=CENTER>Loss of Files</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Scan each page before filing</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Loss of Assets (Desk etc)</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Insurance</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Loss or Theft of IT assets</TD>
			<TD ALIGN=CENTER>Risk of PIPEDA breach</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Encryption</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Communications sent to wrong recipient</TD>
			<TD ALIGN=CENTER>Risk of PIPEDA breach</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Process to double check recipient to material</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Pandemic</TD>
			<TD ALIGN=CENTER>Illness or Death of Employees</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>See Staff Loss &ndash; Death</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Pandemic</TD>
			<TD ALIGN=CENTER>Illness or Death of Clients</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Place Claim on behalf of Client/Estate</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Pandemic</TD>
			<TD ALIGN=CENTER>Increased cleaning requirements</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Increase Cleaning</TD>
			<TD ALIGN=LEFT>Increase Cleaning</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Pandemic</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; Virus/Malware</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; Virus/Malware</TD>
			<TD ALIGN=CENTER>Loss of Files</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; System Failure</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; System Failure</TD>
			<TD ALIGN=CENTER>Cost of Replacement</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; Unplanned Patches</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; Unplanned Patches</TD>
			<TD ALIGN=CENTER>Data Loss</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Backups</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; Theft of Data</TD>
			<TD ALIGN=CENTER>Risk of PIPEDA breach</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Cyber &ndash; Unauthorized Access</TD>
			<TD ALIGN=CENTER>Risk of PIPEDA breach</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Password Protection.  Inactivity Timeouts</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Loss of License</TD>
			<TD ALIGN=CENTER>Unable to conduct business</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Compliance &ndash; Audit</TD>
			<TD ALIGN=CENTER>Efforts to Prepare</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Compliance &ndash; Process Failure</TD>
			<TD ALIGN=CENTER>Risk of Fines</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Complaints</TD>
			<TD ALIGN=CENTER>Fines.  Loss of License</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Follow Processes</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Market Decline</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Illness</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Temporarily re-assign cases</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Disability</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Temporarily re-assign cases</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Death</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Permanent Re-assign cases</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Retirement</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Permanent Re-assign cases</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Termination &ndash; Productivity</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Permanent Re-assign cases</TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=17 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Termination for Cause &ndash; Malfeasance</TD>
			<TD ALIGN=CENTER>Need to review recent work for Compliance and Suitability</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Advisor Mentally Incapacitated</TD>
			<TD ALIGN=CENTER>Loss of Clients</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
		<TR>
			<TD HEIGHT=18 ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT>Staff Loss &ndash; Advisor Mentally Incapacitated</TD>
			<TD ALIGN=CENTER>Need to review recent work for Compliance and Suitability</TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=CENTER><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
			<TD ALIGN=LEFT><BR></TD>
		</TR>
	</TBODY>
</TABLE>

==Business Contingency==
===Steps===

Plan for worst case scenario and how to respond.
*test plan

===Elements===


*Purpose and scope. Your first task is to define the purpose and scope of the plan. ...
*Key business areas
*critical functions
*dependencies between business areas/functions
*Responsibilities. ...
*Plan invocation. ...
**What are the triggers
*Developing the BCP. ...
**Risk Mitigation
**Business Impact Assessment
*Stakeholders. ...
*Document owner, approver and change history. ...
*Change management.
**Document changes
***Record changes/dates/approvals
*Hard Copy as well as digital
*TEST
**Table top exercise
***Read through - looking for gaps
**Structured Walk Through
***rehearsal.  Role playing responsibilities.
**Disaster Simulation Test
***Dress Rehearsal

*Have a OPI
**Role
**Responsibilities
*Have an Emergency Communications Plan
**Key Contacts
**Messages
**Tracking communications and status

When discussing with partners make sure an NDA is in place.  Client Confidentiality.  [[PIPEDA]].  Competitive Benefit.

===Succession planning===
*transition plan

===Continuity Partner===


*does everyone in your family know what to do?  
*Is there a plan in place?  
*Do they know where they can find it?
Clients expect you as a business owner to take care of them.  They don't want to worry about what happens if you don't show up tomorrow.

Who is your continuity partner?
*Good fit
*Ability to take on clients
*Appropriately licensed etc.

Don't try to find another you - you are likely unique.  BUT find someone who has the same core values.

Goal of a crisis isn't just to survive but to thrive.  Plans in place help resiliancy.  Stabilize, Pivot, Grow.

The continuity plan is a form of insurance on your business.

Some day you will exit the business through intent or not.  Do you want to be in control of the exit?

There are lots of continuity plans on the internet.  They are usually HARD to create (from scratch) but easy to modify.

The longer the plan takes to implement the more likely clients do their own transition to other advisors

Only 3% of agents have a plan.  It is a value add to be able to advertise to clients/potential clients that you have one.

parkplaceadvisory.ca/crisismanagement
promo findbob




[[Category: Business]]
[[Category: KSFII]]
[[Category: FHS]]
[[Category: KSFP]]
[[Category: MLFT]]
[[Category: MLFCM]]
[[Category: FindBob]]
[[Category: Continuity Plan]]
[[Category: Hub]]

==Resilient Practice==
Continuity protects against the unplanned (i.e. not able to go into office).

Succession protects for planned (e.g. retirement).

Need to take care of Death/Disability before Succession!

Without a plan you are letting someone else make the decisions for your clients in the event of your disability/death.

===Things preventing having a plan===
#Perception that it is hard.

#Lack of human capital
##talent gap.
#Psychology
##Someone else will be working with my clients and it won't be me!
#Making it a priority.

To make it happen:
#Ask how we might make it easy?
#How do we find the talent to take over?
#Work on Emotional Intelligence skills
#Allocate time to work on it.

Firms can help.  Steps:
#Find out what tools are available
#Identify successors.
##Long term might be different than crisis.
#Negotiate the terms.
#Document
##A plan that isn't documented isn't a plan.
##Firm could/should have templates and agreements laid out.
#Review
##Plans should change as business evolves.

===Contingency===
*Length of absence
**6 months different story than 2 years.
*Staff and roles.  
**Does compensation change?
*Business expenses
**How is it funded
**Overhead insurance
*Review
**At least every 2 years.

===Continuity/Succession===

===Communication Plan===
*What clients will hear
*Who gets phone calls.  Who gets letters.
*Staff need to know the highlights of the plan, and where to find the documentation.

===Mistakes from planning for death/disability===
*Lack of communication
**How to contact
**HR/Payroll
**Spare Keys
**Day to Day running.

===Long Term Solution===
*Build a team
**Advisor of the future is the high performing team of today.
**Identify ideal client
**Identify ideal team member
***What abilities, skills, capabilities do they need
***What are the core values.
***Client philosophies

Solution doesn't need to be perfect.  
*Protect rather than perfect.
*A bad fit is better than no fit.

MGA might have match process.
*They should know the strengths and weaknesses of their advisors
*They should also have a wide view.

===Retirement vs Contingency===
Psych of exiting the business (retirement) is a big deal.

Wrapping in mortality makes it even more difficult.  People don't want to address it, so the plan gets shelved; they will get to it later.

Don't fail to plan for yourself.  If you can plan for your clients you can look after your own needs.

==Key Risks==
*Weather
**Hail
**Rain
**Heat
*Natural disasters
**flood
**earthquake
**tornado/Hurricane
**Avalanche
*Power Loss
*hardware loss
*illness etc
*Property Loss
**Fire
***Office/files
**Loss of Heat/Power
*pandemic
**Cleanliness
**Hygenic
*Cyber Attack
**Virus/Malware
**Theft
**System Failure
**Server Room issues
**Unexpected Patches and Updates
*Loss of License
*complaints
*privacy breach
*market decline
*advisor deemed mentally incapacitated
**no POA

===Mitigations===
***Insurance
***Warranties
***Backups
****Offsite
***AV software