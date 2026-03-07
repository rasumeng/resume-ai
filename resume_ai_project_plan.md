# Resume/LinkedIn Helper AI — Project Plan
### Stack: Local LLM | Python | PDF Output

---

## 🗂 Project Overview

| Item | Decision |
|---|---|
| LLM Runtime | Local / Offline (Ollama + LLaMA 3 or Mistral) |
| Interface | CLI first → optional web UI later |
| Core Features (v1) | Bullet polish, Job tailoring, Experience updater |
| Output Format | PDF |
| Language | Python 3.10+ |

---

## 🏗 Architecture (High Level)

```
User Input (raw text / old resume / job description)
        ↓
  Input Parser (extract sections: summary, experience, skills)
        ↓
  Prompt Builder (select template based on task type)
        ↓
  Local LLM (Ollama API call → LLaMA 3 / Mistral 7B)
        ↓
  Output Cleaner (strip artifacts, enforce formatting rules)
        ↓
  PDF Generator (ReportLab or WeasyPrint)
        ↓
  Final PDF Resume Output
```

---

## 📦 Tech Stack

| Layer | Tool | Why |
|---|---|---|
| LLM Runtime | [Ollama](https://ollama.com) | Dead-simple local model serving |
| LLM Model | LLaMA 3 8B or Mistral 7B | Great instruction-following, runs on 8–16GB RAM |
| Python LLM Client | `ollama` Python SDK or `requests` | Lightweight, no LangChain overhead for v1 |
| PDF Generation | `reportlab` or `weasyprint` | Clean PDF output from Python |
| Input Parsing | `pdfplumber` or plain text | Read existing resume text |
| CLI Interface | `argparse` or `typer` | Clean command-line UX |
| Environment | `venv` + `requirements.txt` | Simple, reproducible setup |

---

## 🚀 Phase Breakdown

### Phase 1 — Foundation (Week 1)
**Goal:** Get local LLM running and producing usable resume output.

- [ ] Install Ollama, pull LLaMA 3 8B or Mistral 7B
- [ ] Write a basic Python script to send prompts to Ollama
- [ ] Build 3 core prompt templates (see below)
- [ ] Test each template with a sample resume
- [ ] Validate output quality — iterate on prompts until consistent

**Done when:** You can paste a bullet point in, and get a polished one back via CLI.

---

### Phase 2 — Input/Output Pipeline (Week 2)
**Goal:** Accept real resume files and produce a structured PDF.

- [ ] Build input parser: accept `.txt` or `.pdf` resume as input
- [ ] Extract resume sections (Summary, Experience, Skills, Education)
- [ ] Route each section through the correct prompt template
- [ ] Build output assembler: collects all AI-improved sections
- [ ] Integrate PDF generator: outputs a clean, ATS-friendly PDF

**Done when:** You can feed in an old resume and get a polished PDF back.

---

### Phase 3 — Feature Completion (Week 3)
**Goal:** All 3 v1 features working end-to-end.

- [ ] **Feature 1:** Bullet Polish — rewrite weak bullets with strong action verbs + metrics prompts
- [ ] **Feature 2:** Job Tailoring — feed in job description, AI aligns resume keywords/language
- [ ] **Feature 3:** Experience Updater — user describes new project/role in plain English, AI formats and inserts it

**Done when:** All 3 features work reliably on 3+ different resume samples.

---

### Phase 4 — Polish & Portfolio Prep (Week 4)
**Goal:** Make it presentable for GitHub and recruiters.

- [ ] Add error handling (bad input, LLM timeout, malformed output)
- [ ] Write a clean README with examples
- [ ] Record a short demo (screen record CLI in action)
- [ ] Push to GitHub with sample input/output files

---

## 🧠 Prompt Templates (v1 Starting Points)

### 1. Bullet Polish
```
You are a professional resume writer. 
Rewrite the following resume bullet point to be more impactful.
Use strong action verbs, quantify results where possible, and keep it under 2 lines.
Be concise and ATS-friendly.

Bullet: {bullet}

Rewritten bullet:
```

### 2. Job Tailoring
```
You are a resume coach. 
Given the resume section and job description below, rewrite the resume section 
to better match the job description's keywords and requirements.
Keep the same facts — only adjust language and emphasis.

Job Description: {job_description}
Resume Section: {resume_section}

Tailored resume section:
```

### 3. Experience Updater
```
You are a professional resume writer.
The user has described a new experience or project in plain English.
Convert it into 2-4 polished resume bullet points using strong action verbs.
Format for ATS compatibility.

User description: {user_input}

Resume bullets:
```

---

## 📅 Week 1 Sprint — Concrete Daily Tasks

| Day | Task |
|---|---|
| Day 1 | Install Ollama, pull Mistral 7B, run a test prompt in terminal |
| Day 2 | Write `llm_client.py` — Python wrapper to send/receive from Ollama |
| Day 3 | Build `prompts.py` — store all 3 prompt templates as functions |
| Day 4 | Write `test_prompts.py` — run 5 sample bullets through Prompt 1, evaluate output |
| Day 5 | Refine prompts based on output quality, test Prompts 2 & 3 |
| Day 6–7 | Rest or explore: try swapping LLaMA 3 vs Mistral, compare output quality |

---

## 📁 Suggested Project Structure

```
resume-ai/
├── main.py                  # CLI entry point
├── llm_client.py            # Ollama API wrapper
├── prompts.py               # All prompt templates
├── input_parser.py          # Read and section a resume file
├── output_builder.py        # Assemble AI outputs into structured resume
├── pdf_generator.py         # Generate final PDF
├── tests/
│   └── test_prompts.py      # Evaluate prompt output quality
├── samples/
│   ├── sample_resume.txt    # Test input
│   └── sample_jd.txt        # Sample job description
├── outputs/                 # Generated PDFs go here
├── requirements.txt
└── README.md
```

---

## ⚡ First Command to Run (Day 1)

```bash
# Install Ollama (Mac/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Pull your model
ollama pull mistral

# Test it immediately
ollama run mistral "Rewrite this resume bullet: Responsible for helping customers"
```

---

## 🎯 v1 Success Criteria

- [ ] Accepts a plain text resume as input
- [ ] Polishes all bullet points automatically
- [ ] Can tailor the resume to a pasted job description
- [ ] Can add a new experience from plain English description
- [ ] Outputs a clean, readable PDF
- [ ] Runs 100% offline on your machine
