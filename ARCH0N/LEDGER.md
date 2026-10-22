# Presentation repair ledger

## 2026-10-21 — Rejected workflow and narration
Reported: Operator found the button demo changed only text and requested removal, no narration, explanatory text below the video and animation within it.
Stage: repair.
Root cause: index.html invented generic workflow cards; media reel reused static frames plus unrequested synthetic narration rather than established product proof.
Fix: replace cards with silent guided product-capture video, animated focus, readable below-player chapter guide.
Guard: no advance/reset workflow buttons; MP4 contains no audio stream; guide has meaningful captions; use safe original product captures.
References: 800z onboarding-es BRIEF/DESIGN; AXE6123,6245,6248,6331. Never substitute a mock UI for a real product capture or quote historical scale numbers as current.
Verified: ffprobe reports exactly48seconds and one video stream/no audio; full decode passes. Source screenshot privacy inspected. Browser shows old workflow controls absent and below-player guide present. Final public seek check pending. AXE144547.
Lesson: specific buyer problem + visible product evidence first. Decorative steps are not a product demonstration.
