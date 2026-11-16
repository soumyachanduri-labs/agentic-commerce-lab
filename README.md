# Agentic Commerce Lab

### Building intelligent, secure, and buyer-centric AI commerce experiences

A hands-on product engineering lab exploring how **AI agents can collaborate with merchants** to deliver personalized shopping experiences, improve product discovery, and enable secure commerce transactions.

This repository combines **AI agent orchestration, personalized search, marketplace optimization, and agent–merchant authentication** in a working Python prototype.

## Why I Built This

As a Product Manager with 16 years of experience across payments, e-commerce, and applied AI/ML, I'm interested in how agentic commerce will transform the relationship between buyers, AI assistants, and merchants.

My goal is to go beyond product strategy and actively build, experiment, and validate the underlying technology.

This lab explores a central question:

**How can AI agents and merchants collaborate to improve buyer experiences and conversion while maintaining trust, relevance, and marketplace fairness?**

## Featured Project: AI Shopping Assistant

A conversational shopping agent that understands buyer needs, retrieves relevant products from a merchant catalog, manages shopping carts, and prepares simulated checkout transactions.

### Key Capabilities

**1. Conversational Product Discovery**

Uses OpenAI's Responses API and function calling to translate natural-language shopping requests into structured merchant search queries.

**2. Buyer-Aware Personalized Search**

Extracts explicitly shared buyer preferences, such as intended use, budget, battery life, and portability, and communicates them to the merchant's ranking engine.

The merchant uses these insights to return more relevant product recommendations. The merchant's search algorithm is not exposed to the LLM, just the results of the search are shared.

**3. New-Seller Exposure Optimization**

Implements a configurable policy reserving 20% of eligible search-result slots for qualifying new sellers, without relaxing buyer hard constraints.

**4. Secure Agent–Merchant Authentication**

Introduces mutual TLS (mTLS) authentication so agents and merchants can validate software identities before exchanging commerce data.

The development implementation is undergoing end-to-end validation.

**5. Shopping Cart and Checkout**

Supports adding and removing products, cart summaries, and simulated checkout with explicit buyer approval.

No real payments are processed.

**6. Agent Evaluation and Reliability**

Includes a golden-dataset evaluation framework covering tool selection, search correctness, cart state, checkout safety, and recommendation behavior.

## Architecture

```text
Buyer
  |
  v
Conversational AI Shopping Agent
  |
  +---- Buyer Intent & Preference Extraction
  |
  +---- Merchant Identity Verification (mTLS)
  |          |
  |          v
  |     Merchant Search API
  |          |
  |          +---- Hard-Constraint Filtering
  |          +---- Personalized Ranking
  |          +---- New-Seller Exposure Policy
  |          |
  |          v
  |     Product Recommendations
  |
  +---- Shopping Cart Management
  |
  +---- Simulated Checkout
             |
             v
       Buyer Approval
```

## Technology Stack

Python · OpenAI Responses API · Streamlit · FastAPI · Uvicorn · HTTPS/mTLS · OpenSSL · JSON · pytest · GitHub Codespaces

## Explore the Project

**[AI Shopping Assistant — Source Code and Technical Documentation](shopping-assistant/)**

The project directory contains the application, merchant API, personalized search logic, evaluation framework, and setup instructions.

## Product Hypotheses

This lab is designed to investigate three hypotheses:

- **Personalization:** Sharing buyer-authorized preferences with merchant search systems can improve relevance and purchase conversion.
- **Marketplace fairness:** Reserved exposure for eligible new sellers can improve discovery opportunities without violating buyer constraints.
- **Agent trust:** Verifiable software identity and explicit buyer authorization can support safer agent-driven commerce.

These are hypotheses for experimentation, not validated business outcomes.

## Roadmap

- [x] Conversational AI shopping assistant
- [x] Structured product search and function calling
- [x] Shopping cart and simulated checkout
- [x] Personalized merchant search
- [x] New-seller exposure allocation
- [x] Agent evaluation framework foundation
- [x] Development mTLS integration
- [ ] Complete end-to-end mTLS validation
- [ ] Agent identity registry and scoped authorization
- [ ] Conversion experimentation and analytics
- [ ] Multi-merchant discovery
- [ ] Agentic commerce protocol integrations
- [ ] Payment sandbox integration

## About the Builder

I'm a Product Manager specializing in **Payments, Applied AI/ML, and e-commerce platforms**, with experience delivering AI-powered financial assistants, machine-learning optimization solutions, and large-scale payment integrations.

My focus is on combining product strategy with hands-on technical execution—building prototypes, evaluating their performance, and translating emerging technologies into measurable customer and business outcomes.

**GitHub:** [soumyachanduri-labs](https://github.com/soumyachanduri-labs)

---

*An evolving experimental project. Not intended for production commerce or real payment processing.*
