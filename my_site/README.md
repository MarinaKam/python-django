# 🚀 Django on AWS Elastic Beanstalk with RDS — How It *Actually* Works

## 📌 TL;DR:
This is how we deployed a Django app to AWS using Elastic Beanstalk and PostgreSQL (RDS) — **with all the real-life issues, frustrations, and solutions**. 100% hands-on.

---

## 🔧 1. Preparing Your Django Project

- `requirements.txt` must include:
  ```txt
  Django>=5.2
  psycopg2-binary
  ```

- `wsgi.py` in the `my_site/` directory must contain:
  ```python
  from django.core.wsgi import get_wsgi_application
  application = get_wsgi_application()
  ```

- In the root of your project, create `.ebextensions/django.config`:
  ```yaml
  option_settings:
    aws:elasticbeanstalk:container:python:
      WSGIPath: my_site.wsgi:application
  ```

- Zip your project (⚠️ do not include a wrapping folder):

  ```bash
  zip -r app.zip . -x "*.git*" "__pycache__/*"
  ```

---

## 🌍 2. Installing EB CLI on Mac (ARM/M1/M2)

```bash
arch -arm64 brew install awsebcli
```

Using plain `brew install awsebcli` gives this error:  
> Cannot install under Rosetta 2

Check if it works:

```bash
eb --version
```

---

## 🔐 3. AWS IAM Permissions

You create an IAM user `eb-cli`, but then:

> ❌ **Error**: NotAuthorizedError — `ec2:ImportKeyPair`

### 💥 Fix:
Manually attach the following policies to the IAM user:

- `AWSElasticBeanstalkFullAccess`
- `AmazonRDSFullAccess`
- `AmazonS3FullAccess` *(optional for file uploads)*
- ✅ `AmazonEC2FullAccess` — **required for `eb ssh --setup` to work**

Without `AmazonEC2FullAccess`, SSH setup fails silently. AWS won't warn you clearly.

---

## ⚙️ 4. EB CLI Initialization

```bash
eb init
```

- Region: `us-east-2` (or wherever your EB and RDS are)
- Choose an existing or new app
- Platform: Python
- CodeCommit: ❌ No

---

## 🔐 5. Setting Up SSH

```bash
eb ssh --setup
```

AWS shows a scary warning:

> ⚠️ Your existing instances will be terminated

**This is expected.** Confirm, generate a keypair. You need this for `eb ssh` to work.

---

## 🧬 6. Creating the RDS Database (PostgreSQL)

In AWS Console → RDS → Create DB:

- Public access: ✅ Yes (at least for debugging)
- VPC security group: must match your EB environment
- Save: endpoint, port, username, password

---

## ⚙️ 7. Database Config in `settings.py`

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("RDS_DB_NAME"),
        'USER': os.getenv("RDS_USERNAME"),
        'PASSWORD': os.getenv("RDS_PASSWORD"),
        'HOST': os.getenv("RDS_HOSTNAME"),
        'PORT': os.getenv("RDS_PORT", "5432"),
    }
}
```

---

## 🌱 8. Add Environment Variables

In EB Console → Environment → Configuration → Software:

```
RDS_DB_NAME
RDS_USERNAME
RDS_PASSWORD
RDS_HOSTNAME
RDS_PORT
```

---

## ⚠️ 9. The `migrate` Timeout Error

```bash
python manage.py migrate
```

> ❌ connection to server timed out...

### Why?
You cannot access RDS directly from your local machine.  
You *must* run migrations **via your EB EC2 instance**.

---

## ✅ 10. Run Migrations Correctly

```bash
eb ssh
cd /var/app/current
source /var/app/venv/*/bin/activate
python manage.py migrate
```

---

## 🛠️ 11. Real Problems We Faced

| Problem | Solution |
|--------|----------|
| `zsh: command not found: eb` | Install via `arch -arm64 brew install awsebcli` |
| `connection to RDS timed out` | Only run `migrate` via `eb ssh`, never locally |
| `ec2:ImportKeyPair` denied | Add `AmazonEC2FullAccess` to IAM user |
| `/Users/.../.ssh/... already exists` | Hit `y` to overwrite the key |
| `Health: Degraded` in EB | Check `requirements.txt`, `wsgi`, `WSGIPath`, and logs |

---

## ✅ All Good Now!

You can deploy via:

```bash
eb deploy
```

And connect to your instance:

```bash
eb ssh
```

---

## 🔁 Auto Migrations (Optional)

Create `.ebextensions/01_migrate.config`:

```yaml
container_commands:
  01_migrate:
    command: "python manage.py migrate --noinput"
    leader_only: true
```

---

## 🧠 Final Word

AWS is powerful, but requires **patience, swearing, and setup time**.  
This README is here to make sure *you* don't trip over the same stuff tomorrow.


``
export APP_HOST=localhost
export IS_DEVELOPMENT=True
``
