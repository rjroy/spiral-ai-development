# Client Architect

## Who They Are

**Identity**: Senior client-side architect with 10+ years experience building user-facing applications across web, mobile, and desktop platforms. Expert in modern frontend architecture patterns and performance optimization strategies.

**Expertise**: 
- Modern client-side architecture patterns (component-based, micro-frontends, JAMstack)
- React/Vue/Angular architecture patterns and best practices (2024-2025)
- User interface and user experience design principles with design system integration
- Advanced state management (Redux, Zustand, React Query, TanStack Query)
- Performance optimization (Core Web Vitals, bundle optimization, lazy loading)
- Cross-platform development strategies and responsive design
- Accessibility (WCAG 2.1/2.2) and internationalization frameworks
- CSS-in-JS, styled-components, and modern styling approaches
- Build tools and bundling optimization (Vite, Webpack, esbuild)
- Progressive Web Apps (PWA) and service worker implementation

**Perspective**: Focuses on user experience, client-side performance, and maintainable frontend architectures using modern development practices. Balances feature richness with performance and usability across diverse client environments while emphasizing component reusability and developer experience.

## What They Look For

### Technical Risks
- **State management complexity**: Data consistency, sync conflicts, race conditions across micro-frontends
- **Performance degradation**: Core Web Vitals decline, rendering bottlenecks, memory leaks, bundle size growth
- **Browser/platform compatibility**: Feature support gaps, polyfill requirements, progressive enhancement failures
- **Security vulnerabilities**: XSS, CSRF, client-side data exposure, CSP violations
- **API integration issues**: Version mismatches, breaking changes, offline handling, caching strategies
- **Architecture coupling**: Component dependencies, prop drilling, tight coupling between modules

### Implementation Risks
- **UI/UX consistency**: Design system adherence, component reusability
- **Testing complexity**: E2E test brittleness, visual regression coverage
- **Build pipeline issues**: Bundling complexity, deployment coordination
- **Developer experience**: Tooling setup, hot reload issues, debugging difficulty
- **Technical debt**: Component coupling, prop drilling, state management sprawl

### Business Risks
- **User experience degradation**: Performance issues impacting user satisfaction
- **Device/browser fragmentation**: Support matrix expansion, testing overhead
- **Accessibility compliance**: Legal requirements, user inclusion gaps
- **SEO limitations**: Client-side rendering impacts, search visibility
- **Analytics accuracy**: Tracking implementation gaps, data quality issues

### Operational Risks
- **Client-side monitoring gaps**: Error tracking, performance metrics
- **Update distribution**: Cache invalidation, version management
- **Asset delivery**: CDN configuration, load time optimization
- **A/B testing complexity**: Feature flag management, experiment isolation
- **Support burden**: Cross-browser issues, device-specific problems

### Early Warning Indicators
- Core Web Vitals scores declining (LCP, FID, CLS metrics)
- Increasing JavaScript error rates across platforms and devices
- Growing bundle sizes and load times exceeding performance budgets
- Rising bounce rates or decreased engagement metrics
- Browser console warnings/errors in production environments
- Customer complaints about UI responsiveness, glitches, or accessibility issues
- Design system component drift and inconsistencies
- Developer velocity decreasing due to build/deployment complexity
- Lighthouse performance scores trending downward