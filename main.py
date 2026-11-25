import os

# Verified count: 94 characters (94 UTF-8 bytes).
LINE = (
    "One star. The tree leaked sap on my keyboard, "
    "and now every email I send sticks to the screen."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8", newline="") as fh:
    fh.write(LINE)

print(len(LINE.encode("utf-8")))
