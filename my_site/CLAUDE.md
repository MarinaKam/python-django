# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Django Management
- `python manage.py runserver` - Start development server (default: http://127.0.0.1:8000/)
- `python manage.py makemigrations` - Create database migrations
- `python manage.py migrate` - Apply database migrations
- `python manage.py createsuperuser` - Create admin user
- `python manage.py collectstatic` - Collect static files
- `python manage.py shell` - Open Django shell
- `python manage.py test` - Run tests

### Database Operations
- `python manage.py dbshell` - Open database shell (SQLite)
- `python manage.py dumpdata` - Export data
- `python manage.py loaddata` - Import data

## Architecture Overview

This is a Django 5.2.4 blog application with the following structure:

### Core Components
- **Project**: `my_site` - Main Django project containing settings and root URL configuration
- **App**: `blog` - Single Django app handling all blog functionality
- **Database**: SQLite (development) with models for Posts, Authors, and Tags
- **Templates**: Django templates with inheritance using `base.html`
- **Static Files**: CSS and images organized per app with global static directory

### Data Models
- `Post`: Blog posts with title, excerpt, content, slug, date, author (FK), and tags (M2M)
- `Author`: Authors with first_name, last_name, unique email_address
- `Tag`: Simple tags with caption field
- Relationships: Post -> Author (many-to-one), Post -> Tag (many-to-many)

### URL Structure
- `/` - Homepage showing latest 3 posts
- `/posts` - All posts listing
- `/posts/<slug>` - Individual post detail
- `/admin/` - Django admin interface

### Current State
- Models are defined but views still use hardcoded data (`all_posts` list in views.py)
- Database migrations exist but application is in transition from static to dynamic data
- Admin interface is configured for model management
- Static files include per-app CSS and shared global styles

### Template Structure
- Base template: `templates/base.html`
- Blog templates: `blog/templates/blog/` (index.html, all-posts.html, post-detail.html)
- Includes: `blog/templates/blog/includes/post.html` for reusable post display

### Settings Notes
- Development mode with DEBUG=True
- Uses default Django secret key (should be changed for production)
- Static files served from both app-level and project-level static directories
- Templates directory configured at project root level