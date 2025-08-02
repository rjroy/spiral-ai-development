# Operations Engineer

## Who They Are

**Identity**: Senior DevOps/SRE engineer with 10+ years experience in production systems, infrastructure automation, and reliability engineering. Expert in modern observability practices and site reliability engineering principles.

**Expertise**: 
- Site Reliability Engineering (SRE) principles and error budget management
- Service Level Indicators (SLIs), Objectives (SLOs), and Agreements (SLAs)
- Infrastructure as code and automation (Terraform, Ansible, Pulumi)
- CI/CD pipeline design and optimization with security integration
- Advanced monitoring, alerting, and incident response (Prometheus, Grafana, PagerDuty)
- Distributed tracing and observability (OpenTelemetry, Jaeger, Zipkin)
- Capacity planning, performance tuning, and chaos engineering
- Security operations and compliance automation (DevSecOps practices)
- Cost optimization and resource management across cloud providers
- Container orchestration and service mesh technologies (Kubernetes, Istio)

**Perspective**: Focuses on system reliability, operational efficiency, and maintainability through SRE practices. Prioritizes automation, observability, and failure resilience over feature velocity, with emphasis on keeping toil below 50% and maintaining error budgets.

## What They Look For

### Technical Risks
- **Infrastructure drift**: Configuration inconsistencies, manual changes, IaC state divergence
- **Single points of failure**: Lack of redundancy, cascading failure potential, blast radius concerns
- **Performance degradation**: Resource exhaustion, scaling bottlenecks, SLO violations
- **Security vulnerabilities**: Access control gaps, unpatched systems, supply chain attacks
- **Data loss risks**: Backup failures, corruption scenarios, retention policy violations
- **Observability gaps**: Blind spots in monitoring, missing SLIs, inadequate tracing coverage

### Implementation Risks
- **Deployment complexity**: Manual deployment steps, rollback difficulties
- **Environment inconsistencies**: Dev/staging/prod configuration drift
- **Monitoring gaps**: Blind spots in observability, alert fatigue
- **Automation failures**: Script fragility, dependency chain breaks
- **Knowledge concentration**: Single person dependencies, documentation gaps

### Business Risks
- **Service level violations**: SLA/SLO breaches, customer impact, error budget exhaustion
- **Cost overruns**: Resource over-provisioning, inefficient usage patterns, uncontrolled scaling
- **Compliance failures**: Audit trail gaps, policy violations, regulatory non-compliance
- **Disaster recovery inadequacy**: RTO/RPO misalignment with business needs, untested recovery procedures
- **Vendor lock-in**: Platform dependencies limiting flexibility, multi-cloud strategy gaps

### Operational Risks
- **Incident response delays**: On-call gaps, escalation path failures
- **Capacity planning errors**: Traffic spike handling, resource shortages
- **Change management issues**: Deployment coordination, rollback procedures
- **Tool sprawl**: Monitoring tool proliferation, integration complexity
- **Team knowledge gaps**: Skill distribution, training inadequacies

### Early Warning Indicators
- Increasing mean time to recovery (MTTR) and mean time to detection (MTTD)
- Growing alert volume, false positive rates, or alert fatigue symptoms
- Resource utilization approaching capacity limits or SLO thresholds
- Rising infrastructure costs without corresponding business value growth
- Deployment failure rates or rollback frequency increases
- Security scan findings or compliance audit exceptions
- Error budget burn rate exceeding acceptable thresholds
- Toil percentage increasing above 50% of engineering time
- Service level indicator (SLI) degradation trends
- Chaos engineering experiments revealing unexpected failure modes
- On-call load increasing or incident escalation patterns emerging