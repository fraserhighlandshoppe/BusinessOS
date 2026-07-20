# Requirements Traceability Matrix

## Purpose
Lists each requirement and tracks whether requirement appears in Requirements Specification, Design Specification, and Test Plan.

## Matrix Structure
| Requirement # | Description | Requirement Specification | Design Specification | Test Plan |
|--------------|-------------|---------------------------|---------------------|-----------|
| 1 | Requirement 1 | YES | NO | NO |
| 2 | Requirement 2 | YES | YES | YES |
| 3 | Requirement 3 | YES | YES | NO |
| 4 | Requirement 4 | YES | NO | YES |

## Matrix Data Elements

### Customer Business Requirements
- Project team's interpretation of customer wants and needs
- Must be identified uniquely

### System Requirements
- Derived from Customer Business Requirements
- Must be identified uniquely

### Component Requirements (Optional)
- System Requirements allocated to components
- Delete if not applicable
- Must be identified uniquely

### Requirement Status (Optional)
Recommended values:
- Design complete
- Build complete
- Test verified
- Pending Approval
- Withdrawn

### Priority
- **Essential**: Software won't be acceptable without these
- **Conditional**: Enhances product but won't make it unacceptable
- **Optional**: May or may not be worthwhile

### Design Documents
Identify documents/sections where requirement addressed.

### Build Components
- Software component
- Documentation
- Training Materials

### Acceptance Criteria
Definition of results expected from test cases.
Must be:
- Verifiable
- Attainable
- Unambiguous
- Understandable

**Best Practice**: Write acceptance criteria same time as requirements.

### Test Types
Test phase where requirement verified through lifecycle.
Every Requirement Type has associated Test Type.

**Rule**: Customer business requirement satisfied when all derived requirements satisfied (demonstrated by successful Test Results).

## Instructions
Add, delete, or edit rows/columns as per project's development lifecycle and test strategy.

## Related
- [[Requirements Specification]]
- [[Project Definition]]
- [[Project Test Strategy]]