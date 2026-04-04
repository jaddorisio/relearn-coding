# DevOps and Security

Deployment code is just as critical as architectural system code. The state of production environments should be reproducible, verifiable, and strictly controlled.

## CI/CD Pipeline Automation
- **Continuous Integration (CI):** Automating the execution of linters, code formatters, static-type checking, and the complete test suite upon every commit before code merges. Never run format issues ad-hoc.
- **Continuous Deployment (CD):** Pushing fully verified artifacts into production without requiring manual zip-folders or FTP dropping. All code deployment must involve a predictable, trackable process.

## GitOps and Infrastructure as Code (IaC)
- Treat `git` as the single source of absolute truth for environments.
- Whether a database needs updating, an AWS server scaling up, or a firewall policy changing, it should be defined explicitly via human-readable text code (e.g., Terraform, Ansible) inside a repository rather than someone clicking a manual web UI button.

## Safe Releasing Patterns
Decouple the "Deployment" (putting code onto server instances) from the "Release" (switching on traffic to end users).
- **Feature Flags:** Hiding incomplete code blocks behind remote configuration toggles, allowing code to be continuously integrated onto the main branch safely.
- **Canary Rolling:** Putting the shiny new code onto 5% of web servers to evaluate memory errors or exceptions over time before exposing the rest of the users.
- **Blue/Green Deployments:** Spinning up the entirety of the brand new `Green` architecture alongside the exact old running `Blue` architecture. Flipping the router DNS from Blue to Green simultaneously provides immediate zero-downtime switchovers and immediate rollback ability if things shatter.

## The Pillars of Observability
- Attempting to deduce production issues via unstructured print terminals is highly ineffective when hundreds of nodes are involved.
- **Logs:** A discrete record of events. (e.g., `Failed logging in. API route rejected.`). Must be aggregated to a central repository.
- **Metrics:** A structured numeric representation of state monitored over intervals to trigger alerts. (e.g., `Node memory usage spiking at 90%`).
- **Distributed Traces:** A unique identifier passed through the call-stack across disparate micro-services mapping a single user-request’s timeline completely. 

## Zero Trust and Secure by Design
- Always assume bad actors operate successfully inside your private network walls.
- Follow the Principle of Least Privilege: Provide code only the fundamental IAM permissions immediately required to run.
- Keep API Keys out of code completely (`.env`/AWS Secrets).
- Encrypt everything at rest and in transit.
- Integrate software composition scanning inherently deep into the DevOps pipeline ("Shift Security Left".)
