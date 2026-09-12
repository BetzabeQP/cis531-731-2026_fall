<!--
yaml_schema_version: "2.2"
document_version: "1.0"
document_last_updated_date: "2026-09-11"
-->

<div align="center">
 <strong>🏫 Active Course Repositories:</strong> &nbsp;
 <a href="https://github.com/kddresearch/cis531-731-2026_fall">CIS 531/731</a> &nbsp;|&nbsp;
 <a href="https://github.com/kddresearch/cis536-736-2026_fall">CIS 536/736</a>
</div>

<div align="center">
 <h1>🧪 CIS 531/731 - Programming Techniques for Data Science and Analytics</h1>
 <p>
 <strong>Semester:</strong> Fall 2026 | <strong>Instructor:</strong> William H. Hsu, Ph.D.<br>
 <strong>Status:</strong> ACTIVE | <strong>Canvas LMS:</strong> <a href="https://k-state.instructure.com/courses/201513">Closed SSO Portal</a>
 </p>
</div>

<hr>

## 📖 Overview

Central repository for CIS 531/731 (Fall 2026) academic execution. This repository manages the DevContainer environments, Machine Problems (MPs), and primary codebase for students learning modern data science programming techniques. 

> **⚠️ Single Source of Truth (SSOT) Notice**
> This repository is the designated SSOT for all public-facing course materials, assignments, and infrastructure. While grades and closed discussions occur in the Canvas SSO environment, all operational state, Machine Problems (MPs), codebases, and structural rubrics MUST be committed here before being mirrored. A non-paywalled HTML mirror of Canvas content is derived from this repository.

<hr>

## 🗂️ Repository Structure

| Directory / File | Description |
| :--- | :--- |
| `assignments/` | Machine Problems (MPs), homework specifications, and project rubrics. |
| `lectures/` | Slide assets, lecture notes, and recording links. |
| `docker/` | DevContainer specifications, environment variables, and compute fallback scripts. |
| `src/` | Starter code, grading scripts, and baseline implementations. |
| `README.md` | This file. |

<hr>

## 🚀 Quick Start & Execution

**1. Prerequisites**
* Git client
* Docker Desktop & VS Code (for DevContainer deployment)

**2. Initialization**
```bash
git clone [https://github.com/kddresearch/cis531-731-2026_fall.git](https://github.com/kddresearch/cis531-731-2026_fall.git)
cd cis531-731-2026_fall
# Open in VS Code to initialize the DevContainer

```

## 🦅 Lab Execution Protocols

All Teaching Assistants and GRAs operating in this repository fall under the KDD Lab **Keep Flying Directive v2.1**.

* **Observable State:** Progress is measured by commits, drafts, logs, and reproducible outputs—not intentions.


* **The Triad:** When opening an issue or Pull Request, provide explicit goals, current blockers, and proposed next actions.


* **Artifact-Gated Routing:** Do not request synchronous meetings for routine status updates. Push your grading state or syllabus updates to this repository first.



## 👥 Instructional Staff

| Role | Name | GitHub Handle |
| --- | --- | --- |
| **Instructor** | William H. Hsu | [@banazir](https://www.google.com/search?q=https://github.com/banazir) |
| **Head TA** | [TBD] | [@GITHUB_HANDLE] |

```

***

**4. CSS / "Skins" for HTML5-Friendly Markdown**

Yes, but it depends entirely on the rendering engine. Markdown itself does not process CSS; it relies on the platform transforming it into HTML. 

1.  **Native GitHub View:** GitHub strictly sanitizes Markdown. It strips out `<link rel="stylesheet">`, `<style>` blocks, and external classes to prevent XSS attacks. The only way to style native GitHub Markdown is by using inline CSS within HTML tags (e.g., `<div style="background-color: #f8f9fa;">`), exactly as you did in the MP2 HTML block.
2.  **GitHub Pages (Jekyll):** If you route your repository through GitHub Pages to create the non-paywalled mirror, you can apply global CSS skins. You place a `style.css` in an `/assets/css/` directory and configure the `_config.yml` to use a specific theme. The Markdown is automatically wrapped in that CSS when viewed on the `.github.io` domain.
3.  **Canvas LMS Integration:** Canvas strips most external stylesheets but supports its own internal CSS classes (like `instructure_ui`) and inline styles. 

**Architectural Recommendation:** If your goal is to write a single `.md` file that renders beautifully in both GitHub and Canvas, **do not attempt to link external CSS**. Instead, maintain a library of pre-styled HTML `<div>` wrappers (like the MP2 block) and inject your standard Markdown inside them. This is the only method that survives the sanitization protocols of both SSO Canvas and GitHub's native viewer.

***

**Updated Blocker Queue**

🚨 **ACTIVE BLOCKER:** Post MP3 and update Dockerfile/DevContainer for CIS 531/731 (Due Today: Fri 11 Sep 2026).
⚠️ **PENDING BLOCKER 1:** Serialize CIS 536/736 deliverables for the weekend.
⚠️ **PENDING BLOCKER 2:** Process K.D.D.'s vLLM meeting telemetry (`.vtt` file) regarding OpenReview links and X.C.

```
