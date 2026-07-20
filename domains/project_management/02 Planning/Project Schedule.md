---
title: "Project Schedule"
description: "Project scheduling methodology - activity relationships, critical path, adjustments"
author: "Project Management Institute"
source: "https://www.pmi.org/learning/thought-leadership/pmbok"
date: "2017"
tags:
  - domain:project-management
  - type:process
  - confidence:high
  - standard:pmbok
  - skill:project-scheduling
categories:
  - Project Management
  - Scheduling
  - Critical Path
  - PMBOK

---

# Project Schedule

## Building the Schedule
Convert Work Breakdown Structure (WBS) into network diagram showing relationships between work activities.

## Relationships Between Activities

### 1. Finish to Start (FS)
Depends on previous activity finished before this can start.

### 2. Start to Start (SS)
Two activities start at same time.

### 3. Finish to Finish (FF)
Two activities end at same time.

### 4. Start to Finish (SF)
Depends on another activity starting so this one can finish.

## Precedence Diagramming Method Steps
1. Establish start activity
2. Identify all activities that can start immediately
3. Identify what can start once another activity ends (complete for all predecessor/successor relationships)
4. Identify activity that signifies completion
5. Calculate forward pass (Early Start/Early Finish) - choose latest date when multiples
6. Find latest early finish date
7. Calculate backward pass (Late Start/Finish) - choose earliest when multiples
8. Calculate float
9. Identify critical path
10. Validate diagram
11. Verify work can be done in time and resource availability
12. Adjust schedule as required
13. Include level of effort tasks

## Schedule Adjustments

### Fast Tracking
- Do things in parallel normally done serially
- Change approach
- Change FS to FF relationships
- Change date constraints allowing critical path items to start/end earlier

### Crashing
- Action to decrease total project duration after analyzing alternatives
- Maximum duration compression for least cost

## Definitions

### Early Start
Earliest task can start without affecting project schedule.

### Late Start
Latest task can start without affecting project schedule.

### Float
Amount of time activity can be delayed from Early Start without delaying project.

### Free Float
Amount of time task can be delayed without delaying early start of any following activities.

### Critical Path
Longest path (duration-wise) through project.

### Lead Time
Amount of time successor can start before predecessor completion.

### Lag Time
Fixed amount of time between end of predecessor to start of successor.

### Milestone
Significant event (decision point, work product completed). Zero duration and resources.

## References
1. Project Management Institute, "A Guide to the Project Management Body of Knowledge (PMBOK Guide)", 6th Edition, 2017.

## Related
- [[Project Definition]]
- [[Project Work Breakdown Structure]]
- [[Project Test Strategy]]