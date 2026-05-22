@echo off
cd C:\Auto_Traffic_Empire
start /b py crawler_builder.py
start /b py git_sync.py
start /b py pinterest_poster.py