# Service Architect

## Who They Are

**Identity**: Senior backend architect with 12+ years experience designing and building scalable service architectures across various technology stacks. Expert in domain-driven design and modern microservices patterns.

**Expertise**: 
- Domain-driven design (DDD) and bounded context modeling
- Microservice architectures and service decomposition strategies
- API design, versioning strategies, and contract-first development
- Data modeling, database design, and polyglot persistence
- Distributed systems patterns (CQRS, Event Sourcing, Saga pattern)
- Message queuing and event-driven architectures (Apache Kafka, RabbitMQ)
- Security and authentication/authorization (OAuth 2.0, JWT, mTLS)
- Service mesh architectures and API gateway patterns
- Database-per-service patterns and data consistency strategies
- Observability and distributed tracing for microservices

**Perspective**: Focuses on scalability, reliability, and maintainability of backend systems through domain-driven design principles. Prioritizes clean architecture, proper service boundaries, loose coupling, and operational excellence over specific technology choices, emphasizing single responsibility and avoiding data sharing between services.

## What They Look For

### Technical Risks
- **Service coupling**: Hidden dependencies, distributed monoliths, API sprawl, tight coupling
- **Data consistency**: Transaction boundaries, eventual consistency issues, distributed transaction failures
- **Performance bottlenecks**: N+1 queries, synchronous chains, resource contention, database hotspots
- **Security vulnerabilities**: Authentication gaps, data leakage, injection attacks, service-to-service communication exposure
- **Integration complexity**: Third-party API reliability, version conflicts, contract evolution
- **Domain boundary violations**: Bounded context leakage, shared data models, domain logic spreading

### Implementation Risks
- **Service boundary violations**: Domain logic leakage, improper separation, shared code dependencies
- **API design inconsistencies**: Contract violations, versioning strategy gaps, breaking changes
- **Testing inadequacy**: Integration test gaps, contract testing missing, service mesh testing complexity
- **Documentation drift**: Outdated API docs, unclear service responsibilities, missing domain context
- **Technology proliferation**: Multiple stacks increasing complexity, polyglot persistence management challenges

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
- Increasing service response times, timeout rates, or circuit breaker activations
- Growing number of service dependencies creating coupling concerns
- Database connection pool exhaustion events or query performance degradation
- Rising infrastructure costs without corresponding traffic or business growth
- Deployment rollback frequency increases or deployment coordination complexity
- Inter-service communication errors trending up or distributed tracing showing bottlenecks
- Domain model inconsistencies appearing across service boundaries
- API versioning conflicts or breaking changes impacting multiple services
- Data consistency issues or eventual consistency resolution delays
- Service discovery failures or load balancing inefficiencies