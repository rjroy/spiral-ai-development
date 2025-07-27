# Level 2 Component Artifact Template

This template structures component specifications from Level 2 Structure Definition. External artifacts (APIs, data models, interfaces) are referenced, not embedded.

---
artifact_type: "component"
component_name: "ComponentName"
created_date: "YYYY-MM-DD"
sdd_level: 2
source_phase: "structure"
version: "1.0"
---

## Component Definition

**Name**: ComponentName
**Purpose**: Single sentence describing what this component does
**Responsibility**: Primary responsibility of this component
**Boundaries**: What this component does NOT do

**Business Domain**: Business area this component serves
**Team Ownership**: Which team owns this component
**Replaceability Assessment**: LOW/MEDIUM/HIGH - realistic assessment of replacement difficulty

## Component Interfaces and Contracts

### Exposed Interfaces
This component provides the following interfaces to other components:

```yaml
exposed_interfaces:
  - interface_name: "InterfaceName"
    interface_type: "REST_API/GRAPHQL/MESSAGE_QUEUE/DATABASE/FILE_SYSTEM"
    specification_file: "path/to/api-spec.yml"  # External reference
    description: "What this interface provides"
    consumers: ["List of components that use this interface"]
```

### Consumed Interfaces
This component depends on the following external interfaces:

```yaml
consumed_interfaces:
  - interface_name: "ExternalInterfaceName"
    provider_component: "ComponentThatProvidesThis"
    interface_type: "REST_API/GRAPHQL/MESSAGE_QUEUE/DATABASE/FILE_SYSTEM"
    specification_file: "path/to/external-api-spec.yml"  # External reference
    description: "What this component needs from external interface"
    critical_dependency: true  # true if component cannot function without this
```

## Data Management

### Owned Data
This component owns and manages the following data:

```yaml
owned_data:
  - data_entity: "EntityName"
    data_model_file: "path/to/data-model.yml"  # External reference
    description: "What this data represents"
    persistence_type: "DATABASE/FILE/CACHE/MEMORY"
    access_patterns: ["READ_HEAVY/WRITE_HEAVY/MIXED"]
```

### Accessed Data
This component accesses but does not own the following data:

```yaml
accessed_data:
  - data_entity: "ExternalEntityName"
    owner_component: "ComponentThatOwnsThis"
    access_type: "READ_ONLY/READ_WRITE"
    description: "How this component uses external data"
```

## Integration Patterns

### Communication Patterns
How this component communicates with others:

```yaml
communication_patterns:
  - pattern_type: "SYNCHRONOUS/ASYNCHRONOUS"
    protocol: "HTTP/GRPC/MESSAGE_QUEUE/DATABASE"
    usage: "When this pattern is used"
    error_handling: "How errors are handled"
```

### Data Consistency Requirements
Data consistency needs for this component:

```yaml
consistency_requirements:
  - requirement: "Description of consistency need"
    scope: "Which data/operations this applies to"
    consistency_level: "STRONG/EVENTUAL/WEAK"
```

### Performance Characteristics
Expected performance characteristics:

```yaml
performance_characteristics:
  - characteristic: "Response time/Throughput/etc"
    target_value: "Specific measurement target"
    measurement_method: "How this will be measured"
```

## Component Constraints and Assumptions

### Technical Constraints

```yaml
technical_constraints:
  - constraint: "Specific technical limitation"
    source: "Where this constraint comes from"
    impact: "How this affects the component"
    mitigation: "How to work within this constraint"
```

### Business Constraints

```yaml
business_constraints:
  - constraint: "Business rule or limitation"
    source: "Business requirement or regulation"
    impact: "How this affects component design"
```

### Scaling Constraints

```yaml
scaling_constraints:
  - constraint: "Scaling limitation"
    bottleneck: "What limits scaling"
    mitigation_strategy: "How to handle scale"
```

## Validation and Testing Approach

### Integration Validations
Integration points that need validation:

```yaml
integration_validations:
  - validation_target: "What integration point to test"
    validation_method: "How to validate this works"
    success_criteria: "What indicates success"
```

### Boundary Validations
Component boundaries that need validation:

```yaml
boundary_validations:
  - boundary: "Which boundary to test"
    validation_approach: "How to validate boundary is correct"
```

### Performance Validations
Performance characteristics to validate:

```yaml
performance_validations:
  - performance_aspect: "What performance characteristic to test"
    measurement_approach: "How to measure performance"
    acceptance_criteria: "What performance is acceptable"
```

## Risk Assessment

### Component Risks

```yaml
component_risks:
  - risk_id: "R-COMP-001"
    risk_description: "What could go wrong"
    probability: "HIGH/MEDIUM/LOW"
    impact: "HIGH/MEDIUM/LOW"
    mitigation_strategy: "How to prevent/respond"
```

### Integration Risks

```yaml
integration_risks:
  - risk_id: "R-INT-001"
    risk_description: "Integration failure scenario"
    affected_components: ["List of components affected"]
    mitigation_strategy: "How to handle integration failure"
```

## Traceability

**Level 1 Approach**: Which Level 1 approach this component supports
**Level 0 Vision**: How this component contributes to Level 0 vision
**Architectural Decisions**: Key architectural decisions this component implements

## External Artifacts

### API Specifications

```yaml
api_specifications:
  - artifact_name: "API Specification Name"
    file_path: "path/to/api-spec.yml"
    format: "OpenAPI/GraphQL/Proto/etc"
    description: "What this specification covers"
```

### Data Models

```yaml
data_models:
  - artifact_name: "Data Model Name"
    file_path: "path/to/data-model.yml"
    format: "JSON_Schema/Proto/SQL/etc"
    description: "What data this model represents"
```

### Interface Definitions

```yaml
interface_definitions:
  - artifact_name: "Interface Definition Name"
    file_path: "path/to/interface.yml"
    format: "YAML/JSON/Proto/etc"
    description: "What interface this defines"
```

## Decomposition Readiness

### Ready for Level 3
**Ready for Level 3**: true (when this component can be decomposed into features)

### Suggested Feature Decomposition

```yaml
suggested_decomposition:
  - feature_area: "Area of functionality"
    rationale: "Why this should be a separate feature"
    complexity_estimate: "LOW/MEDIUM/HIGH"
```

### Blocking Dependencies

```yaml
blocking_dependencies:
  - dependency: "What needs to be resolved"
    impact: "How this blocks Level 3 decomposition"
    resolution_approach: "How to resolve this dependency"
```