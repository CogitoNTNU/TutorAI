# Architecture

## Quality Attribute Scenarios

- **Usability**:

#### An end user wants to ask a questions to a given book during the enitire semester.

| Portion of scenario | Value                                                                       |
| ------------------- | --------------------------------------------------------------------------- |
| Source              | End user (normal user)                                                      |
| Stimulus            | Uploads a pdf to the system                                                 |
| Artifact            | Database, server                                                            |
| Enviroment          | Persistence                                                                 |
| Response            | Add tensor and pdf file to the database, only accessable for the given user |
| Response measure    | The user can access the file until it is deleted by user                    |

- **Performance**:

#### Lots of end users using system sitaiously.

| Portion of scenario | Value                         |
| ------------------- | ----------------------------- |
| Source              | 1000 end users                |
| Stimulus            | 3000 requests in a 30 seconds |
| Artifact            | System                        |
| Enviroment          | Normal Opertations            |
| Response            | All requests are served       |
| Response measure    | Sucess rate at least 99%      |

- **Security**: The system must be secure to protect the user's data and financial information. It is important that the system is secure to prevent unauthorized access to the system as the API keys are stored in the system.

#### S1: System expiriences DoS

| Portion of scenario | Value                                   |
| ------------------- | --------------------------------------- |
| Source              | 1 end users                             |
| Stimulus            | 500 requests to backend in a 60 seconds |
| Artifact            | System                                  |
| Enviroment          | Normal Opertations                      |
| Response            | User gets timeout                       |
| Response measure    | User must be timeout within 30 seconds  |

#### S2: Uploading of inapropriate content

| Portion of scenario | Value                              |
| ------------------- | ---------------------------------- |
| Source              | An end user                        |
| Stimulus            | Tries to Uploads illegal content   |
| Artifact            | System                             |
| Enviroment          | Normal Operations                  |
| Response            | Content is flagged and rejected    |
| Response measure    | Content rejected within 20 seconds |

#### S3: API keys exposed

| Portion of scenario | Value                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| Source              | Unkown                                                                   |
| Stimulus            | Production API key exposed                                               |
| Artifact            | API Key                                                                  |
| Enviroment          | Normal Operations                                                        |
| Response            | API Key should be deactivated                                            |
| Response measure    | An spare API Key should be injected into production in less then an hour |

#### S4: Unauthorized access attempt

| Portion of scenario | Value                                        |
| ------------------- | -------------------------------------------- |
| Source              | Malicious user                               |
| Stimulus            | Attempts to access restricted data           |
| Artifact            | User authentication and authorization system |
| Enviroment          | Normal Operations                            |
| Response            | Access is denied and logged                  |
| Response measure    | Denial and logging occur within 2 seconds    |

#### S5: Data breach attempt

| Portion of scenario | Value                                        |
| ------------------- | -------------------------------------------- |
| Source              | Malicious user                               |
| Stimulus            | Attempts to breach sensitive user data       |
| Artifact            | Database and network security                |
| Enviroment          | Normal operations                            |
| Response            | Intrusion detected and connection terminated |
| Response measure    | Connection termination within 1 second       |

- **Modifiability**:

#### M2: The system must be able to change COTS (Commercial Off-The-Shelf) components with only local changes.

| Portion of scenario | Value                                                          |
| ------------------- | -------------------------------------------------------------- |
| Source              | Developer                                                      |
| Stimulus            | Changes a COTS                                                 |
| Artifact            | TutorAI backend                                                |
| Enviroment          | Development time                                               |
| Response            | COTS should be easy to change                                  |
| Response measure    | COTS shoul be changed within one hour wihtout any side effects |

#### M4 The system must be able to easily change database without any side effects

| Portion of scenario | Value                                                          |
| ------------------- | -------------------------------------------------------------- |
| Source              | Developer                                                      |
| Stimulus            | Changes the database                                           |
| Artifact            | TutorAI backend                                                |
| Enviroment          | Development time                                               |
| Response            | New database should be easy to add                             |
| Response measure    | New databese is added within 3 hours whithout any side effects |

**Other relevant quality attributes**

- **Availability**:

#### A1: System uptime must be 99%, with capabilities to handle critical operations around the clock.

| Portion of scenario | Value                         |
| ------------------- | ----------------------------- |
| Source              | 1000 end users                |
| Stimulus            | 3000 requests in a 30 seconds |
| Artifact            | System                        |
| Enviroment          | API calls, normal operation   |
| Response            | Tokens will not run out       |
| Response measure    | Sucess rate at least 99%      |

- **Integrability**:
- **Testability**:

**Not so relevant quality attributes**

- **Deployability**:
- **Energy efficiency**:
- **Safety**: The system is not safety critical.

The system should not display any harmfull ideas or language.
(chat gpt content filter)

| Portion of scenario | Value                                                            |
| ------------------- | ---------------------------------------------------------------- |
| Source              | 1 end user                                                       |
| Stimulus            | Ask questions of harmful or unlawful nature                      |
| Artifact            | System                                                           |
| Enviroment          | API calls, normal operation                                      |
| Response            | Language model's content filter should not allow harmful content |
| Response measure    | No harmful content in at least 99% of responses                  |
