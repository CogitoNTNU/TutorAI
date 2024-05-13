# Architectural Design

## Quality Attribute Scenarios
See [Quality Attribute Scenarios](quality_attribute_scenarios.md)

## Architectural Drivers / Architecturally Significant Requirements (ASRs) 
See [Architectural Drivers](requirements.md)

## Components

The TutorAI uses the following COTS components:
[COTS Components](cots.md)

## Stakeholders and Concerns
See [Stakeholders and Concerns](stakeholders.md)

## Architectural tactics and patterns


### Tactics


| Tactic                                       | Affected Quality Attribute | Reasoning                                                                                  |
|----------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------|
| Cloud-based Hosting                          | Performance, Availability  | Ensures scalability and high availability through cloud services.                          |
| Increase Resources                           | Performance, Availability  | Handles increased load by employing robust hardware and additional servers.                |
| Schedule Resources                           | Performance                | Optimizes performance by dynamically allocating resources based on demand.                 |
| Continuous Deployment                        | Deployability               | Allows for updates without downtime, maintaining high availability.                        |
| Reduce Size of Modules                       | Modifiability              | Breaks down modules into smaller, more manageable components.                              |
| Increase Cohesion                            | Modifiability              | Ensures each module has a single, well-defined purpose.                                    |
| Encapsulate                                  | Modifiability              | Limits dependencies by encapsulating functionalities.                                      |
| Use an Intermediary                          | Modifiability              | Manages interactions between modules through intermediaries.                               |
| Restrict Dependencies                        | Modifiability              | Minimizes dependencies between modules.                                                    |
| Abstract Common Services                     | Modifiability              | Creates common services that can be reused across the system.                              |
| Defer Binding                                | Modifiability              | Increases flexibility by delaying the binding of components until needed.                  |
| Prioritize Events                            | Modifiability              | Manages event priorities to handle critical operations efficiently.                        |
| Introduce Concurrency                        | Modifiability              | Improves responsiveness by implementing concurrent processing.                             |
| Heartbeat Monitoring                         | Availability                | Regularly checks the health of the system to detect and respond to failures.               |
| Throttling                                   | Performance                | Prevents server overload and ensures consistent performance by implementing rate limiting. |
| Detect Service Denial (DDoS) Attacks         | Security                   | Monitors and mitigates DDoS attacks.                                                       |
| Encrypt Data                                 | Security                   | Ensures data is encrypted both in transit and at rest.                                     |
| Detect Intrusion                             | Security                   | Monitors and responds to security breaches through intrusion detection systems.            |
| Authenticate Actors                          | Security                   | Verifies the identity of users and systems.                                                |
| Authorize Actors                             | Security                   | Controls access to resources based on user roles and permissions.                          |
| Limit Access                                 | Security                   | Restricts access to sensitive areas of the system.                                         |
| Limit Exposure                               | Security                   | Minimizes the exposure of the system's internal structures and data.                       |
| Revoke Access                                | Security                   | Ensures access can be revoked quickly if necessary.                                        |
| Maintain Audit Trail                         | Security                   | Keeps a detailed log of system activities for monitoring and forensic analysis.            |
| Restore Data                                 | Security                   | Ensures data can be restored quickly in the event of corruption or loss.                   |
| Maintain Task Model                          | Usability                  | Continuously updates the model of user tasks to ensure the system remains user-friendly.    |
| User Model                                   | Usability                  | Maintains an understanding of the user base to tailor interactions and improve UX.         |
| System Model                                 | Usability                  | Keeps a model of system interactions to ensure predictable and intuitive behavior.         |

### Patterns

The application uses client-server architecture with a multi-tier architecture. The client is a web browser that communicates with the server using HTTPS. The server is a RESTful API. The server is hosted on a cloud-based service. The application uses a layered architecture with the following layers: presentation, logic and data tier. 



## Architectural Viewpoints

### Physical View
*The physical view should describe how the software is allocated to
hardware. This includes the client, the server, and network connections you develop
and other services you use (like cloud-based services, etc.). A typical notation for this
view is a deployment diagram.*

### Logical View
*It is recommended to use multiple diagrams for this view, e.g., provide
one high-level diagram and one or more diagrams for more detail. Typical notations
for this view include a UML class diagram, UML package diagram, layers diagram,
ER diagram, and combination of UML class and package diagrams.*

### Process View
*It is also recommended to use multiple diagrams for the view to give a
complete description of the run-time behavior of the system. Typical notations for this
view include a UML activity diagram, a UML state diagram, and a UML sequence
diagram.*

### Development View
*The purpose of the development view is to make it easier to
allocate work to various team members and make it possible to allow development in
parallel. Based on this view, it should be easy to give programming tasks to group
members and make it easy to integrate the results after completion with the rest of the
system*

## Architectural Rationale 
