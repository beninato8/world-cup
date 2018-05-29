import os

d = os.path.dirname(os.path.realpath(__file__)) + '/../../../'
cmd = """osascript << EOF
tell application "Terminal"
activate
do script with command \"cd """ + d + """\"
end tell
EOF
"""

os.system(cmd)
