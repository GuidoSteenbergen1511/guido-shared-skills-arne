# GenAI Definition: What Counts as Generative AI

## Core Definition
**Generative AI** refers to AI systems that can generate new content (text, images, audio, video, code) based on learned patterns from training data.

---

## INCLUDE These Technologies

### Large Language Models (LLMs)
| Technology | Examples |
|------------|----------|
| OpenAI | GPT-4, GPT-4o, GPT-3.5, ChatGPT |
| Anthropic | Claude, Claude 3.5 Sonnet, Claude Opus |
| Google | Gemini, Gemini Pro, Gemini Ultra, PaLM |
| Meta | Llama, Llama 2, Llama 3 |
| Open Source | Mistral, Mixtral, Falcon, Phi |
| Enterprise | IBM WatsonX, AWS Bedrock (when using LLMs) |

### Image Generation
| Technology | Examples |
|------------|----------|
| OpenAI | DALL-E, DALL-E 3 |
| Stability AI | Stable Diffusion, SDXL |
| Midjourney | Midjourney v5, v6 |
| Adobe | Firefly |
| Google | Imagen |

### Other Generative Modalities
| Type | Examples |
|------|----------|
| Code Generation | GitHub Copilot, Cursor, Codeium, Amazon CodeWhisperer |
| Video Generation | Runway, Pika, Sora |
| Audio/Music | Eleven Labs, Murf, Suno |
| 3D Generation | Point-E, Shape-E |

### GenAI Applications
- AI Assistants / Chatbots (powered by LLMs)
- Content generation (marketing copy, product descriptions)
- AI-powered search (semantic search, RAG)
- Document summarization
- Code completion and generation
- Creative design assistance
- Personalized recommendations (when LLM-powered)

---

## EXCLUDE These Technologies

### Traditional Machine Learning
| Category | Examples | Why Excluded |
|----------|----------|--------------|
| Demand Forecasting | Prophet, ARIMA, DeepAR | Predictive, not generative |
| Recommendation Engines | Collaborative filtering, matrix factorization | Retrieval, not generation |
| Predictive Analytics | Churn prediction, CLV models | Classification/regression |
| Anomaly Detection | Isolation Forest, autoencoders | Detection, not generation |
| Time Series | LSTM for forecasting | Prediction, not generation |

### Computer Vision (Non-Generative)
| Category | Examples | Why Excluded |
|----------|----------|--------------|
| Object Detection | YOLO, R-CNN | Classification, not generation |
| Image Classification | ResNet, EfficientNet | Classification |
| OCR | Tesseract, standard OCR | Recognition, not generation |
| Face Recognition | DeepFace, FaceNet | Identification |

### Rule-Based / Traditional Automation
| Category | Examples | Why Excluded |
|----------|----------|--------------|
| RPA | UiPath, Automation Anywhere | Scripted automation |
| Business Rules | Decision trees, rule engines | Logic-based |
| Chatbots (scripted) | Flow-based chatbots | Not AI-generated responses |

---

## Edge Cases: Include With Caution

### Include if GenAI is Core Component
| Use Case | Include? | Reasoning |
|----------|----------|-----------|
| RAG-powered search | YES | Uses LLM for answer generation |
| AI recommendation with LLM explanations | YES | GenAI generates explanation |
| Computer vision + GenAI descriptions | YES | GenAI generates descriptions |
| Demand forecasting with LLM insights | MAYBE | Only if LLM generates novel insights |

### Exclude if GenAI is Minor Component
| Use Case | Include? | Reasoning |
|----------|----------|-----------|
| Dashboard with AI summary | NO | Core is visualization |
| CRM with AI note cleanup | MAYBE | Depends on depth |
| Email with spell check | NO | Basic NLP |

---

## Search Keywords

### Include Keywords (search queries)
```
"generative AI" "[Company]"
"GPT" "[Company]"
"ChatGPT" "[Company]"
"LLM" "[Company]"
"AI assistant" "[Company]"
"AI chatbot" "[Company]"
"content generation" "[Company]"
"DALL-E" "[Company]"
"Midjourney" "[Company]"
"Copilot" "[Company]"
"Claude" "[Company]" AI
```

### Exclude Keywords (negative filters)
```
"demand forecasting" (unless + "LLM")
"predictive analytics" (unless + "generative")
"recommendation engine" (unless + "LLM" or "GPT")
"machine learning" (too broad - need GenAI specifics)
```
