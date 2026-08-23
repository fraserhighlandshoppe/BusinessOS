---
title: "Solution Assessment and Validation"
source: "http://fhsws002.ksfraser.com/infra/wiki/index.php?title=Solution_Assessment_and_Validation"
type: wiki
categories: Business
author: Fraser Highland Shoppe Wiki
---

{{:Project Management Pages}}

{{:Requirements Process}}
==Solution Assessment and Validation==
The process to review and assess a software solution is similar to what you would do when shopping for a new stove.
#review and revise the solution until it meets stakeholder requirements
#choose the solution
#test the solution
#implement the solution
#conduct post implementation activities such as closing the project and lessons learned.

Benefits include
*able to review and revise the solution in a methodical manner
*being able to make an informed decision when selecting the solution
*being able to avoid many pitfalls associated with solution implementation
*knowing the key aspects of a post implementation strategy.

===Design process selection===
Once the requirements package is approved the tech team can work on the solution
*modeling
*prototyping
The BA communicates design decisions to stakeholders so that decisions can be made in a timely fashion.

The BA also communicates with the tech team to help them with decisions that need to be made.

===Creating the design plan===
#review characteristics of end user
##need to accommodate knowledge, skill levels and needs
##generally one user profile for each user group.
#review features and functions
##functional requirements
##Quality of Service requirements
###performance
###security
###operational
###environmental
###privacy
###quality
#map requirements to design
##tech designer and BA 
###automated or manual
###priority
###data requirements
###business rules
###complexity rating and technical priority
#propose design phases
##PM and BA decide on how many design phases and move requirements into the appropriate phase
##BA writes a description of each phase - goals and requirements 
###interface
###components
###data structures
###algorithms
#update the requirements traceability matrix
##some regulatory agencies require the matrix to ensure safety.
##when a row or column in the matrix is missing a cross reference, you have missing requirements or feature creep.
###BA must alert PM immediately when a missing requirement or a feature creep is discovered.
#recommend improvements for non-automated processes
##it is not always possible to automate all processes.

===Build or Buy===
Lacking tech resources, small organizations often buy or contract a third party to build.

Medium to large organizations frequently feel their needs are unique and therefore buying isn't appropriate.

To correctly decide:
#focus
##buy or outsource peripheral activities.
#skill
##some external organizations have a deep skill level
#scale
##economies of scale due to performing the same thing many times.

Types of software solution
*COTS
*Custom Built
*hybrid

==Solution Testing==
===Principals of testing===
#assume the solution has errors
#clarify the expected result of each test
#use testers who are not directly involved with the project team
##gets rid of biases held by development team
#save all testing documentation
##testing is iterative, so you need to track as you go along.
##retained test documents records what, when, results, etc
##retained plans can be reused for each iteration, regression, etc.
#check for unwanted side effects
##highly coupled code have a ripple effect from a small change.
#make sure requirements have been signed off before testing
##sign off doesn't prevent change, but it does indicate what the expected results are
#create a safe testing environment
##don't affect prod environment
##data probably has [[PIPEDA]] or other protection levels required.

===Structural Walkthrough===
The structured walkthrough is a stakeholder meeting to review processes, screen mockups, etc.

Emphasis is on finding ommisions, and not on fixing them.  After the walk through the author of the artifact fixes the artifact by interviewing SMEs etc as required.  A followup walkthrough may be required.

The structured walkthrough is used to ensure requirements are ready to turn over to the developer.

Check
*use cases
*test plans
*entity relationship diagrams

Testing for completeness and accuracy.  Any errors in the requirements become large errors in the code, which are much more expensive to fix.
===Test Case===
Test cases are written by the BA or QA to match.

Test cases are written without any knowledge of how the code works (i.e. black box testing).

Test cases are usually required for:
*each column of a decision table
*each row of a condition-response table
*each flow of a use case

Each test case is associated to a test script.
*data required
*procedure to test
**what to test
**what data to use
**how to test the data
**how often to repeat
**expected result.
*boundary value analysis
**max
**min
**just inside and outside the min and max
**typical values
**error values

If the number of input or output values must lie within a range, 
#create a test to cover each end of the range i.e. one at the min and one at the max.
#create 2 invalid tests - one just below the min and one just above the max.

==Implementation==
===Prepare===
*review the infrastructure
**ensure capacity will be sufficient
*coordinate with everyone involved.  
**Ensure everyone knows their roles.  
**Communicate with infrastructure and support groups.
*provide training to those that need it
**create training plan
**map content and develop courses
*test training materials during software test phase
*training delivered just before implmentation

Training delivered too far in advance will ensure no one remembers how the system works.  OTOH if the training is rushed the trainees won't have the time to absorb the new info and internalize the new processes.
===Install===
*physically install
**declare test version is now prod; or
**migrate software from test environment into prod
**install at multiple locations (aka rollout).
*convert data
**map data from old to new systems
**convert business rules
**schedule the data conversion
*perform final validation.
**checking that everything appears to be running as expected
**move data through the software
[[Category: Software Install]]
===Implement===
*switch users over to the new processes and procedures
*monitor that software is performing as expected
**new software generally includes new processes.  This requires good documentation and support teams.
[[Category: Software Implementation]]
==Project closure==
#conduct a lessons learned
#review project plan to ensure all phases completed - ensure all sign-offs received, all deliverables have been delivered and action items have been closed.
##scope
##design
##development
##testing
##training
##documentation
##Installation
#gather measurements and reports
##common reason for a project is performance improvement. Measure to see if project met objectives.
#analyze project data
##using the performance data and compare against requirements, prove that project met requirements/plan.
#get approval from sponsor to close
##obtain signatures agreeing project is complete
##deliver a presentation of the objectives, and how they were met.  Use the data from the previous step.
#archive files
##planning documents can be used for future similar project planning
##risk and issues logs can help plan future projects.
##physical or electronic archive of
###charter
###plan
###risk register
###schedule
###budget
###requirements package
###change requests
###lessons learned.
[[Category: Project Closure]]

===Lessons learned===
*examine project records and documents
*using a questionnaire or survey
*conduct personal interviews
*facilitate a meeting
[[Category: Lessons Learned]]

===Post Implementation Review===
Easiest way to tell if the solution meets the stakeholder needs is to ask them.
*surveys
*interviews

ask about
*management of the budget and schedule
*achievement of goals and objectives
*effectiveness of communication
*requirements and functionality
*realization of project benefits.
[[Category: Post Implementation Review]]

Then conduct a project assessment with PM, project team and key stakeholders:
*feedback from surveys and interviews
*what was successful and what wasn't
*best practices
*lessons learned
[[Category: Project Assessment]]

Then draft the Post Implementation Report.  It is the history of the project.
*includes the project assessment
*includes PM conclusions
*includes BA conclusions

[[Category: Post Implementation Report]]

[[Category: Requirements]]
[[Category: Business]]
[[Category: Business Analyst]]