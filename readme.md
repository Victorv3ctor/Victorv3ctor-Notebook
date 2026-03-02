# 📒 Notebook CLI — Python Backend Portfolio

## 🚀 Purpose

This project demonstrates backend engineering fundamentals including:

- Layered architecture
- Dependency injection
- Unit and integration testing
- Persistence abstraction

---


## 🏗 Architecture Diagram
``` 
                                    ┌───────────────┐
                                    │     USER      │
                                    └──────┬────────┘
                                           ↓
                                           ↓
                                    ┌───────────────┐
                                    │      UI       │
                                    └──────┬────────┘
                                           ↓
                                           ↓
                                    ┌───────────────┐
                                    │   SERVICE     │
                                    └──────┬────────┘
                                           ↓
                                           ↓
                                    ┌───────────────┐
                                    │    DOMAIN     │
                                    └──────┬────────┘
                                           ↓
                                           ↓
                                    ┌───────────────┐
                                    │  PERSISTENCE  │
                                    └───────────────┘
``` 

---

## 🛠 Technologies & Concepts Demonstrated

- Python OOP  
- Clean Architecture principles  
- Dependency Injection  
- Unit and Integration Testing  
- JSON Persistence  
- CLI Application Design  

---

## 🎨 Presentation Layer

### Files
- ui.py  
- main.py  

### Responsibilities
- User interaction  
- CLI menu rendering  
- Input validation  
- Application control flow  

The UI layer contains **no business logic**.

This separation ensures:
- Easier testing  
- Better maintainability  
- Future migration to web frontend possible  

---

## ⚙️ Service Layer (Application Orchestration)

### File
- service.py  

The service layer acts as a mediator between UI and domain logic.

Responsibilities:
- Create domain objects  
- Orchestrate workflows  
- Delegate operations to domain layer  

Example workflows:
- Add note workflow  
- Edit note workflow  
- Delete note workflow  

The service layer is intentionally thin to improve testability.

---

## 🧠 Domain Layer (Core Business Logic)

### Files
- note.py  
- notebook.py  

This layer represents the heart of the application.

Contains business entities and rules.

---

### Note Entity

Represents a single note record.

Features:
- Attribute modification methods  
- Serialization support
- String representation formatting  

---

### Notebook Aggregate

Manages note collections.

Responsibilities:
- Note storage in memory  
- Unique ID generation  
- Search operations  
- Delete operations  

---

## 💾 Persistence Layer

### File
- storage.py  

Provides storage abstraction.

Features:
- Load notes from JSON file  
- Save notes to JSON file  
- Error-safe file operations  

Future storage migrations can be implemented without modifying business logic.

---

## 🔬 Testing Strategy

Testing is implemented using **pytest + mocking techniques**.

### Unit Testing

Tested components:
- Domain entities  
- Business logic  
- Service orchestration  

---

### Integration Testing

Tested components:
- Storage serialization  
- File persistence  

Testing principles applied:
- Dependency injection  
- Behavior verification  
- Contract-based testing  

---

## 🔄 Runtime Workflow
``` 
User selects action
↓
UI processes input
↓
Service executes workflow
↓
Domain logic processes data
↓
Storage layer persists data (if needed)
``` 

---
## ⭐ Design Decisions Q&A

### Why layered architecture?

To ensure:
- Scalability  
- Testability  
- Maintainability  

---

### Why Service layer?

To separate:
- User interface logic  
- Business workflow logic  

---

### Why storage abstraction?

To allow future migration to:
- SQL databases  
- Cloud storage  
- External APIs  

---

## 🚀 Future Improvements

- Database persistence (SQLite/PostgreSQL)  
- REST API backend version  
- Authentication and authorization  
- Advanced search and filtering  

---

## 👨‍💻 Author

VictorV3ctor


