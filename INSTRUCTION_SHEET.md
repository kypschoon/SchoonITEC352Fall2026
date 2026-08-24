# Instructor Instruction Sheet — Playlist Manager (1-hour)

**Overview (1 line):**
Students implement a small playlist manager focused on procedural skills: local/global variables, functions with and without returns, and list operations.

**Materials**
- Computer with Python 3
- Code editor/IDE
- Files: playlist.py, test_playlist.py (provided in this package)

**Schedule (60 minutes)**
- 0–5 min: Introduce objectives and deliverables.
- 5–10 min: Hand out starter code, read spec aloud.
- 10–45 min: Student coding time (pairs recommended). Instructor circulates.
- 45–55 min: Students run tests and prepare a 1-minute explanation of one scope decision.
- 55–60 min: Quick wrap-up and collect submission method (GitHub gist, LMS upload, or email).

**Student deliverables**
- Completed `playlist.py` meeting the spec:
  * global list `playlist` with >=3 songs
  * add_song(title) — modifies playlist (no return)
  * remove_song(title) — removes first matching and returns True/False
  * find_song(title) — returns index or -1
  * get_playlist_copy() — returns a shallow copy
  * replace_song(old, new) — replaces first occurrence and returns (index, new) or None
  * main() demonstrating at least one returning and one non-returning function
- Passing `test_playlist.py` assertions

**Assessment & submission**
- Ask students to run `python test_playlist.py`. Passing tests = major functional credit.
- Quick oral check: pick a student to explain why their `add_song` either used `global` or didn't (expect answers about mutation vs rebinding).
- Collect files via LMS, or request a GitHub gist link.

**Common pitfalls to watch for**
- Assigning to `playlist` inside a function (rebinds name — requires `global`).
- Forgetting `return` in a function that should return a value.
- Returning the global list itself from `get_playlist_copy()` (should return a copy).

**Extensions (if students finish early)**
- Ban `global`: require functions to return new state and have `main()` reassign.
- Add CSV save/load (file I/O).
- Use dictionaries for songs (id, title, artist).

**LMS-ready assignment text (copy/paste)**

Title: Playlist Manager — Procedural Python (1 hour)

Description:
Implement functions in `playlist.py` to manage a playlist. Your solution will be graded for correct use of global/local scope, functions with and without return values, and list manipulation. Run `python test_playlist.py` — all tests must pass before submission.

Deliverables:
- Upload `playlist.py` (single file) to the assignment submission area.
- In the submission comments, write one sentence explaining a scope decision you made (e.g., "I used mutation in add_song to avoid rebinding the global variable").

Grading:
Use the attached rubric (included).
