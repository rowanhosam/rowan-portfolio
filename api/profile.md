# About Rowan (the assistant's only source of facts)

Edit this file to change what the chat assistant knows. Lines starting with
"TODO" are placeholders: the assistant ignores them.

## Basics
- Name: Rowan Elansary
- Role: Software engineer (full stack at the core) and Computer Science student
- Looking for: a Summer 2027 internship in software engineering: full stack, front end, back end, mobile and app design, or AI.
  Enjoys exploring across the stack.
- Location: Fresno, CA
- Email: rowanelansary123@gmail.com
- LinkedIn: linkedin.com/in/rowan-elansary
- GitHub: github.com/rowanhosam
- Experience: 1+ years across 5 internships, plus two research assistant roles
- Availability: Summer 2027 (internship), then returning to full-time studies.
  If asked for exact dates, say they're flexible and to get in touch.

## Summary
Builds full-stack applications, back-end services and REST APIs, and data
pipelines in production, and does AI/ML research in generative AI, RAG and
computer vision. Uses AI-assisted development tools daily (Copilot, Cursor,
Claude Code) while reviewing and testing all generated code.

## Education
- B.S. in Computer Science (accelerated B.S./M.S. program), California State
  University, Fresno. Expected December 2027. Full-time student.
- Dean's List, Spring 2025. Cybersecurity Fundamentals Certificate, Spring 2025.
- Coursework: Data Structures and Algorithms, Database Systems, Software
  Engineering, Computer Security.

## Experience
- AI & Innovation Intern, Lyles Construction Group (Lyles Services Co.), Fresno, CA.
  Aug 2026 to present.
  - The 2 survey apps below were Rowan's first two Lyles projects and are done
    and in production. Progress & Projection is the third and current project.
  - Contributes to Progress & Projection, Lyles' internal web platform for job
    costing and subcontract management, which replaces an older Angular system.
    It's a full-stack Next.js and .NET (C#) web app integrated with the company
    ERP, used by project managers, accounting and external subcontractors.
    Shipped workflow features, security and UX fixes, and automated tests
    through the team's CI and pull-request process.
  - Also contributes to other projects across the department.
  - Designed, built and shipped 2 survey apps, now in production, used by Lyles' subsidiary
    companies to collect customer satisfaction responses, each with a dashboard
    that tracks the results. Before sending a survey email, the apps pull from the
    company database to check that the work order or project has closed.
    Built with React, Node.js/Express REST APIs and SQL
    Server on Azure.
  - Built an automated data pipeline that processes large datasets of
    service-visit records every 15 minutes, integrating the company ERP and the
    Microsoft Graph API.
  - Found and fixed 4 security and data-integrity vulnerabilities before
    production; debugs and resolves production issues.
  - Works in 2-week Agile sprints with weekly stand-ups and code reviews.
- Website & Social Media Intern, Madera K-16 Collaborative, Fresno State. Current.
  - Runs the collaborative's website and social media channels.
- Full Stack Developer Intern, F3 Innovate, Fresno, CA. May 2026 to Aug 2026.
  - Svelte was used only here, for the front end.
  - Built a research-projects inventory feature end to end: Svelte UI,
    Python/FastAPI REST endpoints and PostgreSQL data models, including a TRL/CRL
    readiness-scoring engine.
  - Implemented JWT-based authentication, access control and asynchronous
    services for a platform used by farmers, professors and research assistants.
- Research Assistant, Generative AI, Computer Science Department, Fresno State.
  Jan 2026 to present.
  - The project is called Hibiki-AI (AIISLab at Fresno State). It lets people
    talk with a person from history in their own words. The first persona is
    Fred Hirasuna, a Nisei farmer and JACL leader from Fresno, who answers only
    from his oral-history interviews held by Fresno State's Henry Madden Library.
    Answers can come back as text, voice and lip-synced video.
  - How it works: a React client; a FastAPI service that retrieves passages
    from the interviews (RAG) to ground answers; and a GPU job pipeline that
    turns answers into speech, then lip-synced video, then smooth transitions.
  - Rowan's own contribution in code: the Synthetic Media Modulation step, an
    OpenCV cartoonization filter applied to every generated video so it is
    never mistaken for real footage of the (often deceased) person. Written
    from scratch (bilateral smoothing, posterized colors, light edge outlines)
    to avoid licensing problems in existing models; switched from k-means to
    posterization so a 30-second clip takes about 5 seconds. Tested on all
    900 frames of real reference footage; merged through a pull request.
  - Hibiki-AI won the People's Choice Award at the 2026 INSPIRE Convening
    (hosted by Learning Lab, theme "Reinventing Higher Education").
  - Uses retrieval-augmented generation (RAG) to ground model responses for an
    AI-driven historical persona platform.
  - Benchmarks generative AI models across speech, image and video, including 4
    zero-shot voice-cloning models (such as XTTS v2 and IndexTTS-2).
- Digital Health Intern, Valley Children's Hospital, Madera, CA. Sep 2025 to Dec 2025.
  - Cleaned, transformed and validated operational healthcare datasets and built
    data analysis reports for leadership.
- Computer Vision Research Assistant, Lyles College of Engineering, Fresno State.
  Jun 2025 to Aug 2025.
  - Built a real-time object detection and 3D localization system in Python with
    YOLOv8 and depth cameras, reaching 91% detection accuracy.
- Data Analyst Intern, Umida Ag & Terra Tech, Fresno, CA. Jun 2025 to Aug 2025.
  - Built Python automation scripts that cut reporting time by 80%.

## Projects
- Community membership website, evenstar-trading.com (2026): designed, built and
  deployed a responsive site serving 2,000+ users; manages hosting, deployments,
  version control and payment redirection.
- Personal iPhone apps in Swift and SwiftUI, built outside school and work (ongoing).
  Swift is used only for these personal projects, not at any job.
- This portfolio: static site plus a FastAPI chat service that calls Claude
  Haiku, rate limited per visitor; the intro video is AI-generated with the
  background removed frame by frame.

## Skills
- Strongest for coding interviews: C++ (takes coding assessments in C++), with a
  strong foundation in data structures, algorithms and object-oriented design.
- Languages: C++, Python (1+ years), C#, Java, JavaScript, TypeScript, SQL, Swift,
  Objective-C, HTML, CSS
- Back end: C#, REST APIs, Node.js, Express, FastAPI, asynchronous services, JWT
  authentication, third-party API integrations (ERP, Microsoft Graph)
- Front end and mobile: React (current work), Svelte (at F3 Innovate), Tailwind CSS, responsive UI, SwiftUI, iOS, macOS
- Data: SQL Server, PostgreSQL, BigQuery, SQLAlchemy, data modeling, data
  pipelines, Apache Spark (PySpark), data validation
- AI and ML: PyTorch, computer vision (YOLOv8), RAG, generative AI model evaluation
- Cloud and DevOps: Microsoft Azure, Docker, Linux (Ubuntu), Git, GitHub, GitHub Projects
- Web and social media: website management, social media content
- Practices: SDLC, Agile, code reviews, testing, debugging production issues,
  vulnerability remediation, AI-assisted development
