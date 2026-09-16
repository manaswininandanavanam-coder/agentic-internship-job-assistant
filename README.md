# Agentic AI-Based Internship and Job Discovery and Application Assistant

## 📌 Project Overview

The Agentic AI-Based Internship and Job Discovery and Application Assistant is an AI-powered career assistance platform designed to help students discover relevant internship opportunities based on their resume, skills, and career interests.

The system uses multiple AI agents to analyze the student's resume, discover internships, calculate skill compatibility, identify skill gaps, provide personalized learning guidance, prepare application materials, and track applications.

---

## 🎯 Objectives

- Analyze student resumes automatically.
- Extract skills, education, projects and experience.
- Discover real internship opportunities.
- Match internships with the student's skills.
- Rank internships based on skill compatibility.
- Identify missing skills.
- Generate personalized learning roadmaps.
- Use RAG to retrieve relevant resume information.
- Assist in preparing internship applications.
- Track internship application status.

---

## 🧠 Agentic AI Architecture

The system follows a multi-agent architecture.

```text
                    ┌─────────────────────┐
                    │   React Frontend    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Flask Backend    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ AI Orchestrator     │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
 Resume Agent          Job Discovery Agent      Matching Agent
        │                      │                      │
        ▼                      ▼                      ▼
 Resume Analysis          Adzuna API          Skill Matching
                               │
                               ▼
                         Ranking System
                               │
                               ▼
                         RAG System
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
           Skill Gap Agent           Application Agent
                  │                         │
                  ▼                         ▼
          Learning Roadmap           Application Help
                                            │
                                            ▼
                                  Tracking Agent
                                            │
                                            ▼
                                        SQLite