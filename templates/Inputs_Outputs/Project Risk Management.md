# Project Risk Management

## Purpose
Proactive identification, analysis, and mitigation of risks that could impact project success.

## Risk Definition
A potential event that might adversely affect the project.

## Risk Matrix

| Probability \ Impact | Low | Medium | High |
|---|---|---|---|
| **High** | Medium | High | Critical |
| **Medium** | Low | Medium | High |
| **Low** | Low | Low | Medium |

### Risk Scoring
- **Probability**: 1-5 (Rare to Almost Certain)
- **Impact**: 1-5 (Negligible to Catastrophic)
- **Risk Score** = Probability × Impact
- **Exposure %** = (Probability + Impact) / 2

## Risk Types

### Internal Risks (Under Project Team Control)
- Quality of deliverables
- Project plans accuracy
- Resource availability
- Missed requirements
- Delivery schedule

### External Risks (Outside Project Team Control)
- Market conditions
- Governmental legislation
- Organizational changes
- Vendor performance
- Economic factors

## Risk Management Process

### 1. Identification

**Methods**:
- Brainstorming sessions
- Historical data review
- Expert interviews
- Checklists
- Assumption analysis

**Considerations**:
- Size of domain
- Number of technologies
- Complexity
- Regulations
- Business stability
- Novelty of solution
- Geographic dispersion

### 2. Analysis

**Qualitative Analysis**:
- Probability: Very Low (1) - Very High (5)
- Impact: Very Low (1) - Very High (5)

**Quantitative Analysis** (for high risks):
- Monte Carlo simulation
- Decision tree analysis
- Sensitivity analysis

### 3. Response Planning

#### Risk Strategies

| Strategy | When to Use | Example |
|---|---|---|
| **Avoid** | Risk unacceptable | Change approach entirely |
| **Mitigate** | Reduce probability/impact | Additional testing |
| **Transfer** | Shift to third party | Insurance, outsourcing |
| **Accept** | Cost of action > benefit | Reserve budget |
| **Exploit** | Positive risk opportunity | Accelerate delivery |

#### Response Actions

1. **Mitigation**: Proactive steps to reduce risk
2. **Contingency**: Specific actions if risk occurs
3. **Reserve**: Budget/time set aside
4. **Insurance**: Contractual protection

### 4. Tracking & Control

**Monitoring**:
- Risk register updates
- Risk indicator tracking
- Regular risk reviews
- Status changes

**Control Actions**:
- Activate contingency plans
- Use reserves
- Create new mitigation plans
- Close resolved risks

### 5. Reaction

**When Risk Occurs**:
1. Implement response plan
2. Document lessons learned
3. Update risk register
4. Communicate impact

## Risk Register Template

| ID | Risk | Category | Probability | Impact | Score | Owner | Response | Status |
|---|---|---|---|---|---|---|---|---|
| R-001 | | | 1-5 | 1-5 | P×I | | | |

## Risk Response Plans

### Mitigation Plan Template
```markdown
## Risk: [Risk Name]

**Probability**: [1-5]
**Impact**: [1-5]

### Mitigation Actions
1. [Action 1] - Owner: [Name], Due: [Date]
2. [Action 2] - Owner: [Name], Due: [Date]

### Success Criteria
[Measurable outcome]

### Contingency Plan
[If mitigation fails]
```

### Contingency Plan Template
```markdown
## Contingency: [Risk Name]

### Trigger
[What indicates risk is occurring]

### Response
1. [Step 1]
2. [Step 2]

### Resources
- Budget: $[Amount]
- Time: [Days]
- Personnel: [Who]

### Approval
Signature: _________________
```

## RACI Chart

| Activity | Project Manager | Risk Owner | Team | Sponsor |
|---|---|---|---|---|
| Identify risks | R | C | A | I |
| Analyze risks | A | R | C | I |
| Plan responses | A | R | C | C |
| Track risks | R | A | C | I |
| React to risks | R | A | C | I |

## References
- Project Scope Document
- Historical project data
- Stakeholder inputs