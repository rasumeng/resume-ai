def clean_bullets(text: str) -> str:
    lines = text.strip().split("\n")
    cleaned = []
    for line in lines:
        line = line.strip()
        if line:
            # Remove leading numbers like "1." "2." etc
            if line[0].isdigit() and line[1] in ".):":
                line = "- " + line[2:].strip()
            cleaned.append(line)
    return "\n".join(cleaned)
