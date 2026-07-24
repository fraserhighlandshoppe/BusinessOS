# bpPROC.pdf

```markdown
ebXML CC/BP Analysis Team

March 2001

1

2

3

ebXML Catalog of Common Business
Processes v1.0

4

Business Process Project Team
11 May 2001

5
6
7
8

1 Status of this Document

9
10

This Technical Report document has been approved by the Business Process Project Team and
has been accepted by the ebXML Plenary.

11

This document contains foundation material based on ebXML Technical Specifications or Reports.

12

Distribution of this document is unlimited.

13

The document formatting is based on the Internet Society’s Standard RFC format.

14

This version:

15

http://www.ebxml.org/specs/bpPROC.pdf

16
17
18

Latest version:
http://www.ebxml.org/specs/bpPROC.pdf

19

Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML CC/BP Analysis Team

20

March 2001

2 ebXML Participants

21
22

We would like to recognise the following for their significant participation to the development of this
document.

23

Business Process Project Team Co-Leads:

24

Paul Levine, Telcordia

25

Marcia McLure, McLure-Moynihan, Inc.

26

Editors:

27

Nita Sharma, Netfish Technologies

28

David Welsh, Nordstrom.com

29

Contributors:

30

Jim Clark, I.C.O.T.

31

David Connelly, OAG

32

Charles Fineman, Arzoon

33

Stephan de Jong, Philips International B.V.

34

Brian Hayes, Commerce One

35

David Welsh, Nordstrom.com

36

Rebecca Read, Mercator

37

William McCarthy, Michigan State University

38

Michael Rowell, OAG

39

Nita Sharma, Netfish Technologies

40

Jennifer Loveridge, Nordstrom.com

41

AIAG Members

42

ASC X12 EWG Members

43

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

2

ebXML CC/BP Analysis Team

44

March 2001

3 Table of Contents

45

1 Status of this Document............................................................................................. 1

46

2 ebXML Participants.................................................................................................... 2

47

3 Table of Contents....................................................................................................... 3

48

4 Introduction............................................................................................................... 4

49

4.1

Summary of Contents of Document .................................................................... 4

50

4.2

Audience........................................................................................................ 4

51
52
53
54

5 Design Objective........................................................................................................ 4
5.1

Objectives ....................................................................................................... 4

5.2

Goals ............................................................................................................. 4

6 Business Process Catalog Use Cases........................................................................ 5

55

6.1

Discovery of Business Processes....................................................................... 5

56

6.2

Cross References ............................................................................................ 5

57

6.3

Support Business Process Contextual Category................................................... 5

58

6.4

Discovery of Core Components.......................................................................... 5

59

6.5 Support Business Process Modeling.......................................................................... 6

60

7 The Common Business Process Catalog Overview..................................................... 6

61

7.1

What is a Common Business Process................................................................. 6

62

7.2

Catalog Categorization Scheme......................................................................... 7

63

7.3

Meta data for Cross Reference table................................................................... 8

64

7.4

Methodology for Building the Catalog.................................................................. 8

7.5

Registry and Repository for the Catalog .............................................................. 9

65
66

8 Catalog of Business Processes................................................................................ 11

67

8.1

Catalog of Common Business Processes with Cros s References ......................... 11

68

8.2

Catalog of Industry Specific Business Processes with Cross References ............... 48

69

8.3

Description of Common Business Processes ..................................................... 53

70

8.4

REA Table .................................................................................................... 54

71

8.5

Transactional View......................................................................................... 56

72

9 References.............................................................................................................. 60

73

10 Disclaimer............................................................................................................... 60

74

11 Contact Information................................................................................................. 60

75

Figures

76

Figure 6.5-1, Business Process Editor and Business Process Catalog................................. 6

77

Figure 7.1-1, Business Process Model Reuse.................................................................. 7

78

Figure 7.2-1, Graphical representation of the Porter Value Chain ........................................ 8

79

Figure 7.5-1, Common Business Process Development .................................................... 9

80

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

3

ebXML CC/BP Analysis Team

81

4 Introduction

82

4.1 Summary of Contents of Document

March 2001

83
84
85
86
87
88
89

This document puts together an initial list of common business process names, generic in nature
that can be used across various industries. This includes business processes with cross
references across common industry standards; including RosettaNet PIPs, X12, EDIFACT,
JiPDEC/CII(Center for information of Industry of JAPAN Information Processing Development
Center), OAG BOD, xCBL (CommerceOne). Identification of this catalog of common business
processes were influenced by various industry initiatives like RosettaNet, EIDX, CPFR, EIAJ, OAG
etc. This document also illustrates how to catalog business processes.

90
91
92
93

A Business Process consists of a set of business collaborations, which is itself composed of one or
more business transactions as defined by the UN/CEFACT Modeling Methodology (UMM)
Business Transaction View (BTV). The behavioral aspects of a business process are defined via
the UMM Metamodel.

94
95
96

The keywords MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT,
RECOMMENDED, MAY, and OPTIONAL, when they appear in this document, are to be
interpreted as described in RFC 2119 [Bra97].

97
98
99
100

4.2

Audience

The target audiences for this document includes business staff of both information and technical
background and specific business focus areas wishing to relate their electronic trading activities in
a consistent pattern to the general ebXML trading community.

101

5 Design Objective

102

5.1 Objectives

103
104
105
106
107
108
109

The primary objective of this catalog is to provide the e-business community with a list of business
process names and related information that are independent of any industry specifics. The generic
nature of these business processes enables one to reuse them with specific context and business
rules within different vertical industries. Common business processes have been grouped under
various classifications. Another objective of this catalog is to provide the corresponding references
to business documents and business processes defined across various industry standards.

5.2 Goals

110

The goals of the list of common business processes are:

111
112

n

This list will drive the creation of templates for each of these business processes that can be
reused across industries.

113
114

n

These processes are going to be the basis for discovery and definition of collaboration
patterns.

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

4

ebXML CC/BP Analysis Team

115
116

n

This catalog can evolve to become a global, industry neutral catalog of commonly used
processes with refinement and contribution from all sectors of the industries.

117

6 Business Process Catalog Use Cases

118

6.1 Discovery of Business Processes

119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138

March 2001

Given ebXML community growth, independent of industry sector, business processes commonly
used within industry will be developed according to the UMM and will be available for re-use via
business process catalogs hosted in ebXML compliant registries/repositories also called Business
Libraries. The catalog of common business processes can be used for the discovery of reusable
business processes in conjunction with Worksheets/Guidelines. Please refer to the figure 7.1.1.
The catalog supports discovering and comparing business processes in the early stages of
business process analysis. Common business processes in the catalog have associated process
specifications that include core components specific to it. Business process specification is a
declaration of the partners, roles, collaborations, choreography and business document exchanges
that make up a business process. A catalog of common business processes can be used as the
business process specifications for building business document(s) for similar business processes
within a specific context.

6.2 Cross References
This catalog provides informative cross-references to non-ebXML business processes and
business documents defined by electronic business standards organizations around the world. The
catalog can also be extended to include other industry specific common electronic trading
documents or business process conventions. This catalog will be stored in the business library.
When business process models/specifications are inserted into a business library they should be
cross-referenced against other industry standards.

6.3 Support Business Process Contextual Category

139

Business Process is one of the contexts defined by the ebXM L Core Components classification

140
141
142
143
144
145
146
147
148

scheme . A Business Process context relies on a classification derived from the list of common
business processes. The main reason to use context is to encourage reuse of core components,
and with it common documents and ultimately common business processes. By working from a
common set of core components and agreeing on the context for business processes, trading
partners can better understand what business information is required to be part of a Business
Process. The contextual categories, identified by ebXML Core Components, map to existing
elements and attributes within a business process model complying to the UMM. For example, the
contextual Category “Process” maps to the Metamodel elements BusinessProcess, ProcessArea,
and BusinessArea.

149
150
151
152
153

1

6.4 Discovery of Core Components
The catalog of common business processes is useful for discovery and analysis of core
components that will be used as the building blocks for deriving business documents within a given
context. This can be done by checking all sources of documents listed and cross-referenced on the
Common Business Process Catalog to identify a document that may have the information needed
1

see [ebCNTXT]for additional information on context

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

5

ebXML CC/BP Analysis Team

154
155
156
157
158
159
160
161
162
163

164
165
166
167
168
169
170

(which may be EDIFACT, X12, xCBL, RosettaNet PIPs, CII, OAG BODs). There may be an
existing document, which is similar and could be evaluated. Next identify if the document
components meet the business requirements. If so, then these components can be reused.

6.5 Support Business Process Modeling
Business processes are modeled by the information specified in the UN/CEFACT Modeling
Methodology (UMM) Metamodel. This metamodel specifies all the information that needs to be
captured during the business modeling of an electronic commerce based business process. With the
expansive potential of the UMM in all of it’s “intricate depth of detail”, people are advised to use tools
to help them model their business processes; and thus facilitate business analysis activities.

Figure 6.5-1, Business Process Editor and Business Process Catalog

When business experts model a business process using a “Business Process Editor” (BPE) tool
which could use the catalog of common business processes to discover existing business process;
ie. via a drop down list. A BPE would work with ebXML compliant registries/repositories. For further
reference, see Business Process and Business Document Analysis Definitions.

171

7 The Common Business Process Catalog Overview

172

7.1 What is a Common Business Process

173
174
175

March 2001

Common Business Processes are industry neutral and re-usable business processes. See Figure
7.1-1. Various components of a common business process specification can be re-used to create
new business processes. Re-use will typically occur at the business process, business
Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

6

ebXML CC/BP Analysis Team

March 2001

176
177

collaboration, business transaction, and business document model components. Refer to section
8.4 for a more detailed example.

178
179

Figure 7.1-1 has been revised to show the role of the Catalog of Common Business
Processes

Catalog
of Common Business Processes

Business Process
Reuse

Process Composition
/ Decomposition

C

Business Collaboration

Business Collaboration

a

Partner Types

Reuse

Roles

Business Transaction
Reuse

Figure 7.1-1, Business Process Model Reuse

7.2 Catalog Categorization Scheme

n

182

Business Transaction

Guard

o

180
181

Transition

gm
t C a o l mo
P r o c e s s

Choreography

183
184
185
186
187
188
189
190

The catalog’s categorization scheme is based upon an enterprise value chain, the concept
2
pioneered by Michael Porter , following review of several other reference models. A value chain is
a purposeful network of business processes designed to cumulatively transform a set of process
inputs into an output of greater value to the enterprise’s set of customers. Porter’s Value Chain
stages are illustrated in Figure 7.2 below as resource flows which progress from left to right in
transforming inputs as labor, capital, and goods into components of a business’s final product.
Figure 7.2 illustrates the linked major events within each process that consume business inputs
and produce business outputs.

191
192
193
194

Each business process in the Catalog of Common Business Processes is at the most general level
represented by a normative category of enterprise activities as procurement, financing, and
manufacturing. Normative category processes can be broken into normative sub-categories for
better business discovery.

195

Figure 7.2-1has been revised to show the normative categories in clearer font.

2

Michael E. Porter, Competitive Advantage : Creating and Sustaining Superior Performance, 1998, Harvard Business
School Press

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

7

ebXML CC/BP Analysis Team

March 2001

$$

$$

financing

raw materials

procurement
labor

transportation
human
resources

$$

labor
delivered raw
materials

labor
facilities, services
& technology

manufactured
goods
delivered
manufactured
goods

manufacturing
labor

procurement

marketing
& sales
customer service

196
197
198

product services

Figure 7.2-1, Graphical representati on of the Porter Value Chain

7.3 Meta data for Cross Reference table

199

The various components of this cross-reference of common business processes table:

200
201
202
203

Common Business Processes – A business process describes in detail how trading partners
take on roles, relationships and responsibilities to facilitate exchange of information. Common
Business processes are identified as commonly used across various organizations, industries or
other business entities.

204

Normative Category – Built from components of a Porter Value Chain.

205

Normative Sub-category – Decomposition of the Porter Component into logical sub groups

206
207

EDIFACT/X12/CII/OAG BOD/xCBL – Common industry standards used as a cross-reference, by
identifying their specific equivalent business documents commonly used today.

208
209
210

RosettaNet PIP – Common business processes cross-referenced to business transactions as
specified by RosettaNet Partner Interface Processes™ (PIPs™) which define business processes
between trading partners.

211
212
213
214
215
216

7.4 Methodology for Building the Industry-Neutral Catalog
With participation of business domain experts from major business communities and industry
standards organizations, there was consensus gathering with respect to current common practices
involved with electronic business trading. A comprehensive and consistent analysis needs to be
conducted for each “discovered” component by a domain-neutral technical assessment teams, to
further ensure cross-domain harmonization.

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

8

ebXML CC/BP Analysis Team

217
218
219
220
221
222
223
224
225
226
227
228

March 2001

7.5 Registry and Repository for the Catalog
The catalog of common business process names and associated cross-reference MAY be
stored in an ebXML Business Library and MAY be stored in other business libraries. There
can only be one catalog per ebXML registry. The Common Business Process catalog
owner needs to be an accredited global standards body such as UN/CEFACT, ITU, ISO.
The Catalog’s main service is to be shared by the global community. The catalog of
business process will be accessed through its registry interface. Business domain experts
within UN/CEFACT, perhaps also partnered with industry interest groups, need to define
and maintain each detailed specification for each common business process. The
classification/retrieval method for accessing the catalog will be defined in a
classification/retrieval mechanism.

BOLERO.NET

AIAG

EDIFACT

X12

SWIFT

Catalog of Common
Business Processes

OAG

OTHERS

Common Business
Process Specification

Specification for Common
Business Process

Global Repository

229
230

Figure 7.5-1, Common Business Process Development

231
232
233
234
235
236

In performing ebXML analysis activities to a business process, either establishing new business
processes or re-engineering existing ebXML business processes, it will be necessary to persist the
business process model. Business process analysis activities may call for many forms of
supporting information to aid in the analysis. It is desirable to maintain relationships with supporting
information and the ebXML business process model. Examples of supporting information include
technical drawings, design images and sound tracks in digital format.

237
238
239
240
241

Resource Description Framework (RDF) or XMI can be used to persist a Business Process model
in it’s complete UMM form, including other associated information resources that the business
users feel are significant to be kept associated with the business process model. A modeled
business process and supporting information registered in a catalog makes it accessible via its
reuseable components/artifacts.

242
243
244
245
246
247

Storing a modeled business process into the catalog needs to result in the business process to be
accessible via its reusable components/artifacts. Reusability can occur at various levels in the
UMM, however, reuse of artifact will likely be found at the business process, binary collaboration,
business transaction, and document levels of the UMM. Experience today strongly sugges ts that
reusability will often occur at the business transaction and document levels when compared to
traditional EDI.
Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

9

ebXML CC/BP Analysis Team

March 2001

248
249

ebXML compliant registry’s should satisfy the following Catalog of Common Business Process
service requirements towards business analysis activities :

250
251

A standard mechanism for registering catalogs so the catalog of common business processes can
be shared.

252
253

A standard mechanism for registering and storing Business Process and Information models (in
RDF or XMI) so that business processes may be discovered.

254

Catalog of Common Business Processes
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

10

ebXML BP/CC Analysis Team

255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271

March 2001

8 Catalog of Business Processes
This section contains several tables that represent various aspects of cataloging business processes. Each business process [should
represent/represents] a logically complete economic action or commitment. Some are atomic binary relationships that would be used as a Business
Transaction within a Binary Collaboration; some may encompass several transactions, and therefore would be used within ebXML as a higher-level
nested Collaboration.

The Section 8.1 identifies common business processes (used and being developed) that may or may not have traditional EDI documents available,
which do fit into the Value Chain classification schema. Here we take a Value Chain approach of classifying business processes, but recognize there
are many business and regulatory domains that may not appear immediately classified in the Value Chain classification. Section 8.2 shows an
example of the Insurance Industry, which can also be classified by its common business processes but cannot be categorized under the Value Chain
approach. So business processes may be categorized by the Porter’s Value Chain or other appropriate categorization scheme, perhaps specific to an
industry or company. Section 8.3 contains the definitions of the common business process as identified in Section 8.1. Section 8.4 is the REA
representation of the common business processes. To make this entire structure more concrete in the mind of catalog users, an illustrative table has
been included in this document. The illustrative table portrays: (1) each normative category, (2) its possible sub-categories, (3) its normal types of
resource inflows and outflows, (4) its major types of events that effect those flows, and (5) the normal types of agents and roles for those processes.

8.1 Catalog of Common Business Processes with Cross References

272
273

This section contains a list of common business process names and a cross-reference to various standards industry specific business process and
business document names.

274

Note: xCBL column removed from the following table
Common Business Normative
Processes
Category

Notification Of
Failure
∗

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Administration Failure
Notification

APERAK

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

PIP0A1

(CONFIRM BOD)

If document name not found in the latest official EDIFACT directory, it is a subset.

11

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Failure

Notification

Manage Product
Information
Subscription

Administration Product
Service Review

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

PIP1B1

065_update_productreq
_004,
067_cancel_productreq_
004
063_get_prodavail_003
064_show_prodavail_00
3
137_sync_pricelist_001
128_sync_catalog_001

Request/Verify
Account Info
Delete Party Profile

TUPREQ

Request Account Administration Party Profile
Setup

PARTIN

838

PIP1A1

007_sync_customer_004
008_sync_supplier_004
(plans to use ebXML
tpaML based work in
future)

Maintain Account Administration Party Profile

PARTIN

838

PIP1A2

007_sync_customer_004
008_sync_supplier_004

12

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

(plans to use ebXML
tpaML based work in
future)
Request Credit
Reference

Administration Party Profile

PIP1A3

025_get_credit_003,
026_show_credit_003,
027_update_credit_003

Maintain
Agreement

Administration Party
Agreement

007_sync_customer_004
,
008_sync_supplier_004

Request Quote /
Response

Procurement
Management

Pre-Order and REQOTE, 840, 843
Quote
QUOTES

PIP3A1

0310, 0311

152_sync_quote_002,
159_get_quote_002,
154_change_quote_002,
156_response_quote_00
2

Query Price And
Availability

Procurement
Management

Pre-Order and PROINQ, 879
Quote
AVLREQ,
TIQREQ

PIP3A2

137_sync_pricelist_001,
138_get_pricelist_001,
139_show_pricelist_001

Query Price

Procurement
Management

Pre-Order and
Quote
13

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

Management

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Quote

Query Availability Procurement
Management

Pre-Order and AVLREQ,
Quote
AVLRSP

Request Promise
Of Availablity

Procurement
Management

Pre-Order and AVLREQ,
Quote
AVLRSP

Price Catalog

Procurement
Management

Pre-Order and PRICAT
Quote

832

128_sync_catalog_001,
129_get_catalog_001,
130_show_catalog_001

Establishment Of Procurement
Contract Award
Management

Pre-Order and CONEST
Quote

Negotiate
Reservation

Procurement
Management

Pre-Order and RESREQ,
Quote
ITAREQ

Create Auction
Offer

Procurement
Management

Auction

836

003_process_po_005
(with appropriate PO
TYPE)
0210, 0211

NA

840, 843

Create Auction Bid

Bid Acceptance

14

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Barter Offer

Barter Acceptance

Haggle/Negotiation

Report Auction
Results

Procurement
Management

Auction

Check Credit

Procurement
Management

Payment Term DOCAPP, 460, 465,
Negotiation
DOCADV, 466
DOCINF

025_get_credit_003,
026_show_credit_003,
028_change_status_003

Establish Payment Procurement
Terms
Management

Payment Term Part of
Part of 850
Negotiation
create PO,
ORDERS

006_load_payable_005
003_process_po_005
(payment terms are on
the PO)
152_sync_quote_001
(payment terms are on
the quote)

Amend Payment
Terms

Procurement
Management

Payment Term DOCAMR, 469 Part of
Negotiation
DOCARE, Change PO,
Part of
860, 865

003_process_po_005
(payment terms are on
the PO)
15

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

ORDCHG, 860, 865
ORDRSP

Item Performance Procurement
History Request
Management

Forecast /
Planning

INVRPT

852

Item Performance Procurement
History Response Management

Forecast /
Planning

INVRPT

852

Create Sales/Order Procurement
Forecast
Management

Forecast /
Planning

DELFOR

830,

Identify Forecast
Exception

Procurement
Management

850
(blanket)

Forecast /
Planning

the PO)
152_sync_quote_001
(payment terms are on
the quote)

162_sync_plansched_00
2,
165_sync_seqsched_00
2
163_get_plansched_002,
164_show_plansched_0
02,
166_get_seqsched_002,
167_show_seqsched_00
2

Resolve Forecast Procurement
Exception
Management

Forecast /
Planning

163_get_plansched_002,
164_show_plansched_0

16

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

02,
166_get_seqsched_002,
167_show_seqsched_00
2
Create Shipping
Schedule For JIT
Delivery

Procurement
Management

Forecast /
Planning

168_sync_shipschd_002
,
169_get_shipschd_002,
DELJIT

830

Request Forecast Procurement
Information
Management

Forecast /
Planning

Obtain Future
Trend Analysis
Request

Procurement
Management

Forecast /
Planning

Obtain Future
Trend Analysis
Response

Procurement
Management

Forecast /
Planning

Obtain
Performance
History Request

Procurement
Management

Forecast /
Planning

INVRPT

846

Obtain
Procurement
Performance
Management
History Response

Forecast /
Planning

INVRPT

846, 852

170_show_shipschd_00
2

17

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

History Response
Issue Sales/Order Procurement
Forecast
Management

Forecast /
Planning

DELFOR

830, 850

Issue Raw Material Procurement
Authorization
Management

Forecast /
Planning

DELFOR

830, 850

Issue Fabrication
Authorization

Procurement
Management

Forecast /
Planning

DELFOR

830, 850

Identify Forecast
Exception

Procurement
Management

Replenishment DELJIT
/Scheduling

862, 866

Receive
Procurement
Acknowledgment Management
of Shipping
Schedule Delivery

Replenishment APERAK
/Scheduling

824

Issue Shipment
Authorization

Replenishment DELJIT
/Scheduling

862, 866

Resolve Forecast Procurement
Exception
Management
Issue Shipping
Schedule for
Delivery

Procurement
Management

Procurement
Management

Identify Schedule Procurement
Authorization
Management

Replenishment
/Scheduling

18

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Resolve Schedule Procurement
Exception
Management

Replenishment
/Scheduling

Issue Defect
Notification

Procurement
Management

Defect
Resolution

Issue Defect
Resolution Plan

Procurement
Management

Defect
Resolution

Receive
Resolution Plan
Acceptance

Procurement
Management

Defect
Resolution

Test Specification Procurement
Management

Test
Specification

Manage Purchase Procurement
Order
Management
(Create/Change/Ca
ncel and Accept
PO)

Procurement ORDCHG, 860, 852,
ORDERS, 850, 865,
ORDRSP 875, 876

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

PIP3A4

0410, 0411

004_Acknowledge_PO_0
05
056_Add_PO_005
058_Cancel_PO_005
057_Change_PO_004
010_Get_PO_005
054_Getlist_PO_004
055_List_PO_004
003_Process_PO_005

19

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

012_Receive_PO_004
011_Show_PO_005
092_Sync_PO_004
Create Order

Procurement
Management

Procurement ORDERS, 850, 855,
ORDRSP 865

PIP3A4

Change Order

Procurement
Management

Procurement ORDCHG 860

PIP3A4

057_Change_PO_004

Request Order

Procurement
Management

Procurement

Query Order
Status

Procurement
Management

Procurement OSTENQ, 869, 870
OSTRPT

PIP3A5

010_get_po_006,

850 (OBI)

011_show_po_005
054_getlist_po_005,
055_list_po_005

Distribute Order
Status

Procurement
Management

870

PIP3A6

011_show_po_006

Notify Of Purchase Procurement
Order Acceptance Management

Procurement ORDRSP 855

PIP3A7

004_acknowledge_po_0
06

Evaluate Supplier Procurement
Performance
Management

Procurement

Communicate
Supplier

Procurement

Procurement
Management

Procurement OSTRPT

501

20

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Performance

Management

Authorize
Fabrication

Procurement
Management

Authorize
Action

DELFOR

830

Authorize
Shipment

Procurement
Management

Authorize
Action

DELJIT

830

Authorize Raw
Material

Procurement
Management

Authorize
Action

DELFOR

830

Distribute
Despatch
Instructions

Procurement
Management

Transportation INSDES
and
Distribution

862, 858

PIP3B1

Notify Of Advance Procurement
Shipment
Management

Transportation DESADV
and
Distribution

856, 869

PIP3B2

Notify Of Shipment Procurement
Status
Management

Transportation IFTSTA, 114(Air),
PIP3B3
and
ORDSTA 214(Motor),
Distribution
315(Ocean),
404 (Rail
Carrier),
870

161_Show_shipment_00
3

Query Shipment
Status

Transportation IFTSTQ
and
Distribution

161_show_shipment_00
1

Procurement
Management

066_createprodorder_004

165_sync_shipschd_001

0520

213(Motor PIP3B4
Carrier),
313 (Ocean
Carrier),

165_sync_shipschd_001

21

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

0520

869

Change Shipment Procurement
Information
Management

Transportation RECON
and
Distribution

856

PIP3B5

Notify Of Transport Procurement
Exception
Management

Transportation
and
Distribution

854

PIP3B6

Create Delivery
Appointment

Transportation
and
Distribution

Procurement
Management

PIP3B7

Notify Of Shipment Procurement
Receipt
Management

Transportation RECADV
and
Distribution

861

Create
Transportation
Claim

Procurement
Management

Transportation
and
Distribution

Shipment
Instruction

Procurement
Management

Transportation IFTMIN
and
Distribution

304,
404,104,204
853

Booking
Confirmation

Procurement
Management

Transportation IFTMBC,
and
RESREQ
Distribution

301

PIP3B8

161_show_shipment_00
1

059_update_delivery_00
3

0540

PIP3B9

003_process_po_005
(instructions on PO line
and PO line schedule)

22

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Create Freight
Invoices

Procurement
Management

Transportation INVOIC,
and
IFTMCS
Distribution

Customs
Declaration
(International
Freight)

Procurement
Management

Transportation CUSDEC
and
Distribution

Material Safety
Data Sheet

Procurement
Management

SAFHAZ

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

110, 210,
310,410,810

161_show_shipment_00
1(Carried as part of the
Show Shipment)

848

Compliance Leak Procurement
Report
Management
Marine Inspection Procurement
Report
Management
Return Product

867

Procurement
Management

Return of
Goods

CREADV, 180,812
DEBADV

PIP3C1

Obtain Financing Procurement
Approval
Management

Payment

AUTHOR 828

PIP3C2

Match Invoice

Payment

Procurement
Management

0710, 0711,
0720, 0730

161_show_shipment_00
1
028_change_status_003,
027_update_credit_003

INVOIC

810, 819,
811

PIP3C3

0810, 0811,
0820, 0821

073_load_matchdoc_004
,
077_get_matchdoc_005,
078_Show_matchdoc_0
05

23

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Process Payment Procurement
Management

Payment

PIP3C4

0830, 0831

Distribute Risk
Analysis

Procurement
Management

Product
Configuration

PIP3D1

Distribute Test
Report

Procurement
Management

Product
Configuration

PIP3D2

Distribute Test
Result

Procurement
Management

Product
BMISRM
Configuration

Request Product
Acceptance

Procurement
Management

Product
Configuration

PIP3D11

Distribute
Engineering
Change Request

Procurement
Management

Product
Configuration

PIP3D12

REMADV, 820, 824,
PAYORD, 823, 827,
DIRDEB, 185, 813
FINSTA,
BANSTA

863

PIP3D10

107_sync_engchgorder_
002,
108_get_engchgordr_00
2,
109_show_engchgorder
_002

Distribute
Procurement
Engineering
Management
Change Response

Product
Configuration

PIP3D13

107_sync_engchgorder_
002,

24

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Change Response

108_get_engchgordr_00
2,
109_show_engchgorder
_002

Request
Engineering
Change Order
Approval

Procurement
Management

Product
Configuration

PIP3D14

107_sync_engchgorder_
002,
108_get_engchgordr_00
2,
109_show_engchgorder
_002

Notify Of
Engineering
Change Order

Procurement
Management

Product
Configuration

PIP3D15

110_confirm_engchgord
er_002

Notify Of
Engineering
Change
Implementation
Plan

Procurement
Management

Product
Configuration

PIP3D16

110_confirm_engchgord
er_002

Notify Of Solution Procurement
Configuration
Management

Product
Configuration

PIP3D2

110_confirm_engchgord
er_002

Notify Of
Manufacturing
Specification

Product
Configuration

PIP3D3

110_confirm_engchgord
er_002

Procurement
Management

25

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

Request Build
Authorization

Procurement
Management

Product
Configuration

PIP3D4

Distribute Material Procurement
Status
Management

Product
Configuration

PIP3D5

Notify Of Build
Readiness

Procurement
Management

Product
Configuration

PIP3D6

Request Deviation Procurement
Or Waiver
Management

Product
Configuration

PIP3D7

Distribute Work In Procurement
Process
Management

Product
Configuration

PIP3D8

033_update_wipconfirm
_004

Query Work In
Process

Procurement
Management

Product
Configuration

PIP3D9

031_get_wipconfirm_003

Distribute New
Product
Information

Product
Introduction

Preparation for
Distribution

Query Product
Information

Product
Introduction

625

CII
OAG BODs
(HWSW001A)

061_show_item_004

032_show_wipconfirn_0
04
832

PIP2A1

0110

140_sync_itemspecs_00
1
142_show_itemspecs_0
01

Preparation for TIQREQ
Distribution

893, 620

PIP2A2

141_get_ite mspecs_001,
142_show_itemspecs_0
01,
100_get_item_003,

26

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

101_show_item_003
Query Marketing
Information

Product
Introduction

Preparation for
Distribution

PIP2A3

141_get_itemspecs_001,
142_show_itemspecs_0
01,
139_show_pricelist_001,
138_get_pricelist_001,
135_get_itemxref_001,
136_show_itemxref_001

Query Sales
Product
Promotion And
Introduction
Rebate Information

Preparation for
Distribution

889

PIP2A4

Query Technical
Information

Product
Introduction

Preparation for
Distribution

841

Query Product
Lifecycle
Information

Product
Introduction

Preparation for
Distribution

PIP2A6

Request Product
Discontinuation
Information

Product
Introduction

Preparation for
Distribution

PIP2A7

141_get_itemspecs_001,
142_show_itemspecs_0
01

PIP2A5

141_get_itemspecs_001,
142_show_itemspecs_0
01
141_get_itemspecs_001,
142_show_itemspecs_0
01
141_get_itemspecs_001,
142_show_itemspecs_0
01
27

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

01
Distribute Product Product
Stock Keeping
Introduction
Unit (SKU)

Preparation for
Distribution

Change Product
Information

Product
Introduction

Product
Change
Notification

Change Marketing Product
Information
Introduction

PIP2A8

134_sync_itemxref_001
136_show_itemxref_001

TUPREQ, 888
SKDUPD

PIP2B1

065_update_productreq
_004

Product
Change
Notification

PIP2B2

140_sync_itemspecs_00
1,

Change Sales
Product
Promotion And
Introduction
Rebate Information

Product
Change
Notification

PIP2B3

137_sync_pricelist_001

Change Product
Technical
Information

Product
Introduction

Product
Change
Notification

PIP2B4

Change Product
Lifecycle
Information

Product
Introduction

Product
Change
Notification

PIP2B5

140_sync_itemspecs_00
1

140_sync_itemspecs_00
1
061_sync_item_004

134_sync_itemxref_001,

28

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

Query Optional
Product
Information

Product
Introduction

Product
Change
Notification

PIP2B6

Distribute
Inventory Report

Procurement
Management

Inventory
Reporting

Distribute
Inventory Tieout
Report

Procurement
Management

Inventory
Reporting

PIP4C2

Distribute
Inventory Error
Notification

Procurement
Management

Inventory
Reporting

PIP4C3

Distribute
Procurement
Inventory Tie-Out Management
Discrepancy
Report

Inventory
Reporting

PIP4C4

Warehouse Stock Procurement
Transfer Receipt Management
Advice

Inventory
Reporting

Warehouse Stock Procurement
Transfer Shipment Management
Advice

Inventory
Reporting

943

Notify Of
Procurement
Commercial Sales Management
Report

Sales
Reporting

SLSRPT, 867
STLRPT

CII
OAG BODs
(HWSW001A)

135_get_itemxref_001,
136_show_itemxref_001

INVRPT

846

PIP4C1

068_sync_inventory_005
,

022_get_countinfo,
023_show_countinfo

RECADV

944

036_show_picklist_005
037_update_picklist_005
036_show_picklist_005
037_update_picklist_005
PIP4E1

089_getlist_salesorder_0
05

29

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

090_list_salesorder_005
Notify Of
Consumer Sales
Report

Procurement
Management

Notify Of Tieout
Sales Report

Procurement
Management

Sales
Reporting

PIP4E2

089_getlist_salesorder_0
05
090_list_salesorder_005

Sales
Reporting

PIP4E3

089_getlist_salesorder_0
05
090_list_salesorder_005

Request Detail
Sales Tieout
Report

Procurement
Management

Sales
Reporting

PIP4E4

089_getlist_salesorder_0
05
090_list_salesorder_005

Distribute
Procurement
Commercial Sales Management
Report Error
Notification

Sales
Reporting

Notify Of
Consumer Sales
Report For
Affected Errors

Procurement
Mana gement

Sales
Reporting

Distribute
Consumer Sales
Report Error
Notification

Procurement
Management

Sales
Reporting

PIP4E5

089_getlist_salesorder_0
05
090_list_salesorder_005

PIP4E6

30

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

Price Protection

Procurement
Management

Price
Protection

PIP4F

Ship From Stock
And Debit_Credit

Procurement
Management

Ship from
Stock and
Debit_Credit

Procurement
Management

Regulatory_Ro
yalty

Create Invoice
(Products)

Financial

Financial

Create Invoice
(Services)

Financial

Financial

811

Receive Payables Financial

Financial

820

Originate Payables Financial

Financial

820

Receive
Receivables

Financial

Financial

820, 823

Originate
Receivables

Financial

Financial

820

Originate Child
Fina ncial
Support Payments

Financial

820

Originate Payroll

Financial

Financial

820

Originate Tax
Payments

Financial

Financial

820

CII
OAG BODs
(HWSW001A)

161_show_shipment_00
3

185, 813

INVOIC

810

076_load_plinvoice_003

006_load_payable_005

31

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Payments
Originate Royalty Financial
Payments

Financial

820

Acknowledge a
Payment Order

Financial

Financial

824

Confirm/Verify
Payment Orders

Financial

Financial

831

Notify Party of
Financial
Returned payment
Item

Financial

827

Request Payment Financial
Cancellation

Financial

829

Process Lockbox Financial

Financial

823

Cash
Reconciliation
(Asset)

Financial

Financial

821

Cash
Reconciliation
(Liability)

Financial

Financial

821

Send Debit
Authorization

Financial

Financial

828

Issue a Check
Issuance List

Financial

Financial

828

32

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Issuance List
Transmit Business Financial
Credit Information

Financial

155

Transmit Real
Estate Title
Information

Financial

Financial

197

Request Loan
Information

Financial

Financial

198

Transmit Loan
Information

Financial

Financial

198

Transmit Real
Financial
Estate Settlement
Information

Financial

199

Report Mortga ge Financial
Credit Information

Financial

200

Transmit Uniform Financial
Residential Loan
Application

Financial

201

Transmit Mortgage Financial
Loan Information

Financial

202

Transmit Mortgage Financial
Note Information
and

Financial

205

33

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Characteristics
Transmit Mortgage Financial
Service
Information

Financial

203

Transmit Real
Estate Site
Inspection
Information

Financial

Financial

206

Transmit Property Financial
Tax Information

Financial

245

Transmit
Financial
Collection Account
Assignments

Financial

248

Report Collection Financial
Account Status
Inquiries

Financial

248

Apply for
Financial
Mortgage
Insurance Benefits

Financial

260

Request Real
Financial
Estate Information

Financial

261

Report Real Estate Financial
Information

Financial

262

34

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Respond to a
Residential
Mortgage
Insurance
Application

Financial

Financial

263

Mortgage Loan
Default Status
Report

Financial

Financial

264

Order Real Estate Financial
Title Insurance
Services

Financial

265

Notify Parties of
Mortgage or
Property Record
Change

Financial

Financial

266

Transmit a
Debit/Credit
Adjustment

Financial

Financial

812

Request/Respond Financial
Financial Action

Financial

814

Transmit Billing
and Operating
Expense Details

Financial

Financial

819

Transmit Account Financial
Analysis

Financial

822

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

35

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Information
Order for Mortgage Financial
Credit Information

Financial

833

Request Account Financial
Adjustment Action

Financial

844

Respond to a
Financial
Request for
Account
Adjustment Action

Financial

849

Apply for
Residential
Mortgage
Insurance

Financial

Financial

872

Invoice for Grocery Financial
Products

Financial

880

Create Payroll

Financial

Financial

040_update_persontime
_003

Issue
Ticket/Voucher

TKTREQ,
TIKTRES

Exchange/Reissue
Ticket

TKTREQ,
TKTRES

Refund Ticket

TKTREQ,
TKTRES

36

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Void Ticket

CII
OAG BODs
(HWSW001A)

TKTREQ,
TKTRES

Request Payment Financial
Status

Financial

REMADV 820

Request Payment Financial

Financial

REMADV 820

Customs
Declaration
(Shipper)

RosettaNet
Partner
Interface
Process

Transportation Declaration of CUSDEC
and Logistics Goods and
Transportation

161_show_shipment_00
3,
003_process_po_006,
084_sync_salesorder_00
5 (Customs declarations
can be carried on each
of these.)

Shipping Line To
Customs –
(Carrier)

Transportation Declaration of CUSCAR
and Logistics Goods and
transportation

161_show_shipment_00
3,
003_process_po_006,
084_sync_salesorder_00
5 (Customs declarations
can be carried on each
of these.)

Environment
Transportation Declaration of IFTDGN
Health And Safety and Logistics Goods and
Declaration
transportation

161_show_shipment_00
3,
003_process_po_006,

37

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

084_sync_salesorder_00
5 (Customs declarations
can be carried on each
of these.)
Export And Import Transporta tion Declaration of
Declaration
and Logistics Goods and
transportation

161_show_shipment_00
3,
003_process_po_006,
084_sync_salesorder_00
5 (Customs declarations
can be carried on each
of these.)

Import Side
Transportation Declaration of
Compliance Check and Logistics Goods and
transportation

161_show_shipment_00
3,
003_process_po_006,
084_sync_salesorder_00
5 (Customs declarations
can be carried on each
of these.)

Voyage Itinerary / Transportation Declaration of
Schedules
and Logistics Goods and
transportation

161_show_shipment_00
3,
003_process_po_006,
084_sync_salesorder_00
5 (Customs declarations

38

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

can be carried on each
of these.)
Request For
Transportation Declaration of
Compliance
and Logistics Goods and
Screening
transportation
(Solvency Check)

161_show_shipment_00
3,
003_process_po_006,
084_sync_salesorder_00
5 (Customs declarations
can be carried on each
of these.)

Announce Arrival Transportation Inbound
Of Vessel/Vehicle and Logistics Transport (at
international
port)
Entry Of Cargo

Transportation Inbound
and Logistics Transport (at
international
port)

161_show_shipment_00
3

COARRI

Pickup / Pre Transportation Inbound
carriage Of Goods and Logistics Transport (at
At Origin
international
port)

161_show_shipment_00
3

Announce
Departure Of
Vessel / Vehicle

161_show_shipment_00
3

Transportation Outbound
and Logistics Transportation
(at
international

39

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

port)
Departure Of
Cargo

Transportation Outbound
CODECO
and Logistics Transportation
(at
international
port)

Onward Carriage Transportation Outbound
Of Cargo To Final and Logistics Transportation
Destination
(at
international
port)

161_show_shipment_00
3

Vessel / Vehicle
Arrival Planning

Transportation Operation (at
and Logistics international
port of call)

161_show_shipment_00
3

Vessel / Vehicle
Departure
Planning

Transportation Operation (at
and Logistics international
port of call)

161_show_shipment_00
3

Vessel / Vehicle
Discharge
Operation

Transportation Operation (at
and Logistics international
port of call)

Vesse l / Vehicle
Load Operation

Transportation Operation (at
and Logistics international
port of call)

Cargo Relay
Operation

Transportation Operation (at
and Logistics international

BAPLIE

40

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

Operation

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

and Logistics port of call)

Customs
Transportation Clearance
Clearance Of
and Logistics
Cargo For Export

161_show_shipment_00
3

Customs
Transportation Clearance
Clearance Of
and Logistics
Cargo For Import

161_show_shipment_00
3

Health And Safety Transportation Clearance
Clearance Of
and Logistics
Cargo

161_show_shipment_00
3

To-Be-Determined Transportation G. Cross
and Logistics Border Return
Handling
Manage Sales
Lead

Marketing
Management

Marketing
Campaign
Management

PIP5A1

Transfer Sales
Lead
Responsibility

Marketing
Management

Marketing
Campaign
Management

PIP5A2

Query Sales Lead Marketing
Status
Management

Marketing
Campaign
Management

PIP5A3

087_change_salesorder
_006 (Carries sales lead
responsible for the
order.)

41

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

Notify Of Sales
Lead Status

Marketing
Management

Marketing
Campaign
Management

PIP5A4

Distribute
Marketing
Marketing Activity Management
Information

Marketing
Campaign
Management

PIP5B1

Notify Of
Marketing
Marketing Activity Management

Marketing
Campaign
Management

Create Sales
Marketing Claim

Marketing
Management

Marketing
Campaign
Management

Process Sales
Marketing Claim

Marketing
Management

Marketing
Campaign
Management

PIP5B2

Change Sales
Marketing Claim

Marketing
Management

Marketing
Campaign
Management

PIP5B3

Notify Of Cancel
Sales Marketing
Claim

Marke ting
Management

Marketing
Campaign
Management

PIP5B4

Query Sales
Marketing Claim
Status

Marketing
Management

Marketing
Campaign
Management

PIP5B5

CII
OAG BODs
(HWSW001A)

42

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Notify Of Sales
Marketing Claim
Status

Marketing
Management

Marketing
Campaign
Management

PIP5B6

Distribute Product Marketing
List
Management

Design Win
Management

PIP5C1

Request Design
Registration

Marketing
Management

Design Win
Management

PIP5C2

Request Design
Win

Marketing
Management

Design Win
Management

PIP5C3

Distribute
Marketing
Registration StatusManagement

Design Win
Management

PIP5C4

Query Registration Marketing
Status
Management

Design Win
Management

PIP5C5

Request Ship
From Stock And
Debit
Authorization

Marketing
Management

Ship from
Stock and
Debit

PIP5D1

019_confirm_issue_005

Notify Of Blanket
Ship From Stock
And Debit
Authorization

Marketing
Management

Ship from
Stock and
Debit

PIP5D2

161_show_shipment_00
3

Distribute Open
Ship From Stock
And Debit

Marketing
Management

Ship from
Stock and
Debit

PIP5D3

43

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Common Business Normative
Processes
Category

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

Authorization
Status

Debit

Query Ship From Marketing
Stock And Debit
Management
Authorization
Status

Ship from
Stock and
Debit

PIP5D4

Create Ship From Marketing
Stock And Debit
Management
Claim

Ship from
Stock and
Debit

PIP5D5

Notify Of Ship
Marketing
From Stock And Management
Debit Claim Status

Ship from
Stock and
Debit

PIP5D6

CII
OAG BODs
(HWSW001A)

028_change_status_003

Product Request Product
Needs
PROINQ
(Internal / External Development Determination
– All Sources)

841, 244

Request
Evaluation
(Research)

841

143_sync_rfq_002

Evaluation Results Product
Needs
PRODAT 841
Development Determination

143_syn_rfq_002,

Gather And
Document
Information

143_sync_rfq_002

Product
Needs
Development Determination

Product
Requirements GENRAL 841
Development Definition

151_show_rfq_002

44

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

Analyze
Information

Product
Requirements
Development Definition

Develop
Functional
Specifications

Product
Requirements
Development Definition

Develop Technical Product
Design
Specifications
Development Product
Design Tooling

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

PRODAT 841

Product
Design
Development Product

841

150_get_rfq_002,
151_show_rfq_002,
144_add_rfq_002,
146_cancel_rfq_002

Design Process
(Routing)

Product
Design
Development Product

PROTAP

841

150_get_rfq_002,
151_show_rfq_002,
144_add_rfq_002,
146_cancel_rfq_002

Establish Product Product
Design
Configuration
Development Product
(BOM)

PRODAT 841

Production
Planning

145_change_rfq_002

145_change_rfq_002

45

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

Initiate
Manufacturing
Order

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

CII
OAG BODs
(HWSW001A)

Product
Manufacturing ORDERS 830
Manufacturing

Setup Production Product
Manufacturing
Line (Tooling)
Manufacturing

145_change_rfq_002

145_change_rfq_002

Get Materials (RM / Product
Manufacturing
Component Parts / Manufacturing
MRO)
Produce Product

Product
Manufacturing
Manufacturing

Inspect Incoming Product
Quality
Material (Tooling, Manufacturing Assurance
RM, Components)

INSRPT,
INSREQ

863

Inspect WIP

Product
Quality
Manufacturing Assurance

INSRPT,
INSREQ

863

Inspect Finished
Goods

Product
Quality
Manufacturing Assurance

INSRPT,
INSREQ

863

Test
Product
Quality
Product/Process Manufacturing Assurance
Characteristics
(RM, Components,
Finished Goods)

QALITY

863

Report Test
Results / Non-

QALITY,
INSRPT

863, 842

Product
Quality
Manufacturing Assurance

46

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common Business Normative
Processes
Category

March 2001

Normative Sub EDIFACT X12
Category
including including
sub-sets∗ sub-set∗

RosettaNet
Partner
Interface
Process

conformance /
Scrap / Rework /
Certifications

Manufacturing Assurance

Provide And
Administer Asset
Management

Service
Support

Provide and
Administer
Warranties,
Service
Packages, and
Contracted
Services

PIP6A1

Technical Support Service
And Service
Support
Management

Provide and
Administer
Warranties,
Service
Packages, and
Contracted
Services

PIP6C1
PIP6C2
PIP6C3
PIP6C4

Provide and
Administer
Asset
Management

PIP6B1

Service
Support

CII
OAG BODs
(HWSW001A)

INSRPT

47

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

275
276
277

8.2 Catalog of Industry Specific Business Processes with Cross References
Note: xCBL column removed from the following table

278
279

Common

Category

Sub Category

Business

EDIFACT
including subsets

X12 including
sub-sets

Processes

xCBL 3.0 RosettaNet Partner OAG BODs
Interface
Process

Declare Lien

Insurance

Administration

IPPOAD

Accept Lien

Insurance

Administration

IPPOAD

Change Insurer

Insurance

Cancellation

IPPOAD

Claims Recovery Request Insurance

Cancellation

IPPOAD,
(Other TBD)

Claims Recovery
Acceptance

Insurance

Cancellation

IPPOAD,
(Other TBD)

Loss Advice

Insurance

Claims

IFTICL

Solicitor Instruction /
Report

Insurance

Claims

ICSOLI

Claims Settlement /
Agreement / Invoice

Insurance

Claims

IFTICL,
ICASRP

272, 148

276, 810, 811

48

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common

March 2001

Category

Sub Category

Business

EDIFACT
including subsets

X12 including
sub-sets

Processes

xCBL 3.0 RosettaNet Partner OAG BODs
Interface
Process

Loss Adjustment

Insurance

Claims

IFTICL

Payment Rejection

Insurance

Claims

ICASRP

824

Claims Payment

Insurance

Claims

PRPAID

820, 835

Claims Survey Request

Insurance

Claims

IFTICL,
ICASRP

Claims Survey Report

Insurance

Claims

IFTICL,
ICASRP

Claims Recovery /
Subrogation Request

Insurance

Claims

ICASRP

272

Claims Re covery/
Subrogation Response

Insurance

Claims

ICASRP

272

Authorization for Vendor
Services on a Claim

Insurance

Claims

ICASRP

272

Change / Cancel
Authorization for Vendor
Services

Insurance

Claims

272, 824

Intermediary System
Insurance
Authority Update Request

System Services

ISENDS

Intermediary System
Authority Update Accept

System Services

ISENDS

Insurance

49

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common

March 2001

Category

Sub Category

Business

EDIFACT
including subsets

X12 including
sub-sets

Processes
Support Application for
Admission

xCBL 3.0 RosettaNet Partner OAG BODs
Interface
Process

Student Record

Transcript/Student
Record Transfer

130

Update Enrollment Status Student Record

Transcript/Student
Record Transfer

130

Support Application for
Employment

Student Record

Transcript/Student
Record Transfer

130

Provide Transfer Credit
Validation

Student Record

Transcript/Student
Record Transfer

130

Transfer Student Record Student Record

Transcript/Student
Record Transfer

130

Support Licensing
Application

Student Record

Transcript/Student
Record Transfer

130

Authenticate Sender of
Transcript

Student Record

Transcript
Acknowledgment

131

Reconcile Transcript Data Student Record

Transcript
Acknowledgment

131

Request Delivery of
Transcript

Student Record

Request Transcript

146

Respond to Transcript
Request

Student Record

Request Response

147

Transfer of Test
Score and Related

138

Support Application for
Test Score Report
Admission to Educational

50

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common

March 2001

Category

Sub Category

Business

EDIFACT
including subsets

X12 including
sub-sets

Processes

xCBL 3.0 RosettaNet Partner OAG BODs
Interface
Process

Institution

Information

Support Application for
Employment

Test Score Report

Transfer of Test
Score and Related
Information

138

Support Licensing
Application

Test Score Report

Transfer of Test
Score and Related
Information

138

Update Testing Service
Information

Test Score Report

Transfer of Test
Score and Related
Information

138

Create a Prospective
Student Record

Prospective Student Transfer of
Report
Prospective Student
Information

138

Update a Prospective
Student Record

Prospective Student Transfer of
Report
Prospective Student
Information

138

Transfer Application Data Admission of
Students

Admission
Application
Processing

189

Report Student Status
Confirmation

Enrollment
Verification

190

Degree Verification

190

Student Status
Certification

Confirm Degree Awarded

51

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Common

March 2001

Category

Sub Category

Business

EDIFACT
including subsets

X12 including
sub-sets

Processes

xCBL 3.0 RosettaNet Partner OAG BODs
Interface
Process

Distribute Course
Information

Course Catalog

188

Request Course
Information

Course Catalog

188

Report Staff Profile

Human Resources

Staffing Information

Report Staff Assignments

132
132

Report Institution
Description

Institutional
Characteristics

Institution
Information

133

Report Institution
Enrollment

Institutional
Characteristics

Institution
Information

133

Report Institutional
Student Profile

Institutional
Characteristics

Institution
Information

133

280

52

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

281
282
283
284

March 2001

8.3 Description of Common Business Processes
Each common business process identified in the catalog will contain detailed descriptions in this section. This definition will identify the roles,
transaction and documents involved in this process. Currently the table has limited descriptions and will grow as domain experts define the business
process specifications. This table is intended to be illustrative only, not exhaustive
Business Process

Definition

Request For Quote

The Request Quote allows a Buyer to request a product quote from a Seller. The Seller may return a quote, or a referral
to another Seller. The Buyer has the option of requesting a quote from the referral.
Quotes may involve:
*One or more items. * Fixed price quotes or negotiated prices. *Configurable or standalone product.

Query Price And Availability

Partners can query the price and availability of products from other partners that supply products in the supply chain.
This query contains both the specification of a request for information and a specification of how that information must be
returned to the requestor. (The information must be returned in tabular format in the order specified by the select part of
the query.)

Manage Purchase Order

The purchase order management process comprises the creation, change and cancellation of a purchase order. A Buyer
or buying organization initially creates a purchase order and sends the request to fulfil the order to a Seller. The Seller
acknowledges acceptance of the purchase order by returning a substantive purchase order acceptance Business
Document. A Buyer can then initiate a purchase order change or cancel the purchase order.

Query Order Status

The status of a product order is requested after a purchase order is created. The status of a purchase order informs a
requesting partner of the fulfilment and shipping status of the products in the order. For example, products in the
purchase order request may be backordered, shipped, or the entire purchase order may have been cancelled.

Distribute Order Status

The status of a product order is distributed on an unsolicited basis after a purchase order is created. The status of a
product order informs a Buyer of the fulfillment and/or shipping status of the products in the order. For example, products
in the purchase order request may be backordered, shipped or the entire purchase order may have been canceled

Distribute New Product
Information

The process for distributing new product information to Buyers so that enterprise systems can be established to accept
product orders, and for product information users to populate the Buyer’s online sales catalogs.

53

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

Two categories of product information are listed below.
1.

Sales catalog information typically used to promote products to non-technical customers. Sales catalog
information can include quantities, prices and marketing information.

2.

Technical specifications that are used to promote products to technical products and to create content for
configuration catalogs. Technical specifications only comprise the qualitative and quantitative properties.

Product information is typically exchanged to partners who have subscribed for new announcements.
285
286
287
288
289
290
291
292

8.4 REA Table
This table illustrates the normative categories and subcategories of an enterprise as envisioned in the value chain model of Michael Porter. It also
includes columns for illustrative REA (Resources-Events-Agent) components of the BRV layer of the UMM metamodel. The table portrays: (1) each
normative category, (2) its possible sub-categories, (3) its normal types of resource inflows and outflows, (4) its major types of events that effect those
flows, and (5) the normal types of agents and roles for those processes. This table is intended to be illustrative only, not exhaustive. The table also
includes an entry for an Administration category, a component not shown on the resource flow figure

Normative Category

Normative Sub-Category

Resource inflows & outflow

Major types of events

Economic Agents &
Roles

Procurement

Bid Submission

Money

Payments

Buyer

Contract Negotiation

Raw materials

Purchase

Seller

Purchase Order Preparation

Facilities

Purchase Orders

Vendor

Receiving

Services

Price Quotes

Cashier

Technology

Contract Negotiation

Money

Cash Payments

Human Resources

Hiring

Employee

54

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Normative Category

March 2001

Normative Sub-Category

Resource inflows & outflow

Major types of events

Economic Agents &
Roles

Training

Purchased training materials

Acquisition of labor

Student

Payroll Management

Purchased benefit packages

Training

Beneficiary

Loading

Raw Materials

Shipment

Buyer

Shipping

Delivered Raw Materials

Warehousing Tasks

Vendor

Packaging

Manufactured Goods

Material Handling

Logistics Worker

Delivered Manufactured Goods

Trucking

Trucker

Product Development

Facilities & Technology

Manufacturing Operation

Factory Worker

Product Design

Labor

Raw Material Issue

Supervisor

Assembly

Raw Materials

Manufacturing Job

QC Inspector

Quality control

Finished Goods

Advertising Use & Campaigning

Labor

Cash Payment

Customer

Marketing Management

Advertising Service

Customer Invoice

Salesperson

Sales Calling

Delivered Goods

Sale Order

Cashier

Customer Credit Management

Product Services

Price Quotes

Cash

Contract Negotiation

After Sales Service

Labor

Service Call

Warranty Construction

Purchased Services

Product Repair

Personnel Deployment
Transportation

Manufacturing

Marketing & Sales

Customer Service

Customer Service
Agent

55

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

Normative Category

Financing

Administration

March 2001

Normative Sub-Category

Resource inflows & outflow

Major types of events

Economic Agents &
Roles

Product Warranties & Services

Service Contract

Customer

Loan Management

Cash

Interest Payments

Stockholders

Stock Subscriptions and Sales

Bonds

Stock Subscriptions

Bond Holders

Dividend Policy

Stocks

Dividend Declarations

Investment Brokers

Derivative Instruments

Cash Receipts

Financial Managers

Employee Labor

Employee Service

Managers

Management Projects

Clerks

Accounting
Financial Reporting
Executive Management

293
294
295
296
297
298
299
300
301

8.5 Transactional View
This section and table depicts examples and illustrates the use of common business processes identified in the catalog, as business processes, binary
collaborations and business transactions within a specific hypothetical business process. That process is certain simple economic relationships
between a dotcom retailer (partner type "Retailer") and a drop ship vendor (partner type "DSVendor"), in the hypothetical Business Area "Direct to
Customer Retail", described in the exemplary use case used in Sections 7 and 8 of the Business Process Analysis & Worksheets. The table below
contains the essential metamodel element values for the business processes.

302

56

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

March 2001

A Business Transaction is an exchange of Business Documents between two parties. This table shows one row per Business Transaction.
All Business Transactions MUST be contained in a two-party Binary Collaboration. CPAs are associated with each Binary Collaboration: the Process Specification Digest in a CPA points to a
particular Authorized Role, and therefore to a particular Business Transaction, within a Binary Collaboration. A Binary Collaboration MUST contain one or more Business Transaction, which in the
aggregate MUST use only two Partner Types. One or more Binary Collaborations MAY be aggregated (nested) into composite Collaborations which MUST use two Partner Types and MAY use more
than two.
• A Business Process is a Collaboration (aggregated at any level) referenced as a whole process by an ebXML registry. This entire table may be defined as one Business Process. Partner types are
assigned to persistent roles within a Business Process.
• Authorized Roles are assigned to each of the two roles in each Business Transaction. Each MUST be unique within a Business Process. It is RECOMMENDED that Authorized Roles be named to
facilitate resource discovery, by creating unique composite values from a controlled vocabulary. There is no normative rule for generating the names. In this table, we have used a hypothetical
controlled vocabulary which includes "Buyer, Seller, Shipper, Carrier, Shipment Receiver, Payor, Payee, Debtor, Creditor, Credit Service, Reporter, Report Receiver", to promote resource discovery and
re-use. We have elected to use the Business Transaction names (and, where necessary, Collaboration names) to qualify and distinguish them.
•
•

303

BUSINESS
PROCESS

BINARY
COLLABORATION

BUSINESS
TRANSACTION

INITIATING / REQUESTING SIDE

RESPONDING SIDE

[N90 pattern]3

[X12:EDIFACT equivalents]

[X12:EDIFACT equivalents]

Create order**

PARTNER TYPE:
Retailer

(activity)

(protocol)

Order
Fulfillment

Manage
Purchase
Order**

[Commercial
Transaction]

AUTH ROLE:
Buyer.Create order

DOCUMENT:
Purchase Order
[850:ORDERS]

PARTNER TYPE:
DSVendor
AUTH ROLE: :
Seller.Create order

DOCUMENT:
PO Acknowledgment
[855:ORDRSP]

This column suggests use of one of the six demonstrative transaction patterns currently offered in the UN/CEFACT TMWG N90 metamodel.
**These Business Transactions have been reused from the ebXML Common Business Process Catalog ver 1.0.
3

57

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

BUSINESS
PROCESS

BINARY
COLLABORATION

March 2001

BUSINESS
TRANSACTION

INITIATING / REQUESTING SIDE

RESPONDING SIDE

[N90 pattern]3

[X12:EDIFACT equivalents]

[X12:EDIFACT equivalents]

Change Order **

PARTNER TYPE:
Retailer

(activity)

(protocol)

[Commercial
Transaction]

Notify of
advance
shipment**

Payment
Fulfillment

Process
Payment**

AUTH ROLE:
Buyer.Change
order

Notify of advance
shipment

PARTNER TYPE:
DSVendor

[Notification]

AUTH ROLE:
Shipper.Notify of
advance shipment

Process payment
[Commercial
Transaction]

PARTNER TYPE:
DSVendor
AUTH ROLE:
Payee.Process
payment

DOCUMENT:
Purchase Order
[860:ORDCHG]

DOCUMENT:
ASN
[856:DESADV]

DOCUMENT:
Send Invoice
[810:INVOIC]

PARTNER TYPE:
DSVendor
AUTH ROLE: :
Seller.Change
order
PARTNER TYPE:
Retailer

DOCUMENT:
PO Acknowledgment
[865:ORDRSP]

[No document:
receive ASN]

AUTH ROLE:
Receiver.Notify of
advance shipment
PARTNER TYPE:
Retailer
AUTH ROLE:
Payor.Process
payment

DOCUMENT:
Pay invoice
[820:PAYORD]

304

58

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

ebXML BP/CC Analysis Team

305

March 2001

9 References

306
307

[Bra97]

Bradner, S., "Key words for use in RFCs to Indicate Requirement Level", BCP 14,
RFC 2119, March 1997.

308
309

[ebBPSS]

ebXML Business Process Specification Schema. Version 0.90. 01/17/2001.
Context/Metamodel Group of the CC/BP Joint Delivery Team.

310
311

[bpPROC]

ebXML Catalog of Common Business Processes. Version TBD. Date TBD. ebXML
CC/BP Analysis Team.

312
313
314

[ebCNTXT] ebXML The role of context in the re-usability of Core Components and Business
Processes. Version 1.01. February 16, 2001. ebXML Core Components Project
Team.

315
316

[XBACR]

ebXML specification for the application of XML based assembly and context rules.
Version 1.01. 16 February 2001. ebXML Core Components.

317
318
319

[ISO14662]

Information Technologies - Open-EDI Reference Model. ISO/IEC 14662:1997(E).
International Organization for Standardization (ISO) and International
Electrotechnical Commission (IEC).

320
321

[TAGLOS]

ebXML. TA Glossary. Version 0.95. 12 February 2001. Technical Architecture
Project Team.

322
323

[TASPEC]

ebXML Technical Architecture Specification. Version 1.0.4. 16 February 2001.
ebXML Technical Architecture Project Team.

324
325

[UMM]

UN/CEFACT Modelling Methodology. CEFACT/TMWG/N090R9. February 2001.
UN/CEFACT Technical Modeling Working Group.

326
327

[MDACC]

ebXML Methodology for the Discovery and Analysis of Core Components. DRAFT.
Version 1.0.1. February 16, 2001. ebXML Core Components Project Team.

328
329
330

[BPAWAG]

ebXML Business Process Analysis Worksheets and Guidelines. WORK-INPROGRESS. Version 0.9. March 10, 2001. ebXML Business Process Project
Team.

331
332
333
334
335

336
337
338
339

10 Disclaimer
The views and specification expressed in this document are those of the authors and are not
necessarily those of their employers. The authors and their employers specifically disclaim
responsibility for any problems arising from correct or incorrect implementation or use of this
design.

11 Contact Information
Business Process Project Team
Business Process/Core Components (BP/CC) Analysis Team Lead:
Name:
Brian Hayes
Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

60

ebXML BP/CC Analysis Team

340
341
342
343
344
345
346
347
348
349
350
351
352
353
354

March 2001

Company:
Street:
City, State, ZIP:
Nation:
Phone:
EMail:

Commerce One
4440 Rosewood Drive
Pleasanton, CA
USA
+1 (925) 788-6304
brian.hayes@UCLAlumni.net

Editor:
Name:
Company:
Street:
City, State, ZIP:
Nation:
Phone:
EMail:

Nita Sharma
Netfish Technologies
2350 Mission College Boulevard
Santa Clara, CA 95054
USA
+1 (408) 350-9500
nsharma@netfish.com

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

61

ebXML BP/CC Analysis Team

355

March 2001

Copyright Statement

356

Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

357
358
359
360
361
362
363

This document and translations of it may be copied and furnished to others, and derivative works
that comment on or otherwise explain it or assist in its implementation may be prepared, copied,
published and distributed, in whole or in part, without restriction of any kind, provided that the
above copyright notice and this paragraph are included on all such copies and derivative works.
However, this document itself may not be modified in any way, such as by removing the copyright
notice or references to ebXML, UN/CEFACT, or OASIS, except as required to translate it into
languages other than English.

364
365
366
367
368
369

The limited permissions granted above are perpetual and will not be revoked by ebXML or its
successors or assigns. This document and the information contained herein is provided on an "AS
IS" basis and ebXML DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN
WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY
OR FITNESS FOR A PARTICULAR PURPOSE.

Catalog of Common Business Process
Copyright © UN/CEFACT and OASIS, 2001. All Rights Reserved.

62
```
