set -eu

export PYTHONUNBUFFERED=true

PYTHON_EXECUTABLE=$(which python3.8)

if [ -z "$PYTHON_EXECUTABLE" ]; then
  echo "Python 3.8 or newer is required."
  exit 1
fi

VIRTUALENV=.data/venv

if [ ! -d $VIRTUALENV ]; then
  $PYTHON_EXECUTABLE -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/pip install -r requirements.txt

$VIRTUALENV/bin/python app.py
