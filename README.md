# 1fan

A Patreon-like platform that leverages cryptocurrency for borderless creator support, enabling fans worldwide to support their favorite creators without traditional financial barriers.

Visit us at [1fan.today](https://1fan.today)

## Features

- Borderless cryptocurrency payments
- Creator subscription models
- Secure and transparent transactions
- Global accessibility

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy (async), PostgreSQL
- **Frontend**: HTML5, Jinja2 templates, Stimulus.js, Stacks Icons
- **Infrastructure**: Docker, Nginx, PostgreSQL
- **Tools**: Alembic (migrations), uvicorn (server)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd 1fan
   ```

2. Create a `.env` file with the following variables:
   ```
   POSTGRES_DB=your_db_name
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_PORT=5432
   ```

3. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Access the application at `http://localhost`

## Usage

- Visit the homepage to check database connectivity
- API status endpoint: `/api/status`

## Development

- Backend code is in `app/`
- Frontend templates in `app/templates/`
- Static assets in `static/`
- Nginx configuration in `nginx/`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

ISC