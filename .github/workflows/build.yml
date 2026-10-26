name: Build Android APK

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Cache Buildozer global directory
        uses: actions/cache@v4
        with:
          path: ~/.buildozer
          key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}
          restore-keys: |
            ${{ runner.os }}-buildozer-

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libssl-dev libffi-dev build-essential ccache
          pip install --upgrade buildozer cython

      - name: Build APK
        run: buildozer -v android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: bin/*.apk
