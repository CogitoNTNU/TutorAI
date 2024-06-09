# Architectural Drivers / Architectural Significant Requirements
This document outlines the architectural drivers and significant requirements for the TutorAI system. It includes both functional and non-functional (quality) requirements that define the system's behavior, performance, and operational characteristics. The goal is to ensure that TutorAI meets the needs of its users and [Stakeholders](stakeholders.md) while maintaining a high standard of quality.

## Functional Requirements
*Functional requirements define the specific behaviors, actions, and functionalities that the TutorAI system must provide to its users. They describe what the system will do under various conditions, detail the operations and activities the system must be capable of performing, and outline the explicit services it should deliver.*

The functional requirements are divided into three different priorities: 
| Priority | Description |
|----------|-------------|
| High     | These requirements are essential for the system to function properly; without these, there will be a significant impact on the system's ability to provide an enjoyable experience. |
| Medium   | These requirements are important but not critical for the system to function properly. |
| Low      | These requirements are nice-to-have features that would enhance the system but are not essential for its core functionality. |

All functional requirements are listed below:

### **Document Upload**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR1.1| The system must allow users to upload documents in various formats including PDF, DOC, DOCX, PNG, JPG, JPEG, PPM, TIFF, BMP, TXT, PPTX | High |
| FR1.2| The system must provide feedback on the status of the upload (e.g., success, failure due to unsupported format). | High |
| FR1.3| The system must securely store uploaded documents and associate them with the user's account. And must remove documents when they are no longer in use.| High |
| FR1.4| The system must support batch uploading of multiple documents at once. | Low |
| FR1.5| The system must allow users to upload Panopto recordings. | Medium |
| FR1.6| The system must allow users to upload YouTube recordings. | Low |
| FR1.7| The system must allow users to upload locally if they want to. | Low |

### **Information Search**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR2.1| The system must be able to search within all uploaded documents for relevant citations of curriculum based on user query. | High |
| FR2.2| The system must allow filtering of search results by documents selected by the user. | High |
| FR2.3| The system must handle queries specifically for citations. | Medium |
| FR2.4| The system must handle queries in different languages. | Medium |
| FR2.5| The system must be able to retrieve and display images from the the uploaded file. | Low |



### **Learning Plans**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR3.1| The system must allow users to create personalized learning plans. | Medium |
| FR3.2| The system must recommend a learning path based on the content of uploaded documents and the user’s goals. | Low |
| FR3.3| The system must enable users to modify and save their learning plans persistently. | Low |
| FR3.4| The system must provide notifications for upcoming deadlines (like dates of Exams or Tests) or recommended study sessions based on the learning plan. | Low |

### **Flashcards and Memory Aids**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR4.1| The system must allow users to create digital flashcards from content within uploaded documents. | High |
| FR4.2| The system must allow users to change the content of flashcards. | Medium |
| FR4.3| The system must allow users to delete flashcards. | Medium |
| FR4.4| The system must allow users to save flashcards persistently | High |
| FR4.5| The system must provide an option to export flashcards to external platforms such as Anki and Quizlet. | High |
| FR4.6| The system must be able to create memory aids like mnemonics and acronyms. | Medium |
| FR4.7| The system must allow users to create and share flashcard decks with others. | Low |


### **Quiz Generation**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR5.1| The system must automatically generate quizzes based on the content in uploaded documents and a page range. | High |
| FR5.2| The system must allow users to specify learning goals and generate quizzes based on these goals. | Medium |
| FR5.3| The system must allow users to save quizzes persistently. | High |
| FR5.4| The system must allow users to share quizzes with others. | Low |
| FR5.5| The system should be able to track the performance of users in quizzes. | Low |

### **Quiz Grading**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR6.1| The system must automatically grade quizzes. | High |
| FR6.2| The system must provide detailed feedback on quiz and test results, including correct answers and explanations for each question. | High |

### **Compendium**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR7.1| The system must create a compendium based on the content of uploaded document in a selected page range. | High |
| FR7.2| The system must allow users to access and search this compendium for specific information. | High |
| FR7.3| The system must allow users to save the compendium persistently. | Medium |
| FR7.4| The system must allow users to share the compendium with others. | Low |

### **Study Streaks**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR8.1| The system must track the daily engagement of users with their learning materials. | Medium |
| FR8.2| The system must display ongoing study streaks and provide motivational feedback. | Medium |
| FR8.3| The system must allow users to set goals for their study streaks. | Low |
| FR8.4| The system should be able to send notifications to users to remind them to study. | Low |


### **User Registration**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR9.1| The system must allow users to register for an account. | Medium |
| FR9.2| The system must allow users to log in to their account. | Low |
| FR9.3| The system must allow users to logout of their account | Low |
| FR9.4| The system must allow users to reset their password. | Low |
| FR9.5| The system must allow users to delete their account. | Low |

### **Reading**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR10.1| The system must allow users to read the documents they have uploaded. | Medium |


## Quality Attributes
*Quality attributes are the system's non-functional requirements that specify the system's operational characteristics. They define the system's behavior, performance, and other qualities that are not directly related to the system's functionality.*

### **Usability**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| U1 | The system must have an intuitive interface that allows users to understand essential functions within 30 seconds. | High |
| U2 | The system must provide feedback on the status of the upload (e.g., success, failure due to unsupported format). | High |
| U3 | 	The system must comply with WCAG 2.1 Level AA guidelines to ensure accessibility for users with disabilities. | Medium |
| U4 | 	Instruction manual will be accessible, so that a user may ask the chat function about how to use it. | Low |

### **Performance**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| P1 | The system must support up to 1,000 concurrent users with RAG search response times not exceeding 5 seconds. | High |
| P2 | The system must flexibly scale to accommodate increased demand, especially during peak periods like Exams. | High |
| P3 | The system must be able to upload any document of reasonable lenght in less then 5 minutes | High |
| P4 | The system must be able to generate quizzes in less than 30 seconds | High |
| P5 | The system must be able to grade quizzes in less than 10 seconds | High |
| P6 | The system must be able to generate flashcards of 10 pages in less than 30 seconds | High |
| P7 | The system must be able to generate a compendium of 10 pages in less than 60 seconds | High |

### **Deployment**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| D1 | The system must enable straightforward deployment processes for updates and new features that introduce zero downtime or defects. | High |
| D2 | The system must support automated deployment to streamline the release process. | Medium |

### **Availability**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| A1 | System uptime must be 99%, with capabilities to handle critical operations around the clock. | Medium |
| A2 | The system must be able to recover from failures within 15 minutes. | Low |
| A3 | The system must have redundant failover mechanisms to ensure continuity during outages. | Low |

### **Testability**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| T1 | The system must be designed to allow efficient testing of new features and updates to ensure functionality without extensive manual intervention. | High |
| T2 | The system must have a test suite that covers all essential features | High |
| T3 | The system must be able to mock external services for testing | Medium |

### **Modifiability**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| M1 | The system must be designed to allow for easy modification and extension of features without significant rework or refactoring. | High |
| M2 | The system must be able to change COTS (Commercial Off-The-Shelf) components with only local changes.| High |
| M3 | The system must be able to get new functionalities without much refactoring of existant code.| High |
| M4 | The system must be able to easily change database without any side effects | High |

### **Security**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| S1 | The system must be secure to protect the user's data and financial information. | High |
| S2 | The system must be able to detect and prevent unauthorized access to the system. | High |
| S3 | The system must be able to restore user generated data in case of a security breach | low |
| S4 | The system must encrypt all sensitive user data at rest and in transit. | High |
| S5 | The system must perform regular security audits and vulnerability assessments. | Low |

### **Safety**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| Sa1  | The system should not display any harmfull ideas or language.| Low |

## Business Requirements
*Business requirements are the high-level needs of the business that the system must meet to fulfill its purpose. They define the system's strategic goals, objectives, and constraints that guide the system's development and operation.*

The Business Requirements for TutorAI are not yet defined. They will be added once they are finalized.
### **Market Penetration and User Base**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|


### **Revenue Generation**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| B2.1 | Cost of services should not exceed the revenue | High |

### **Partnerships and Integrations**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|


### **User Engagement and Retention**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|

### **Customer Satisfaction**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|

### **Compliance and Standards**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| BR6.1| The system must comply with GDPR and other relevant data protection regulations. | High |
| BR6.2| The system must compy with copyright laws | High | 

### **Cost Management**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|

