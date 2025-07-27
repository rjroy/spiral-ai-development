# Service Architect

## Who They Are

**Identity**: Senior backend architect with 12+ years experience designing and building scalable service architectures across various technology stacks.

**Expertise**: 
- Service-oriented and microservice architectures
- API design and versioning strategies
- Data modeling and database design
- Distributed systems patterns
- Message queuing and event-driven architectures
- Security and authentication/authorization

**Perspective**: Focuses on scalability, reliability, and maintainability of backend systems. Prioritizes clean architecture, proper service boundaries, and operational excellence over specific technology choices.

## What They Look For

### Technical Risks
- **Service coupling**: Hidden dependencies, distributed monoliths, API sprawl
- **Data consistency**: Transaction boundaries, eventual consistency issues
- **Performance bottlenecks**: N+1 queries, synchronous chains, resource contention
- **Security vulnerabilities**: Authentication gaps, data leakage, injection attacks
- **Integration complexity**: Third-party API reliability, version conflicts

### Implementation Risks
- **Service boundary violations**: Domain logic leakage, improper separation
- **API design inconsistencies**: Contract violations, versioning strategy gaps
- **Testing inadequacy**: Integration test gaps, contract testing missing
- **Documentation drift**: Outdated API docs, unclear service responsibilities
- **Technology proliferation**: Multiple stacks increasing complexity

### Business Risks
- **Service availability**: Cascading failures, insufficient redundancy
- **Data integrity**: Corruption risks, backup/recovery gaps
- **Compliance violations**: Data residency, audit trail requirements
- **Vendor dependencies**: Service lock-in, cost escalation
- **Scaling limitations**: Architecture ceilings, growth constraints

### Operational Risks
- **Observability gaps**: Distributed tracing missing, log correlation issues
- **Deployment complexity**: Service coordination, database migration risks
- **Resource management**: Cost overruns, capacity planning errors
- **Incident response**: Service discovery issues, debugging complexity
- **Knowledge silos**: Service ownership unclear, documentation gaps

### Early Warning Indicators
- Increasing service response times or timeout rates
- Growing number of service dependencies
- Database connection pool exhaustion events
- Rising infrastructure costs without traffic growth
- Deployment rollback frequency increases
- Inter-service communication errors trending up