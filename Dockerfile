FROM node:10.9.0 as builder

WORKDIR /srv/unbabel

# Copy files necessary to run NPM CI and install
COPY package-lock.json package.json ./

# Install NPM dependencies
RUN npm ci

# Copy files necessary to build assets
COPY project project
COPY .babelrc jest.config.js postcss.config.js webpack.config.js ./

# Build assets
RUN APP_ENV=production npm run build

# Final python image
FROM python:3.6

WORKDIR /srv/unbabel

# Copy dependencies file for pip install
COPY requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY config.py manage.py uwsgi.ini ./
COPY project project
COPY .git .git

COPY --from=builder /srv/unbabel/project/static/dist project/static/dist

EXPOSE 8080
CMD ["newrelic-admin", "run-program", "uwsgi", "--ini", "uwsgi.ini"]
