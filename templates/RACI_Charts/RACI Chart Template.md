# RACI Chart Template

## Purpose
Standard template for defining roles and responsibilities across project activities.

## Definitions

| Acronym | Meaning |
|---|---|
| R | Responsible - Does the work |
| A | Accountable - Answerable for outcome |
| C | Consulted - Two-way communication |
| I | Informed - One-way communication |

## Template Structure

```markdown
# RACI Chart: [Project Name]

| Activity/Task | [Role 1] | [Role 2] | [Role 3] | [Role 4] |
|---|---|---|---|---|
| Task 1 | R | A | C | I |
| Task 2 | R | C | A | I |
```

## Key Roles for FHS Projects

| Role | Description |
|---|---|
| Project Sponsor | Business owner, budget approver |
| Project Manager | Day-to-day execution, coordination |
| Technical Lead | System architecture, development |
| Business Analyst | Requirements, user stories |
| QA Lead | Testing, quality assurance |
| End Users | Subject matter experts, feedback |

## Common Activities

| Activity | PM | Sponsor | Tech Lead | BA | QA |
|---|---|---|---|---|---|
| Define scope | A | R | C | R | I |
| Review requirements | C | C | R | A | I |
| Design solution | C | I | A | R | C |
| Develop features | I | I | R | C | I |
| Test solution | C | I | C | I | A |
| Deploy to production | R | A | R | C | C |
| User acceptance | C | C | I | R | C |
| Close project | R | A | I | I | I |

## Usage Notes

- Each activity should have exactly ONE accountable person
- Multiple people can be responsible for collaborative tasks
- Include all relevant stakeholders
- Review and update as project evolves