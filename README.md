# D&D Character Manager

A web application for managing and tracking *Dungeons & Dragons* (D&D) characters. The goal is to provide a centralized place to manage character information, attributes, equipment, abilities, and progression throughout an adventure.

## Features

### Character Management

- Create and manage D&D characters.
- Store character information, including name, species, class, level, and background.
- Track ability scores: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.
- Manage hit points, armor class, initiative, and movement speed.
- Track skills, proficiencies, and saving throws.

### Inventory Management

- Manage weapons, armor, equipment, and consumable items.
- Track item quantities and currency.
- Organize equipment and inventory items.

### Character Progression

- Track experience points and character levels.
- Manage spells and special abilities.
- Record character history and adventure notes.

### Data Persistence

- Store character information in a database.
- Retrieve and update characters between sessions.
- Keep character data organized and consistent.

> Features will be implemented incrementally, starting with the core character sheet and inventory management.

## Technology Stack

| Component            | Technology |
| -------------------- | ---------- |
| Frontend             | React      |
| Programming Language | TypeScript |
| Backend              | Python     |
| Backend Framework    | FastAPI    |
| Database             | SQLite     |
| API Style            | REST       |

## Project Structure

```text
dnd-character-manager/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── features/
│   │   └── services/
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   └── tests/
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Install the following software:

- Python 3.11 or later.
- Node.js and npm.
- Git.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd dnd-character-manager
```

Replace `<repository-url>` with the URL of your Git repository.

### 2. Set Up the Backend

Create and activate a Python virtual environment:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the backend dependencies once a dependency file has been created:

```bash
pip install -r requirements.txt
```

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- API: http://127.0.0.1:8000
- Interactive API documentation: http://127.0.0.1:8000/docs

### 3. Set Up the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the local URL displayed by the frontend development server.

## Development

### Backend

The backend is responsible for:

- Exposing REST API endpoints.
- Validating incoming requests.
- Managing character data.
- Applying character-related business rules.
- Interacting with the database.

### Frontend

The frontend is responsible for:

- Displaying character sheets and inventory.
- Providing forms to create and edit characters.
- Communicating with the backend API.
- Presenting character statistics and progression.

### Testing

Backend tests will be implemented using `pytest`. Frontend tests can be added using a suitable React testing framework.

## Development Roadmap

- [ ] Define the initial database schema.
- [ ] Implement character creation, retrieval, editing, and deletion.
- [ ] Create the character sheet interface.
- [ ] Implement attribute and derived-statistic calculations.
- [ ] Implement inventory management.
- [ ] Add experience and level progression.
- [ ] Implement spells and special abilities.
- [ ] Add character history and adventure notes.
- [ ] Implement automated tests.
- [ ] Improve mobile responsiveness.
- [ ] Add data export and import.

## Design Principles

- **Modularity:** Keep components and business logic separated.
- **Maintainability:** Use clear naming conventions and consistent project structure.
- **Data integrity:** Validate input and maintain consistent character data.
- **Incremental development:** Implement and test features in small, manageable steps.
- **Usability:** Make frequently used character information accessible during gameplay.

## License

The license for this project has not yet been defined.

Dungeons & Dragons and related trademarks belong to their respective owners. This project is an independent fan-made tool and is not an official D&D product.