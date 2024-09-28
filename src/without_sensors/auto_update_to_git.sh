#!/bin/bash
while true; do
	git add -A && git commit -m "auto update" && git push origin main
	/bin/sleep 320
done
