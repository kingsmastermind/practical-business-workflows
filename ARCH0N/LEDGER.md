# Presentation repair ledger

## 2026-10-21 — Rejected workflow and narration
Reported: Operator found the button demo changed only text and requested removal, no narration, explanatory text below the video and animation within it.
Stage: repair.
Root cause: index.html invented generic workflow cards; media reel reused static frames plus unrequested synthetic narration rather than established product proof.
Fix: replace cards with silent guided product-capture video, animated focus, readable below-player chapter guide.
Guard: no advance/reset workflow buttons; MP4 contains no audio stream; guide has meaningful captions; use safe original product captures.
References: 800z onboarding-es BRIEF/DESIGN; AXE6123,6245,6248,6331. Never substitute a mock UI for a real product capture or quote historical scale numbers as current.
Verified: ffprobe reports exactly48seconds and one video stream/no audio; full decode passes. Source screenshot privacy inspected. Browser shows old workflow controls absent and below-player guide present. Public timestamp seek confirmed with duration48/seekable0–48; guide advanced to Research workspace during playback. Public page contains replacement source and no rejected buttons. AXE144547.
Lesson: specific buyer problem + visible product evidence first. Decorative steps are not a product demonstration.

## 2026-10-21 — Product skins, cursor tours and buyer relevance
Reported: operator rejects slow zoom and generic shell aesthetic; requests recovered skins, one walkthrough per product then montage, company-branded example, CRM Pipeline, traditional Fleet, action queue, clean command center/security and daily work. AXE144637/144665.
Root cause: prior walkthrough used static proof captures without product navigation and a generic visual wrapper.
Fix: seven reconstructed synthetic demo view sets; cursor-led tab navigation, brief highlights, individual silent24s tours and21s excerpt montage. Official Lumen logo/observed colors on complete candidate proof page. No source/backend repo or production dashboard changes.
Clarification: current operator explicitly requests cleaned/skinned presentation views; these reconstructions are labeled accordingly and never asserted as live production footage. This supersedes the prior presentation restriction only within synthetic reconstruction scope.
Guard: all28 browser view captures observed;8videos metadata verified, zero audio; product/state pages differ. Official logo visibility checked. Shared pitch acceptance requires source/relevance/skin/video/guide/human review before visual acceptance.
Verified: local browser checks and manifests. Public Pages build263f321 verified;10exact byte checks for page/example and8videos. Legacy reel aliases updated to the new montage in a followup.
Lesson: UI navigation must reveal useful product content. A styled table is illustrative proof, not a live integration acceptance.
