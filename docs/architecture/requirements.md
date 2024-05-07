# Architectural Drivers / Architectural Significant Requirements

## Functional Requirements
*Functional requirements define the specific behaviors, actions, and functionalities that the TutorAI system must provide to its users. They describe what the system will do under various conditions, detail the operations and activities the system must be capable of performing, and outline the explicit services it should deliver.*

The functional requirements are divided into three different priorities: 
| Priority | Description |
|----------|-------------|
| High     | These requirements are essential for the system to function properly, without these there will be a significant impact on the system's ability to give an enjoyable experience. |
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

### **Information Search**
| ID   | Requirement Description | Priority |
|------|-------------------------|----------|
| FR2.1| The system must be able to search within all uploaded documents for relevant citations of curriculum based on user query. | High |
| FR2.2| The system must allow filtering of search results by documents selected by the user. | High |


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


## Quality Attributes

## Business Requirements
