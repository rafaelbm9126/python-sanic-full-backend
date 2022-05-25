cd src/
mkdir upload_file
sanic server:power --host=0.0.0.0 --port=8080 --fast --debug --auto-reload --reload-dir=*
