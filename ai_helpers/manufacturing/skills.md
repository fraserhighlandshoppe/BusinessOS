---
title: "Manufacturing AI Helper Skills"
description: "AI skills and prompt engineering for manufacturing - production planning, quality control, process optimization, capacity management"
author: "Business Operating System"
source: "https://www.ama.org"
date: "2024"
tags:
  - domain:operations
  - type:skill
  - confidence:high
  - standard:ama
  - skill:manufacturing
  - skill:production-management
  - ai:helper
categories:
  - AI Helpers
  - Operations
  - Manufacturing
  - Skills
  - Prompt Engineering

---

# Manufacturing AI Helper Skills

## Core Competencies

### 1. Production Planning Skills
- **Master Production Schedule (MPS)**: Demand forecasting, capacity planning
- **Material Requirements Planning (MRP)**: BOM explosion, procurement scheduling
- **Capacity Planning**: Resource leveling, bottleneck identification
- **Production Scheduling**: Job shop scheduling, finite scheduling
- **Finite Capacity Planning**: Resource constraints, overtime optimization

### 2. Quality Control Skills
- **Quality Planning**: Quality function deployment (QFD), control plans
- **Statistical Process Control (SPC)**: Control charts, process capability
- **Inspection Planning**: Sampling plans, acceptance criteria
- **Non-Conformance Management**: NCR processing, corrective actions
- **Quality Metrics**: Defect rates, yield analysis, customer complaints

### 3. Process Optimization Skills
- **Lean Manufacturing**: Waste identification, continuous improvement
- **Six Sigma**: DMAIC methodology, defect reduction
- **Process Mapping**: Value stream mapping, flow analysis
- **Kaizen Events**: Improvement workshops, rapid improvement
- **Overall Equipment Effectiveness (OEE)**: Availability, performance, quality

### 4. Capacity Management Skills
- **Resource Loading**: Machine, labor, material allocation
- **Capacity Utilization**: Efficiency analysis, bottleneck identification
- **Load Leveling**: Smooth workload distribution, overtime reduction
- **Capacity Expansion**: Equipment purchase, facility expansion
- **Make-or-Buy Analysis**: In-house vs outsourcing decisions

### 5. Shop Floor Management Skills
- **Work Order Management**: Creation, routing, completion tracking
- **Production Monitoring**: Real-time status, deviation alerts
- **Labor Management**: Time tracking, skill assignments
- **Material Tracking**: Raw material consumption, WIP tracking
- **Facility Management**: Equipment maintenance, space utilization

## AI Prompt Engineering

### Production Planning Prompt
```
You are a production planner for [PRODUCT_LINE].

Demand Forecast:
- Next 30 days: [QUANTITY]
- Next 90 days: [QUANTITY]
- Seasonal factors: [FACTORS]

Capacity:
- Available hours: [HOURS]
- Machine capacity: [CAPACITY]
- Labor availability: [LABOR]

Plan production runs:
1. Priority ranking
2. Resource allocation
3. Material requirements
4. Timeline estimation
5. Risk mitigation

Output: Production schedule with material requirements.
```

### Quality Control Prompt
```
You are a quality control engineer reviewing [PRODUCT/BATCH].

Quality Data:
- Defect Count: [COUNT]
- Sample Size: [SIZE]
- Defect Type: [TYPE]
- Process Step: [STEP]
- Date: [DATE]

Analyze:
1. Defect rate calculation
2. Root cause identification
3. Corrective action recommendation
4. Preventive measures
5. Documentation requirements

Output: Quality analysis report with CAPA recommendations.
```

### Process Optimization Prompt
```
You are conducting process improvement analysis for [PROCESS].

Current State:
- Cycle Time: [TIME]
- Throughput: [RATE]
- Defect Rate: [PERCENTAGE]
- Lead Time: [TIME]

Identify improvement opportunities:
1. Waste identification (muda)
2. Bottleneck analysis
3. Standardization needs
4. Automation potential
5. Training requirements

Provide improvement plan with expected benefits.
```

### Capacity Planning Prompt
```
You are planning capacity for [QUOTED_DEMAND].

Capacity Data:
- Current Capacity: [UNITS]
- Utilization: [PERCENTAGE]
- Bottlenecks: [LIST]
- Overtime: [HOURS]
- Equipment Age: [AGE]

Plan capacity expansion:
1. Short-term solutions
2. Medium-term investments
3. Long-term strategy
4. Cost-benefit analysis
5. Implementation timeline

Output: Capacity expansion plan with ROI analysis.
```

### Work Order Management Prompt
```
You are creating work order for [PRODUCT/JOB].

Order Details:
- Product: [PRODUCT]
- Quantity: [QUANTITY]
- Due Date: [DATE]
- Routing: [ROUTING]
- Priority: [PRIORITY]

Create work order with:
1. Bill of Materials
2. Operation sequence
3. Resource requirements
4. Quality checkpoints
5. Completion criteria

Output: Work order ready for shop floor execution.
```

## Related Templates
- [[Production Schedule Template]]
- [[Quality Control Plan]]
- [[Process Map Template]]
- [[Capacity Planning Worksheet]]
- [[Work Order Template]]

## References
1. American Manufacturing Association, "Manufacturing Best Practices", ama.org, 2024.
2. SME, "Manufacturing Engineering Guide", sme.org, 2024.
3. ASQ, "Quality Management Standards", asq.org, 2024.