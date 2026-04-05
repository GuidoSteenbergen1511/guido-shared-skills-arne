# Source Quality Criteria

## Source Credibility Tiers

### Tier 1: Primary Sources (Highest Credibility)
| Source Type | Examples | Credibility |
|-------------|----------|-------------|
| Company official | Press releases, investor presentations, earnings calls | HIGH |
| Vendor case study | OpenAI customer stories, AWS case studies, Google Cloud customers | HIGH |
| Executive interview | CEO/CTO quotes in major publications | HIGH |
| Annual/quarterly reports | 10-K, investor day presentations | HIGH |

### Tier 2: Secondary Sources (High Credibility)
| Source Type | Examples | Credibility |
|-------------|----------|-------------|
| Major tech publications | TechCrunch, Wired, The Verge, Ars Technica | HIGH |
| Business publications | WSJ, Bloomberg, Reuters, Fortune, Forbes | HIGH |
| Industry analysts | Gartner, Forrester, McKinsey, BCG | HIGH |
| Trade publications | Retail Dive, Supply Chain Dive, WWD | MEDIUM-HIGH |

### Tier 3: Tertiary Sources (Medium Credibility)
| Source Type | Examples | Credibility |
|-------------|----------|-------------|
| Industry blogs | DigitalDefynd, RetailBoss, AI expert blogs | MEDIUM |
| News aggregators | Business Insider, Yahoo Finance | MEDIUM |
| Conference presentations | NRF, Shoptalk, Web Summit | MEDIUM |
| LinkedIn posts by executives | With supporting documentation | MEDIUM |

### Tier 4: Low Credibility (Use with Caution)
| Source Type | Examples | Credibility |
|-------------|----------|-------------|
| Anonymous blogs | No author attribution | LOW |
| User forums | Reddit, Quora (unverified) | LOW |
| Outdated sources | >24 months old for GenAI | LOW |
| Affiliate/sponsored content | Paid promotional content | LOW |

---

## Minimum Source Requirements

### For HIGH Confidence Rating
- At least 1 Tier 1 source (company official or vendor case study)
- At least 1 additional Tier 1 or Tier 2 source
- Total: 3+ sources recommended

### For MEDIUM Confidence Rating
- At least 2 Tier 1, 2, or 3 sources
- Sources must be independent (not citing each other)
- Metrics must be consistent (±15% variance acceptable)

### Automatic EXCLUSION
- Only 1 source available
- All sources are Tier 4
- Sources contradict each other on key metrics (>30% variance)
- Cannot verify GenAI technology claim

---

## Source Verification Checklist

### Step 1: URL Verification
- [ ] URL resolves (not 404)
- [ ] Content matches claimed information
- [ ] Page is from claimed publisher (not fake domain)

### Step 2: Content Verification
- [ ] Source explicitly mentions the company
- [ ] Source explicitly mentions GenAI technology (not just "AI")
- [ ] Metrics are stated (not just qualitative claims)
- [ ] Date is recent (within 24 months)

### Step 3: Cross-Reference Verification
- [ ] Second source found for same use case
- [ ] Metrics are consistent between sources
- [ ] No contradicting information found

### Step 4: GenAI Verification
- [ ] Specific GenAI technology mentioned (GPT, Claude, DALL-E, etc.)
- [ ] Not traditional ML rebranded as "AI"
- [ ] Generative capability confirmed (creates content, not just analyzes)

---

## Red Flags

### Content Red Flags
| Red Flag | Action |
|----------|--------|
| No specific metrics | Downgrade confidence or exclude |
| Vague "AI" without GenAI specifics | Search for more specific source |
| Metrics seem too good (+1000%) | Verify with additional source |
| Metrics seem made up (exactly +50.0%) | Verify with additional source |
| Future tense ("will implement") | Exclude - not implemented yet |
| Pilot only, no production | Note as "pilot" if including |

### Source Red Flags
| Red Flag | Action |
|----------|--------|
| No author listed | Downgrade to Tier 4 |
| Obvious SEO/content farm | Exclude |
| Heavy affiliate links | Downgrade credibility |
| Republished press release only | Find original + 2nd source |
| Paywall with no preview | Note limitation |

---

## Handling Discrepancies

### When Sources Conflict on Metrics
1. **Minor variance (±15%)**: Use average, note range in output
2. **Moderate variance (15-30%)**: Use most credible source, note discrepancy
3. **Major variance (>30%)**: Flag for manual review or exclude

### When Sources Conflict on Technology
1. Check which source is more recent
2. Prefer company-official source
3. Note uncertainty if cannot resolve

### When Sources Conflict on Timeline
1. Most recent source typically most accurate
2. Company official source takes precedence
3. Note if implementation is ongoing vs. completed

---

## Source Age Guidelines

### Preferred: 0-12 months
- GenAI moves fast
- Recent implementations more relevant
- Metrics more reliable

### Acceptable: 12-24 months
- Still useful for established use cases
- Verify if still active/relevant
- Note date in output

### Caution: 24-36 months
- Include only for landmark cases
- Verify current status
- Clearly note age

### Exclude: >36 months
- GenAI landscape has changed too much
- Metrics likely outdated
- Technology likely superseded
