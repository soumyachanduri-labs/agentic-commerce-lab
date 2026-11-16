# Agentic Commerce Lab
### Building an AI-Powered Shopping Assistant

**Python | OpenAI API | LLM Tool Calling | Agent Evaluation | E-Commerce**

## Overview

An experimental AI shopping agent designed to transform traditional product discovery into an intelligent, conversational shopping experience.

Instead of requiring customers to manually search, filter, and navigate checkout flows, the assistant interprets natural-language requests, discovers relevant products, and supports shopping-cart management and simulated checkout.

This project explores how AI agents can move beyond answering questions to executing meaningful commerce actions.

## The Problem

Traditional e-commerce experiences place significant effort on customers to:

- Translate their needs into search keywords.
- Navigate multiple filters and product listings.
- Compare products against preferences and constraints.
- Manage shopping carts and complete checkout.

**Product hypothesis:** An AI-powered shopping agent can reduce shopping friction by combining conversational understanding with reliable, controlled commerce actions.

## What I Built

### 1. Conversational Product Discovery
- Interpret natural-language shopping requests.
- Identify product requirements and preferences.
- Recommend products based on available catalog information.

### 2. Agent Tool Calling
- Connect the LLM to a product search function.
- Allow the agent to decide when product search is required.
- Return structured product information for recommendations.

### 3. Shopping Cart and Simulated Checkout
- Support shopping-cart operations.
- Simulate the checkout experience without initiating real payments.
- Explore the transition from product recommendations to transactional actions.

### 4. Agent Evaluation and Reliability
- Build an evaluation script to test shopping-agent behavior.
- Examine failures across different test scenarios.
- Iterate on agent instructions and tool behavior to improve reliability.

### 5. Seller Exposure and Marketplace Fairness
An ongoing enhancement explores reserving a configurable share of eligible recommendation slots for new sellers and unrated listings.

The design aims to balance:
- Buyer relevance and satisfaction.
- Strict compliance with buyer constraints.
- Fair exposure for new marketplace participants.

## High-Level Architecture

```text
Customer
   |
   v
Natural Language Shopping Request
   |
   v
LLM Shopping Agent
   |
   +--> Product Search Tool
   |        |
   |        v
   |    Product Catalog
   |
   +--> Cart Management
   |
   +--> Simulated Checkout
   |
   v
Customer Response

Separate Evaluation Pipeline
   |
   +--> Test Scenarios
   +--> Agent Outputs
   +--> Failure Analysis
```

## Key Product and Technical Decisions

**Tool calling over free-form responses:** Product information should come from a defined search tool rather than relying on the model to invent product details.

**Simulated checkout before live payments:** A controlled environment enables validation of transactional behavior without exposing real payment credentials or processing transactions.

**Evaluation as part of development:** Agent quality requires testing not only response fluency but also tool selection, constraint adherence, and action correctness.

**Marketplace fairness:** Recommendation quality must consider both customer relevance and healthy seller participation.

## Development Milestones

| Milestone | Status |
|---|---|
| Conversational shopping assistant | Completed |
| Product search tool calling | Completed |
| Cart management and simulated checkout | Completed |
| Initial evaluation framework | Implemented; refinement ongoing |
| New-seller exposure allocation | In progress |

## Evaluation Focus

The evaluation framework explores:

- **Tool selection:** Did the agent call the correct tool?
- **Constraint adherence:** Did recommendations satisfy hard buyer requirements?
- **Groundedness:** Were product details supported by catalog data?
- **Transaction correctness:** Were cart and checkout actions performed as expected?
- **Reliability:** How consistently does the agent handle varied shopping scenarios?

The initial evaluation run identified failing scenarios, providing opportunities for further debugging and refinement.

## Future Roadmap

- Improve agent evaluation coverage and reliability.
- Validate seller-exposure allocation against relevance metrics.
- Add persistent shopping-cart state.
- Explore payment integrations and transaction authorization.
- Introduce richer product catalogs and comparison capabilities.
- Explore interoperability standards for agentic commerce.

## Why This Project Matters

Agentic commerce introduces new product challenges beyond traditional search and checkout:

- How much autonomy should a shopping agent have?
- How do we prevent hallucinated product recommendations?
- When should the customer explicitly approve an action?
- How do we balance marketplace fairness with buyer relevance?
- How should agent quality be measured before deployment?

This project is an opportunity to explore those questions through working software and iterative product experimentation.

## About the Builder

Built by **Soumya Chanduri**, a Product Manager with 16 years of experience across AI/ML, payments, and e-commerce.

My professional experience includes building AI evaluation frameworks, ML-powered payment optimization, revenue forecasting, and large-scale marketplace payment experiences.

This repository reflects my interest in combining product strategy with hands-on technical implementation.

**GitHub:** https://github.com/soumyachanduri-labs
