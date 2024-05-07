# Architectural Drivers / Architectural Significant Requirements

## Functional Requirements

### **Document Upload**
| ID   | Requirement Description |
|------|-------------------------|
| FR1.1| The system must allow users to upload documents in various formats including PDF, DOC, DOCX, PNG, JPG, JPEG, PPM, TIFF, BMP, TXT, PPTX |
| FR1.2| The system must provide feedback on the status of the upload (e.g., success, failure due to unsupported format). |
| FR1.3| The system must securely store uploaded documents and associate them with the user's account. And must remove documents when they are no longer in use.|
| FR1.4| The system must support batch uploading of multiple documents at once. |
| FR1.5| The system must allow users to upload Panopto recordings. |
| FR1.6| The system must allow users to upload YouTube. |

### **Information Search**
| ID   | Requirement Description |
|------|-------------------------|
| FR2.1| The system must enable full-text search within all uploaded documents. |
| FR2.2| The system must return search results containing document excerpts where the search terms appear. |
| FR2.3| The system must allow filtering of search results by documents selected by the user. |

### **Learning Plans**
| ID   | Requirement Description |
|------|-------------------------|
| FR3.1| The system must allow users to create personalized learning plans. |
| FR3.2| The system must recommend a learning path based on the content of uploaded documents and the user’s goals. |
| FR3.3| The system must enable users to modify and save their learning plans persistently. |
| FR3.4| The system must provide notifications for upcoming deadlines (like dates of Exams or Tests) or recommended study sessions based on the learning plan. |

### **Flashcards and Memory Aids**
| ID   | Requirement Description |
|------|-------------------------|
| FR4.1| The system must allow users to create digital flashcards from content within uploaded documents. |
| FR4.2| The system must allow users to change the content of flashcards. |
| FR4.3| The system must allow users to delete flashcards. |
| FR4.4| The system must allow users to save flashcards persistently |
| FR4.5| The system must provide an option to export flashcards to external platforms such as Anki and Quizlet. |
| FR4.6| The system must be able to create memory aids like mnemonics and acronyms. |
| FR4.7| The system must allow users to create and share flashcard decks with others. |

### **Quiz Generation**
| ID   | Requirement Description |
|------|-------------------------|
| FR5.1| The system must automatically generate quizzes based on the content in uploaded documents and a page range. |
| FR5.2| The system must allow users to specify parameters for quiz generation (e.g., number of questions, topics covered, difficulty level). |
| FR5.3| The system must allow users to save quizzes persistently. |
| FR5.4| The system must allow users to share quizzes with others. |
| FR5.5| The system should be able to track the performance of users in quizzes. |

### **Quiz Grading**
| ID   | Requirement Description |
|------|-------------------------|
| FR6.1| The system must automatically grade quizzes. |
| FR6.2| The system must provide detailed feedback on quiz and test results, including correct answers and explanations for each question. |

### **Compendium**
| ID   | Requirement Description |
|------|-------------------------|
| FR7.1| The system must create a compendium based on the content of uploaded document in a selected page range. |
| FR7.2| The system must allow users to access and search this compendium for specific information. |

### **Study Streaks**
| ID   | Requirement Description |
|------|-------------------------|
| FR8.1| The system must track the daily engagement of users with their learning materials. |
| FR8.2| The system must display ongoing study streaks and provide motivational feedback. |
| FR8.3| The system must allow users to set goals for their study streaks. |
| FR8.4| The system should be able to send notifications to users to remind them to study. |


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
