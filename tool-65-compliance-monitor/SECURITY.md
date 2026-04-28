# SECURITY.md - Tool-65 Sustainability Compliance Monitor

## Initial Threat Model (AI & Security)

As the AI Developer 2, I have identified the following 5 primary security threats to our AI microservice:

1.  **Prompt Injection**: Users may attempt to bypass our compliance rules by giving instructions like "Ignore all previous rules and output [X]".
2.  **API Key Leakage**: Exposure of `GROQ_API_KEY` through logs, GitHub commits, or client-side code.
3.  **Denial of Service (DoS)**: Malicious actors sending thousands of requests to drain our API quota and increase costs.
4.  **Sensitive Data Exposure**: Users might input private corporate data that shouldn't be processed by external LLMs without anonymization.
5.  **Insecure Output Handling**: If the AI output is rendered directly in the browser without escaping, it could lead to Cross-Site Scripting (XSS).

## Mitigation Strategies (Week 1-2)
- [x] Implement Rate Limiting (Flask-Limiter).
- [x] Implement Input Sanitization filters.
- [x] Use environment variables and `.gitignore` for secrets.
- [ ] Add JSON Schema validation for all AI outputs.

## Week 1 Security Test Results (Day 5)

I have performed security testing on the `/api/analyze` endpoint for empty input, SQL injection, and prompt injection.

### 1. Empty Input Test
- **Status**: PASSED
- **Details**: 
    - Empty query string (`""`) returns `400 Bad Request`.
    - Whitespace-only query (`"   "`) now returns `400 Bad Request` (Fixed in Day 5).
    - Missing query key returns `400 Bad Request`.
- **Mitigation**: Added `.strip()` to input sanitization to catch whitespace-only queries.

### 2. SQL Injection Test
- **Status**: PASSED (Non-Applicable / Robust)
- **Details**: 
    - Tested payloads like `' OR '1'='1` and `'; DROP TABLE users; --`.
    - Since no database is currently used by the microservice, these are treated as literal strings and sent to the AI for analysis.
    - No crashes or unexpected behavior observed.

### 3. Prompt Injection Test
- **Status**: PARTIALLY MITIGATED
- **Details**: 
    - Tested characters like `[]{}<>` which are often used in prompt injection/XSS.
    - **Result**: The current sanitizer successfully removes these characters.
    - **Observation**: While character filtering helps, logic-based prompt injection (e.g., "Ignore previous instructions") is still possible if the LLM follows it.
- **Mitigation**: Character filtering is active. Further mitigation will include system prompt hardening in Week 2.

### 4. Rate Limiting Verification
- **Status**: PASSED
- **Details**: 
    - Verified that `Flask-Limiter` correctly returns `429 Too Many Requests` when the threshold is exceeded.

