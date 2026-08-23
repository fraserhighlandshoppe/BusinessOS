---
title: "Requirements Management"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Requirements_Management"
type: wiki
categories: Business
author: Fraser Highland Shoppe Wiki
---

{{:Business Analysis Pages}}
==Requirements Management==
===The importance of requirements===
Poor requirements lead to troubled projects.  
*Only 29% of projects are successful.
*rework accounts for 30-40% of development budgets
**50% of rework is due to missing/bad requirements

Common causes of troubled projects
*failure to reach common understanding of requirements/completion criteria
*failure to understand proposed solution
*failure to establish appropriate contractual baselines
*failure to set and manage customer expectations
*inaccurate project estimates, etc
**if you don't understand the requirements and scope you can't get an accurate estimate

Successful projects:
*Sell it right
**Right expectations set at the client
***Requirements
***responsibilities
***risks
***assumptions
***deliverables
***delivery approach
*Start it right
***right people
**right process
**right tools n place
**project plan
*Execute it right
**manage business benefits throughout project
**manage scope
**manage profitability
**manage risks
**manage client satisfaction
**work plan tracked
[[Category: Project Management]]
====Quality Requirements====
*Establish a common understanding of work required and potential acceptance criteria.
**clear understanding of needs of users, customers, stakeholders
*Improve customer confidence in the products and services delivered
*provide a roadmap to success by 
**ensuring that high priority needs are addressed
**set and manage expectations
*Assist in ensuring the delivery
**useability of the product
**reduction of defects due to misunderstanding and misinterpretation.

Characteristics:
*Correct
*Possible - feasible tools, techniques, people, budgets
*necessary - trace back to use case
*unambiguous - one interpretation.  Easy to read and understand
*concise - only the info needed to proceed
*Verifiable - testable, measureable
*prioritized

====Poor Requirements====
Contribute to one third of total delivered defects.  
===What are Requirements used for===
Customers may not know what they really want.
*different stakeholders will express their requirements differently

Both customers and vendors hear what they want to hear.

Requirements are never completely understood the first time around.  Requirements aren't complete the first round.
*requirements development is an iterative process
*even with sign-off things can/will change
**don't let yourself or client end up in analysis paralysis.
Key is to have a plan to manage requirements through to sign-off.

Requirements are used for:
*project scope
*cost estimate
*project scheduling and planning
*solution design
*solution testing
*defect management
*release management
*documentation
*training manuals.

You can't build a solution without the requirements.  The requirements will influence:
*direction of development
*architecture
*solution sizing
*solution costing
*product selection
*deployment
*configuration framework
====Requirements are====
*specification of what should be implemented
*description of how the system should behave
*system properties or attributes
====Requirements are NOT====
*design details
*implementation details other than known constraints
*project planning info
*testing info
===The sources of requirements===
*End users
*SMEs
*Business case
*project context (RFP, RTF, SOW)
*IT environment
*enterprise architecture

Requirements are the bridge between the stakeholders and the solution.
====gathering and analysis====
In scope:
*functional
*non functional
Out of Scope
*third party requirements
*future requirements

==Types and levels of requirements==
Requirements are specifications of the capabilities or functions that are needed by the users of the system to complete their job.
*often the wants is based on a preconception and may not provide the benefits required
*frequently their needs are poorly identified.
*Sometimes the needs are conflicting.

You must gather:
*clients needs
*expectations
*constraints
*interfaces
*operational concepts
*product concepts

You must identify, analyze, harmonize, refine and elaborate the client's business requirements.

Key requirements should relate back to business benefits as specified in business cases.
===Types of requirements===
====Functional Requirements====
Functional requirements present a complete description of how the system will function from the user perspective
*allow both business stakeholders and technical people to walk through the system and see every aspect before it is built.

Functional requirements answer the question of "WHAT" does the customer want.  (But not HOW).

Functional requirements can be expressed as interactions between people and systems or systems to systems.
*When I do X the system does Y
*When system1 sends X systems 2 will send back Y.

Functional requirements focus on:
*who will use the system
*when will they use it (what are the triggers)
*what information will they need to input
*what info or action will they take as a result
*what are the business rules that are used to decide what actions to take?

====Non Functional Requirements====
Non functional requirements dictate properties and impose constraints on the project or system.  They specify attributes.
*categories into qualities and constraints
*qualities define the expectation and characteristics
*constraints are things lie
**system should respond within X seconds
**Only authorized users may access X
**system shall conform to standard X
**must adhere to government regulation XYZ123.

Qualities
*runtime
**capacity and performance
**availability
**security
**system management
**integration services
*non runtime
**portability
**maintainability
**scalability
**data integrity
**safety

Constraints
*Business
**regulatory
**risk willingness
**organizational
**marketplace factors
**schedule and budget
*technical
**legacy integration
**development skills
**existing infrastructure
**IT standards
**technology

===Levels of Requirements===
Customer wants and needs
*business drivers

Business requirements
*functional requirements
*non functional requirements

System requirements
*component requirements
*detailed requirements

====Wants and Needs====
A standard work product would look something like:
#Intro
##document summary - describe business problem being solved
#references
#wants and needs
##List of stakeholders
##list of wants and needs
##map business drivers to wants and needs
##assumptions
##issues
##risks
##constraints
#Appendices

====Business requirements====
These address a specific business problem.
*support a business scope or objective
*have a business purpose/focus
They state what needs to be accomplished using business language
*should include success/acceptance criteria
*should include the rationale explaining why each business requirement should be considered
**why it exists
**assumptions
**relevant findings of design studies or other info useful in managing the business requirement.

If the requirement can't be justified, remove it.

====System Requirements====
These are the translation of business requirements into what the system will need to do.
*describes in technical terms the what, but not the how.
*not all business requirements become system requirements.  Some business requ9irements shall be fulfilled through human processes or organizational elements.
*Where a business requirement is implemented in the system, there is usually multiple system requirements to a business requirement.
*system requirements reflect compromises between what the business would like and what it can afford.
System requirements provide a greater level of detail in terms of the interactions and information passing between users and the system or between systems.

==Capturing the client requirements==
A work product may or may not be a part of the deliverable (what is in the contract to be provided to the client)
===Work Products===
====Requirements Traceability and Verification Matrix====
====Customer Wants and Needs====
Requirements and desires from perspective of customer.

If you don't have this, you will have a hard time in the customer relationship showing value.
====Business roles (BR)====
These document the roles involved in the business.

Without these it is difficult to identify user groups.  Also hinders understanding where and how business activities are conducted.
====Functional Requirements (BR)====
COntain all of the business requirements from a user perspective.

Without it:
*no understanding of business requirements that need to be addressed
*fail to deliver the needs
*failure to deliver expectations
*missing capabilities
====Non functional requirements (BR)====
describes the quality attributes

Without this doc, the system may not perform in the way needed (e.g. to slow a response time)
====Architecural Decisions (NFR)====
Documents key decisions about the architecture and the rationale behind those decisions.

Without it:
*different parties may make different decisions more than once, and they may be different each time.
*Difficulty closing controversial decvisions
*inconsistent decisions
*decisions contradicting other decisions
*new team members take longer to understand architecture.
====business events (BR)====
Events that cause the business to act

Without it:
*lack of understanding why
*lack understanding the transactions that need to be addressed
*business processes may be missed
*process models may be too narrowly focused
*use cases may cover multiple events.
====related use cases (BR)====
====business rules (BR)====
====Process (BR)====
A swim lane diagram can be used to document a process:
*Business roles
*business events
*related use cases
*business rules

Without it:
*More complex processes may be difficult to understand
*difficult to ensure design will fulfill required capabilities
*difficult to gather requirements on organization and tech
*difficult to sync design of package and business processes.

====Future Org Scope (BR)====
Describes the organizational change that is required to achieve the objectives.

Without it:
*Org units that are impacted may be missed in communications
*the new organization may have risks the client isn't willing to carry.

====System Context (SR)====
Represents the entire solution as a single object and identifies the interfaces between external entities.

Without it:
*key groups may be missed
*key external systems interfaces may be missed
*validation and agreement of information flowing between external systems and this one may be missed.
====Architecture overview (SR)====
illustrates the essential nature of the proposed architecture.  Shows major building blocks.


====Useability Requirements (SR)====
====Interface Specifications (SR)====
====Standards (SR)====
describes the pre-determined standards.

Without it:
*costly decisions made without regard to standards
*failure to comply with company policies
*exposure of corporate assets
*failure to comply with regulations.
====Use Case Model (SR)====
Captures the intended functions and environment of the system.  Serves as the contract between the customer and the team.

Without it:
*difficult to determine relationship between actors and use cases
*missing understanding how different use cases relate.
====Use Cases (SR)====
Capture system behavior to yield an observable result and who interacts with the system.

All of the use cases together should cover the entire functionality scope of the system.

Without it:
*May be unclear what functionality needs to be supported

====IT Management Requirements (SR)====
used to evaluate the existing IT Management Environment to determine what changes are required to support the solution.

====Network Requirements (SR)====
describe specific network requirements

Needed to design the network architecture and define changes to existing network.

====Performance Model (NFR) ====
Documents the analysis and conclusions of the study to assess the architectures ability to meet the performance requirements.

WIthout it:
*sub standard performance of solution
*over engineer the solution
*capacity planning errors.


[[Category: Business]][[Category: Software]][[Category: Development]][[Category: Requirements]]
[[Category: Project Management]]