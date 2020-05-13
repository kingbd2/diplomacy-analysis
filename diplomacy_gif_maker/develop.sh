#!/usr/bin/env bash
# gnome-terminal -- uvicorn api.main:app --reload
gnome-terminal -e 'sh -c "cd frontend; yarn dev"'